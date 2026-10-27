"""
Unit and Integration Tests for Event-Driven GCS Ingest Trigger.
Tests GCS path parsing, idempotent manifest replay, purge logic, and CloudEvent dispatch.
"""

import unittest
from unittest.mock import MagicMock, patch
from datetime import date, datetime
from cloudevents.http import CloudEvent

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import main


class TestGcsIngestTrigger(unittest.TestCase):

    def test_parse_gcs_path_valid(self):
        cases = [
            ("raw/index_0001/data.csv", ("index_0001", "data.csv")),
            ("raw/index_0696/sub/loans_2026.csv", ("index_0696", "loans_2026.csv")),
            ("raw/index_0020/rail_tickets.csv", ("index_0020", "rail_tickets.csv")),
            ("raw/index_0500/vehicles_spb.csv", ("index_0500", "vehicles_spb.csv")),
            ("raw/index_0080/gaming_profiles.csv", ("index_0080", "gaming_profiles.csv")),
        ]
        for path, expected in cases:
            with self.subTest(path=path):
                result = main.parse_gcs_path(path)
                self.assertEqual(result, expected)

    def test_parse_gcs_path_invalid(self):
        invalid_cases = [
            "bronze/data.csv",
            "silver/index_0001/file.csv",
            "raw/just_a_file.csv",
            "metadata/catalog.yaml",
        ]
        for path in invalid_cases:
            with self.subTest(path=path):
                self.assertIsNone(main.parse_gcs_path(path))

    @patch("main.get_bigquery_client")
    def test_idempotent_manifest_new_file(self, mock_get_client):
        mock_bq = MagicMock()
        mock_get_client.return_value = mock_bq

        # Mock SELECT query returning empty result (new file)
        mock_query_job = MagicMock()
        mock_query_job.result.return_value = []
        mock_bq.query.return_value = mock_query_job

        first_date, first_ts, is_reupload, reupload_count = main.check_and_update_manifest(
            bq_client=mock_bq,
            file_path="gs://my-bucket/raw/index_0001/dump.csv",
            file_name="dump.csv",
            source_id="index_0001",
            file_hash="hash123"
        )

        self.assertFalse(is_reupload)
        self.assertEqual(reupload_count, 0)
        self.assertEqual(first_date, date.today())
        # Assert insert statement was triggered
        self.assertTrue(mock_bq.query.called)

    @patch("main.get_bigquery_client")
    def test_idempotent_manifest_reupload_preserves_date(self, mock_get_client):
        mock_bq = MagicMock()
        mock_get_client.return_value = mock_bq

        # Mock SELECT query returning existing row from 2026-01-15
        mock_row = MagicMock()
        mock_row.first_ingest_date = date(2026, 1, 15)
        mock_row.first_ingest_timestamp = datetime(2026, 1, 15, 10, 0, 0)
        mock_row.reupload_count = 1

        mock_query_job = MagicMock()
        mock_query_job.result.return_value = [mock_row]
        mock_bq.query.return_value = mock_query_job

        first_date, first_ts, is_reupload, reupload_count = main.check_and_update_manifest(
            bq_client=mock_bq,
            file_path="gs://my-bucket/raw/index_0001/dump.csv",
            file_name="dump.csv",
            source_id="index_0001",
            file_hash="hash_updated"
        )

        # Assert original 2026-01-15 date is preserved!
        self.assertTrue(is_reupload)
        self.assertEqual(first_date, date(2026, 1, 15))
        self.assertEqual(first_ts, datetime(2026, 1, 15, 10, 0, 0))
        self.assertEqual(reupload_count, 2)

    @patch("main.get_bigquery_client")
    def test_purge_old_file_records(self, mock_get_client):
        mock_bq = MagicMock()
        mock_get_client.return_value = mock_bq

        mock_res = MagicMock()
        mock_res.num_dml_affected_rows = 1500
        mock_query_job = MagicMock()
        mock_query_job.result.return_value = mock_res
        mock_bq.query.return_value = mock_query_job

        deleted = main.purge_old_file_records(
            bq_client=mock_bq,
            table_id="medallion-project-512608.bronze.raw_index_0001",
            file_name="dump.csv",
            ingest_date=date(2026, 1, 15)
        )
        self.assertEqual(deleted, 1500)

    @patch("main.get_bigquery_client")
    def test_cloudevent_dispatch_success(self, mock_get_client):
        mock_bq = MagicMock()
        mock_get_client.return_value = mock_bq

        # Mock manifest check (new file)
        mock_query_res = MagicMock()
        mock_query_res.result.return_value = []
        mock_bq.query.return_value = mock_query_res

        # Mock load job
        mock_load_job = MagicMock()
        mock_load_job.output_rows = 500
        mock_bq.load_table_from_uri.return_value = mock_load_job

        event_attributes = {
            "type": "google.cloud.storage.object.v1.finalized",
            "source": "//storage.googleapis.com/buckets/medallion-project-512608-raw-data",
        }
        event_data = {
            "bucket": "medallion-project-512608-raw-data",
            "name": "raw/index_0001/investigator_drop_2026.csv",
            "size": "1048576",
            "md5Hash": "dummyMd5==",
        }
        cloud_event = CloudEvent(event_attributes, event_data)

        response = main.on_gcs_object_finalized(cloud_event)

        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["source_id"], "index_0001")
        self.assertEqual(response["rows_loaded"], 500)
        self.assertFalse(response["is_reupload"])

    @patch("main.get_bigquery_client")
    def test_downstream_pipeline_metadata_driven(self, mock_get_client):
        mock_bq = MagicMock()
        mock_get_client.return_value = mock_bq

        # Mock catalog query returning METADATA_DRIVEN
        mock_row = MagicMock()
        mock_row.pipeline_type = "METADATA_DRIVEN"
        mock_row.is_active = True

        mock_query_job = MagicMock()
        mock_query_job.result.return_value = [mock_row]
        mock_bq.query.return_value = mock_query_job

        result = main.trigger_downstream_pipeline(
            bq_client=mock_bq,
            source_id="index_0042",
            ingest_date=date(2026, 10, 26),
            started_at=datetime(2026, 10, 26, 10, 0, 0)
        )

        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["pipeline_type"], "METADATA_DRIVEN")
        self.assertTrue(mock_bq.query.called)

    @patch("main.dataform_v1")
    @patch("main.get_bigquery_client")
    def test_downstream_pipeline_dataform_dag(self, mock_get_client, mock_df_v1):
        mock_bq = MagicMock()
        mock_get_client.return_value = mock_bq

        # Mock Dataform Client and methods
        mock_df = MagicMock()
        mock_df_v1.DataformClient.return_value = mock_df
        mock_comp = MagicMock()
        mock_comp.name = "comp_test"
        mock_df.create_compilation_result.return_value = mock_comp

        mock_inv = MagicMock()
        mock_inv.name = "inv_test"
        mock_inv.state.name = "SUCCEEDED"
        mock_df.create_workflow_invocation.return_value = mock_inv
        mock_df.get_workflow_invocation.return_value = mock_inv

        # Mock catalog query returning DATAFORM_DAG
        mock_row = MagicMock()
        mock_row.pipeline_type = "DATAFORM_DAG"
        mock_row.is_active = True

        mock_query_job = MagicMock()
        mock_query_job.result.return_value = [mock_row]
        mock_bq.query.return_value = mock_query_job

        result = main.trigger_downstream_pipeline(
            bq_client=mock_bq,
            source_id="index_0020",
            ingest_date=date(2026, 10, 26),
            started_at=datetime(2026, 10, 26, 10, 0, 0)
        )

        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["pipeline_type"], "DATAFORM_DAG")
        self.assertTrue(mock_bq.query.called)
        self.assertTrue(mock_df.create_workflow_invocation.called)


if __name__ == "__main__":
    unittest.main()

from unittest.mock import patch

import pytest
from pydantic import ValidationError

from registry.functions.udfs import WorkUdf
from sections.forces.validators.base import base_validation
from sections.forces.validators.callsign import validate_callsign
from sections.forces.validators.category import validate_category
from sections.forces.validators.mos_code import validate_mos_code
from sections.forces.validators.tag_number import validate_tag_number
from sections.forces.validators.unit_code import validate_unit_code
from validators.death_date import death_date


def test_work_udf_valid_minimal_data():
    data = {"fn": "work_udf"}
    model = WorkUdf.model_validate(data)
    assert model.fn == "work_udf"
    assert model.post is None
    assert model.date_start is None
    assert model.date_end is None
    assert model.company is None
    assert model.company_address is None
    assert model.comment is None


def test_work_udf_valid_full_data():
    data = {
        "fn": "work_udf",
        "post": "post_value",
        "date_start": "2023-01-01",
        "date_end": "2023-12-31",
        "company": "company_name",
        "company_address": "company_address",
        "comment": "comment_value",
    }

    model = WorkUdf.model_validate(data)
    assert model.fn == "work_udf"
    assert model.post == "post_value"
    assert model.date_start == "2023-01-01"
    assert model.date_end == "2023-12-31"
    assert model.company == "company_name"
    assert model.company_address == "company_address"
    assert model.comment == "comment_value"


def test_work_udf_failure_extra_field_forbidden():
    data = {
        "fn": "work_udf",
        "post": "post_value",
        "date_starr": "2023-01-01",
        "date_end": "2023-12-31",
    }

    with pytest.raises(ValidationError) as err:
        WorkUdf.model_validate(data)

    assert "date_starr" in str(err.value)
    assert "Extra inputs are not permitted [type=extra_forbidden" in str(err.value)


class TestDeathDate:

    @patch("validators.death_date.date_validation")
    def test_invalid_death_date(self, mock_validation):
        mock_validation.return_value = None
        actual = death_date("invalid_date", "01.01.1990")
        assert actual is None
        mock_validation.assert_called_once()

    def test_no_birth_date_provided(self):
        actual = death_date("2023.01.01", "", "%Y.%d.%m")
        assert actual == "01.01.2023"

    def test_invalid_birth_date(self):
        actual = death_date("01.01.2023", "invalid_bd")
        assert actual == "01.01.2023"

    def test_birth_after_death(self):
        actual = death_date("01.01.2000", "01.01.2010")
        assert actual is None

    def test_valid_dates_provided(self):
        actual = death_date("01.01.2020", "01.01.1980")
        assert actual == "01.01.2020"

    def test_only_date_provided(self):
        actual = death_date("01.01.2021")
        assert actual == "01.01.2021"


class TestForces:
    class TestCallsign:
        def test_validate_callsign(self):
            actual = validate_callsign("- Call`  Sign .")
            assert actual == "Call Sign"

        def test_validate_callsign_invalid(self):
            actual = validate_callsign("---")
            assert actual is None

        def test_validate_callsign_missing(self):
            actual = validate_callsign("")
            assert actual is None

        def test_validate_callsign_invalid_four_spaces(self):
            actual = validate_callsign("ca ll si gn space")
            assert actual is None

        def test_validate_callsign_invalid_single_symbol(self):
            actual = validate_callsign("Aaaa")
            assert actual is None

    class TestCategory:
        def test_validate_category_mob(self):
            actual = validate_category("Мобилизованный")
            assert actual == 0

        def test_validate_category_contract(self):
            actual = validate_category("Контрактная Служба")
            assert actual == 1

        def test_validate_category_conscript(self):
            actual = validate_category("Срочная Служба")
            assert actual == 2

        def test_validate_category_missing(self):
            actual = validate_category("")
            assert actual is None

        def test_validate_category_invalid(self):
            actual = validate_category("conscript")
            assert actual is None

    class TestMosCode:
        def test_validate_mos_code_with_letter(self):
            actual = validate_mos_code("'546372-А ")
            assert actual == "546372А"

        def test_validate_mos_code_without_letter(self):
            actual = validate_mos_code(" 546372'")
            assert actual == "546372"

        def test_validate_mos_code_invalid_letters(self):
            actual = validate_mos_code("546372-ТЕСТ")
            assert actual is None

        def test_validate_mos_code_missing(self):
            actual = validate_mos_code("")
            assert actual is None

        def test_validate_mos_code_unsufficient_length(self):
            actual = validate_mos_code("12345-А")
            assert actual is None

        def test_validate_mos_code_invalid_sequence(self):
            actual = validate_mos_code("111111-А")
            assert actual is None

    class TestTagNumber:
        def test_validate_tag_number(self):
            actual = validate_tag_number("'АЯ - 102938 ")
            assert actual == "АЯ102938"

        def test_validate_tag_number_unsufficient_length(self):
            actual = validate_tag_number("АЯ-102")
            assert actual is None

        def test_validate_tag_number_invalid_sequence(self):
            actual = validate_tag_number("БВ-000000")
            assert actual is None

        def test_validate_tag_number_invalid_letters(self):
            actual = validate_tag_number("АБС-102938")
            assert actual is None

        def test_validate_tag_number_missing(self):
            actual = validate_tag_number("")
            assert actual is None

    class TestUnitCode:
        def test_validate_unit_code(self):
            actual = validate_unit_code(" В/Ч `10293-А`.")
            assert actual == "10293 А"

        def test_validate_unit_code_5_d3(self):
            actual = validate_unit_code("10293-312")
            assert actual == "10293 312"

        def test_validate_unit_code_5_l2(self):
            actual = validate_unit_code("10293-Ан")
            assert actual == "10293 АН"

        def test_validate_unit_code_4(self):
            actual = validate_unit_code("1029")
            assert actual == "1029"

        def test_validate_unit_code_unsufficient_length(self):
            actual = validate_unit_code("102")
            assert actual is None

        def test_validate_unit_code_invalid_sequence(self):
            actual = validate_unit_code("00000-А")
            assert actual is None

        def test_validate_unit_code_invalid_suffix(self):
            actual = validate_unit_code("10293-А1")
            assert actual is None

        def test_validate_unit_code_invalid_letters(self):
            actual = validate_unit_code("102938-АБС")
            assert actual is None

        def test_validate_unit_code_missing(self):
            actual = validate_unit_code("")
            assert actual is None

    class TestUnitName:
        def test_base_validation_name(self):
            actual = base_validation(" -.Unit Name- .-. .")
            assert actual == "Unit Name"

        def test_base_validation_shorten(self):
            actual = base_validation("Unit N.")
            assert actual == "Unit N."

        def test_base_validation_invalid_sequence(self):
            actual = base_validation("Aaaa")
            assert actual is None

        def test_base_validation_missing(self):
            actual = base_validation("")
            assert actual is None

/**
 * BigQuery Source Declarations for Dataform Complex Pipelines
 */

declare({
  database: "medallion-project-512608",
  schema: "bronze",
  name: "raw_index_0020",
  description: "Bronze raw passenger rail tickets and transport itineraries"
});

declare({
  database: "medallion-project-512608",
  schema: "bronze",
  name: "raw_index_0500",
  description: "Bronze raw traffic police vehicle registrations and owner identities"
});

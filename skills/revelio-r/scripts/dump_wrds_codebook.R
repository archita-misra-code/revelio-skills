# Dump a fresh Revelio WRDS codebook from information_schema.
#
# Credentials are read from WRDS_USERNAME and WRDS_PASSWORD.

source("wrds_connection_template.R")

dump_wrds_codebook <- function(
  output = "revelio_wrds_codebook.csv",
  schemas = c(
    "revelio",
    "revelio_common",
    "revelio_individual",
    "revelio_job_postings",
    "revelio_layoffs",
    "revelio_sentiment",
    "revelio_workforce_dynamics"
  )
) {
  con <- get_wrds_connection()
  on.exit(DBI::dbDisconnect(con), add = TRUE)

  sql <- "
    SELECT
      table_schema,
      table_name,
      column_name,
      data_type,
      character_maximum_length,
      numeric_precision,
      numeric_scale,
      ordinal_position
    FROM information_schema.columns
    WHERE table_schema = ANY($1)
    ORDER BY table_schema, table_name, ordinal_position
  "

  codebook <- DBI::dbGetQuery(con, sql, params = list(schemas))
  readr::write_csv(codebook, output)
  invisible(codebook)
}

if (sys.nframe() == 0) {
  dump_wrds_codebook()
}


# Safe WRDS connection template for Revelio Labs queries.
#
# Credentials are read from environment variables:
#   WRDS_USERNAME
#   WRDS_PASSWORD

library(DBI)
library(RPostgres)

get_wrds_connection <- function() {
  username <- Sys.getenv("WRDS_USERNAME")
  password <- Sys.getenv("WRDS_PASSWORD")

  if (identical(username, "") || identical(password, "")) {
    stop("Set WRDS_USERNAME and WRDS_PASSWORD environment variables before connecting.")
  }

  dbConnect(
    RPostgres::Postgres(),
    host = "wrds-pgdata.wharton.upenn.edu",
    port = 9737,
    dbname = "wrds",
    sslmode = "require",
    user = username,
    password = password
  )
}

example_query <- function(limit = 10) {
  con <- get_wrds_connection()
  on.exit(dbDisconnect(con), add = TRUE)

  dbGetQuery(
    con,
    paste0(
      "SELECT user_id, user_country, highest_degree, updated_dt ",
      "FROM revelio.individual_user ",
      "WHERE user_country = $1 ",
      "LIMIT $2"
    ),
    params = list("Morocco", limit)
  )
}


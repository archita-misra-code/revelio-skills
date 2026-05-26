# Small helpers for loading local Revelio extracts in R.

load_revelio_table <- function(path) {
  ext <- tolower(tools::file_ext(path))

  if (ext == "csv") {
    return(readr::read_csv(path, show_col_types = FALSE))
  }
  if (ext %in% c("xlsx", "xls")) {
    return(readxl::read_excel(path))
  }
  if (ext == "rds") {
    return(readRDS(path))
  }
  if (ext == "parquet") {
    return(arrow::read_parquet(path))
  }

  stop("Unsupported file type: ", ext)
}

parse_revelio_dates <- function(df) {
  date_cols <- intersect(c("startdate", "enddate", "updated_dt"), names(df))
  dplyr::mutate(df, dplyr::across(dplyr::all_of(date_cols), lubridate::ymd))
}

assert_required_columns <- function(df, columns) {
  missing <- setdiff(columns, names(df))
  if (length(missing) > 0) {
    stop("Missing required columns: ", paste(missing, collapse = ", "))
  }
  invisible(TRUE)
}


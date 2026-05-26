"""Dump a fresh Revelio WRDS codebook from information_schema.

Credentials are read from WRDS_USERNAME and WRDS_PASSWORD.
The output is a CSV with schema, table, column, type, and ordinal position.
"""

from __future__ import annotations

import argparse

import pandas as pd
from sqlalchemy import text

from wrds_connection_template import get_wrds_engine


DEFAULT_SCHEMAS = (
    "revelio",
    "revelio_common",
    "revelio_individual",
    "revelio_job_postings",
    "revelio_layoffs",
    "revelio_sentiment",
    "revelio_workforce_dynamics",
)


def dump_codebook(output: str, schemas: tuple[str, ...] = DEFAULT_SCHEMAS) -> None:
    engine = get_wrds_engine()
    query = text(
        """
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
        WHERE table_schema = ANY(:schemas)
        ORDER BY table_schema, table_name, ordinal_position
        """
    )
    with engine.connect() as conn:
        df = pd.read_sql_query(query, conn, params={"schemas": list(schemas)})
    df.to_csv(output, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="revelio_wrds_codebook.csv")
    parser.add_argument("--schemas", nargs="*", default=list(DEFAULT_SCHEMAS))
    args = parser.parse_args()
    dump_codebook(args.output, tuple(args.schemas))


"""Safe WRDS connection template for Revelio Labs queries.

Credentials are read from environment variables:
    WRDS_USERNAME
    WRDS_PASSWORD
"""

from __future__ import annotations

import os

from sqlalchemy import create_engine, text


def get_wrds_engine():
    username = os.environ.get("WRDS_USERNAME")
    password = os.environ.get("WRDS_PASSWORD")

    if not username or not password:
        raise RuntimeError(
            "Set WRDS_USERNAME and WRDS_PASSWORD environment variables before connecting."
        )

    url = (
        "postgresql+psycopg2://"
        f"{username}:{password}"
        "@wrds-pgdata.wharton.upenn.edu:9737/wrds?sslmode=require"
    )
    return create_engine(url)


def example_query(limit: int = 10):
    engine = get_wrds_engine()
    query = text(
        """
        SELECT user_id, user_country, highest_degree, updated_dt
        FROM revelio.individual_user
        WHERE user_country = :country
        LIMIT :limit
        """
    )
    with engine.connect() as conn:
        return conn.execute(query, {"country": "Morocco", "limit": limit}).fetchall()


if __name__ == "__main__":
    rows = example_query()
    print(f"Fetched {len(rows)} rows.")


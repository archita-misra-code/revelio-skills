"""Small helpers for loading local Revelio extracts in Python."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_table(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    suffix = path.suffix.lower()

    if suffix == ".parquet":
        return pd.read_parquet(path)
    if suffix in {".pkl", ".pickle"}:
        return pd.read_pickle(path)
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path)

    raise ValueError(f"Unsupported file type: {path.suffix}")


def parse_revelio_dates(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in ["startdate", "enddate", "updated_dt"]:
        if col in out.columns:
            out[col] = pd.to_datetime(out[col], errors="coerce")
    return out


def assert_required_columns(df: pd.DataFrame, columns: list[str]) -> None:
    missing = sorted(set(columns) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


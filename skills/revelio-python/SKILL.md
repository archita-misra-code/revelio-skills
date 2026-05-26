---
name: revelio-python
description: Use when working with Revelio Labs data in Python: WRDS/Postgres access, schema-aware extraction, pandas cleaning, career-history panels, skills/roles analysis, safe credential handling, and publication-ready Morocco/Growth Lab style outputs. Trigger for Python notebooks, scripts, or analyses involving Revelio tables such as individual_user, individual_positions, individual_user_education, individual_user_skills, role lookup, or skill lookup.
---

# Revelio Python

## Safety First

- Never hardcode WRDS usernames, passwords, tokens, or private local paths.
- Read credentials from `WRDS_USERNAME` and `WRDS_PASSWORD`.
- Never export or commit raw licensed data, profile names, LinkedIn URLs, or person-level extracts.
- Report the analysis boundary: Revelio captures LinkedIn-visible, formal, high-skill labor-market activity, not population migration or employment totals.

## Quick Start

Use `scripts/wrds_connection_template.py` for WRDS connections and `scripts/load_revelio_extracts.py` for local extract loading patterns. Read `references/schema.md` when selecting columns or joining tables.

Preferred Python stack:

```python
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
```

## WRDS Query Pattern

1. Select only needed columns and rows.
2. Filter on geography/time/employer in SQL when possible.
3. Keep joins explicit on stable identifiers:
   - `user_id` for person-level joins
   - `rcid` / `ultimate_parent_rcid` for employer joins
   - `rsid` for education institution joins
4. Save only derived, share-safe aggregate outputs unless a secure project workspace requires row-level extracts.

## Cleaning Principles

- Parse dates with `pd.to_datetime(..., errors="coerce")`.
- Preserve missingness indicators before filtering.
- Deduplicate using stable keys such as `user_id`, `position_id`, and spell dates.
- For career histories, sort by `user_id`, `startdate`, `enddate`, and `position_number`.
- Treat overlapping jobs explicitly; do not silently impose one job per person-month.
- For skills, keep both reported/predicted provenance (`skill_source`) and mapped/raw skill fields.

## Analysis Standards

- Always report sample size, date coverage, and missing data patterns.
- Prefer effect sizes and confidence intervals over p-values alone.
- Avoid causal language unless the design supports it.
- For plots, use clean labels, no unnecessary borders, no gridlines unless they carry information, and save at 300 DPI for publication use.

## Common Revelio Tables

- `revelio.individual_user`
- `revelio.individual_positions`
- `revelio.individual_user_education`
- `revelio.individual_user_skills`
- `revelio.company_mapping`
- `revelio.individual_role_lookup`
- `revelio.individual_user_skill_lookup`


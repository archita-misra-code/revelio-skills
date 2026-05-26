---
name: revelio-r
description: Use when working with Revelio Labs data in R: WRDS/Postgres access, dbplyr queries, tidyverse cleaning, career-history panels, skills/roles analysis, safe credential handling, and publication-ready Morocco/Growth Lab style figures or tables. Trigger for R scripts, Quarto, or analyses involving Revelio tables such as individual_user, individual_positions, individual_user_education, individual_user_skills, role lookup, or skill lookup.
---

# Revelio R

## Safety First

- Never hardcode WRDS usernames, passwords, tokens, or private local paths.
- Read credentials from `WRDS_USERNAME` and `WRDS_PASSWORD`.
- Never export or commit raw licensed data, profile names, LinkedIn URLs, or person-level extracts.
- Report the analysis boundary: Revelio captures LinkedIn-visible, formal, high-skill labor-market activity, not population migration or employment totals.

## Quick Start

Use `scripts/wrds_connection_template.R` for WRDS connections and `scripts/load_revelio_extracts.R` for local extract loading patterns. Read `references/schema.md` when selecting columns or joining tables. Read `references/products.md` when choosing among Individual, Job Postings, Sentiment, Layoffs, or Workforce Dynamics products. Read `references/wrds_access.md` for WRDS Postgres schema/view conventions and raw-text table access.

Preferred R stack:

```r
library(DBI)
library(RPostgres)
library(dplyr)
library(dbplyr)
library(readr)
library(lubridate)
library(ggplot2)
```

## WRDS Query Pattern

1. Select only needed columns and rows.
2. Filter on geography/time/employer in SQL or `dbplyr` before collecting.
3. Keep joins explicit on stable identifiers:
   - `user_id` for person-level joins
   - `rcid` / `ultimate_parent_rcid` for employer joins
   - `rsid` for education institution joins
4. Call `collect()` only after narrowing to a manageable extract.

## Cleaning Principles

- Parse dates with `lubridate::ymd()`.
- Preserve missingness indicators before filtering.
- Deduplicate using stable keys such as `user_id`, `position_id`, and spell dates.
- For career histories, arrange by `user_id`, `startdate`, `enddate`, and `position_number`.
- Treat overlapping jobs explicitly; do not silently impose one job per person-month.
- For skills, keep both reported/predicted provenance (`skill_source`) and raw/translated/mapped fields. As of the April 2026 taxonomy update, use `skill_k35000` as the most granular mapped skill field and join to `individual_user_skill_lookup` on `skill_k35000`.

## Analysis Standards

- Always report sample size, date coverage, and missing data patterns.
- Prefer effect sizes and confidence intervals over p-values alone.
- Avoid causal language unless the design supports it.
- For plots, use clean labels, no unnecessary borders, no default gray grid when preparing publication figures, and save at 300 DPI.

## Common Revelio Tables

- `revelio.individual_user`
- `revelio.individual_positions`
- `revelio.individual_user_education`
- `revelio.individual_user_skills`
- `revelio.company_mapping`
- `revelio.individual_role_lookup_v3`
- `revelio.individual_user_skill_lookup`
- `revelio.postings_cosmos`
- `revelio.sentiment_individual_reviews`
- `revelio.sentiment_scores`
- `revelio.workforce_dynamics_geo`
- `revelio.layoffs`

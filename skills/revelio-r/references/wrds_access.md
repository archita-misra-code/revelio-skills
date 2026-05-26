# WRDS Postgres Access Notes

WRDS exposes data through PostgreSQL schemas. There are two relevant schema patterns:

- Base table schemas: product-specific schemas that contain physical tables.
- Friendly alias schemas: shorter view schemas, often matching the SAS library name.

For Revelio, WRDS query pages commonly show:

- Product schema examples: `revelio_individual`, `revelio_job_postings`, `revelio_sentiment`, `revelio_workforce_dynamics`, `revelio_layoffs`, `revelio_common`.
- Friendly alias/library: `revelio`.

In code, prefer the schema/table name confirmed by the user's WRDS account. If a query fails under `revelio.<table>`, inspect accessible schemas/tables with `information_schema`.

## Discovery Queries

List accessible schemas:

```sql
SELECT schema_name
FROM information_schema.schemata
ORDER BY schema_name;
```

Find where a table exists:

```sql
SELECT table_name, table_schema, table_type
FROM information_schema.tables
WHERE table_name = 'postings_cosmos';
```

List columns:

```sql
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'revelio_job_postings'
  AND table_name = 'postings_cosmos_raw'
ORDER BY ordinal_position;
```

## Raw Text Tables

Raw text tables can be huge and are often Postgres-only. Filter before joining or collecting.

Examples:

- `individual_user_raw`
- `individual_positions_raw`
- `individual_user_education_raw`
- `postings_cosmos_raw`

For job postings raw descriptions:

```sql
SELECT p.job_id, p.company, p.country, p.post_date, r.title_raw, r.description
FROM revelio_job_postings.postings_cosmos AS p
JOIN revelio_job_postings.postings_cosmos_raw AS r
  ON p.job_id = r.job_id
WHERE p.country = 'Morocco'
  AND p.post_date >= DATE '2025-01-01'
LIMIT 100;
```

## Locating Individuals

To locate a person, you need `user_id`.

- If you know their company, start from `individual_positions`, filter by `rcid`, ticker/identifier via company mapping, seniority, role, dates, and geography.
- If you know their LinkedIn URL, start from `individual_user.profile_linkedin_url`. Use the form `linkedin.com/in/profile-url-slug` and normalize by removing `https://www.` and trailing `/`.

Do this only for secure internal QA or authorized validation work.


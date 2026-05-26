# Revelio Schema Notes

Core identifiers:

| Identifier | Meaning |
|---|---|
| `user_id` | Person/profile identifier |
| `position_id` | Position spell identifier |
| `rcid` | Employer identifier |
| `ultimate_parent_rcid` | Parent employer identifier |
| `rsid` | School identifier |
| `job_id` | Job posting identifier |
| `review_id` | Sentiment review identifier |

Core tables:

| Table | Grain | Common columns |
|---|---|---|
| `individual_user` | user | `user_id`, `user_country`, `highest_degree`, `sex_predicted`, `f_prob`, `m_prob`, `updated_dt` |
| `individual_user_raw` | user raw text | `user_id` plus raw profile text fields such as title/summary; use only when text analysis or manual QA requires it |
| `individual_positions` | job spell | `user_id`, `position_id`, `rcid`, `country`, `region`, `state`, `metro_area`, `city`, `startdate`, `enddate`, `role_k1500_v2`, `role_k17000_v3`, `onet_code`, `seniority`, `salary`, `position_number`, `company`, `ultimate_parent_company_name` |
| `individual_positions_raw` | position raw text | `user_id`, `position_id` plus raw position text such as descriptions; large table, Postgres preferred |
| `individual_user_education` | education spell | `user_id`, `rsid`, `university_name`, `university_country`, `degree`, `field`, `startdate`, `enddate` |
| `individual_user_education_raw` | education raw text | `user_id`, education spell identifiers, and raw education text fields; useful for spot-checking mapped school/degree/field |
| `individual_user_skills` | user-skill | `user_id`, `skill_raw`, `skill_translated`, `skill_source`, `first_reported`, `skill_k35000` |
| `company_mapping` | company/subsidiary | `rcid`, `company`, `ultimate_parent_rcid`, `ultimate_parent_company_name`, `naics_code`, `hq_country`, `hq_region`, `rics_k50`, `rics_k200`, `rics_k400` |
| `individual_role_lookup_v3` | role code | role clusters including `role_k17000_v3` and broader role categories |
| `individual_user_skill_lookup` | skill code | `skill_k35000` plus broader skill categories down to `skill_k15` |
| `postings_cosmos` | job posting | `job_id`, `company`, `country`, `post_date`, `remove_date`, `rcid`, `role_k1500_v2`, `role_k17000_v3`, `salary`, `salary_min`, `salary_max`, `salary_predicted`, source flags |
| `postings_cosmos_raw` | job posting raw text | `job_id`, `description`, `title_raw`, `jobtitle_translated`, `location_raw`; Postgres-only and very large |
| `postings_role_lookup_v3` | postings role code | `role_k17000_v3`, `role_k1500_v3`, `role_k150_v3`, `role_k50_v3`, `role_k10_v3`, `onet_code`, `onet_title` |
| `sentiment_individual_reviews` | review | `review_id`, `rcid`, `company`, `country`, `review_date`, ratings, raw review text fields |
| `sentiment_scores` | company score | `rcid`, `company`, topic sentiment scores, `num_reviews` |
| `workforce_dynamics_geo` | company-month geography | `rcid`, `country`, `state`, `metro_area`, `datemonth`, `seniority`, `role_k10`, count/inflow/outflow fields, salary, duration |
| `layoffs` | WARN notice | `rcid`, `company`, `state`, `city`, `layoff_date`, `notice_date`, `num_employees`, layoff type fields |

Taxonomy notes:

- April 2026 skills taxonomy: `skill_mapped` was replaced by `skill_k35000`, expanding from about 3,000 to more than 30,000 distinct skills.
- Join `individual_user_skills` to `individual_user_skill_lookup` on `skill_k35000` to map to broader skill categories up to `skill_k15`.
- Newer role fields use versioned names such as `role_k1500_v2` and `role_k17000_v3`; the most granular role category can be used to join to `individual_role_lookup_v3`.
- Fields containing `kN` are Revelio-created cluster categories; raw-text fields live in `_raw` tables and are much larger.
- Raw individual tables are callable directly by table name, e.g. `revelio.individual_user_education_raw`. Join raw education back to mapped education by `user_id` plus available education spell identifiers/date fields; check the WRDS table dictionary for exact columns before assuming a key.
- For COSMOS postings, join `postings_cosmos_raw` to `postings_cosmos` by `job_id`; filter the base table first because both tables are huge.

Sensitive fields and QA:

- `fullname`, `profile_linkedin_url`, and raw person-level location fields are legitimate for secure internal QA, manual spot-checking, and entity validation.
- Do not commit, publish, or externally share files containing those fields or row-level combinations that could identify individuals.
- Aggregate externally shared outputs to safe cell sizes.

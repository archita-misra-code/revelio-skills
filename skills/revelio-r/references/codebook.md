# Revelio WRDS Codebook Snapshot

This is the built-in variable reference for the major Revelio WRDS tables used by this skill. Revelio updates monthly; for a live exhaustive schema dump, run `scripts/dump_wrds_codebook.R` against WRDS.

## revelio_common.company_mapping

| Variable | Type | Description |
|---|---|---|
| `rcid` | Int | Revelio Labs Company ID |
| `company` | Char | Company name |
| `factset_entity_id` | Char | FactSet company ID |
| `year_founded` | Char | Year founded |
| `ticker` | Char | Ticker |
| `exchange_name` | Char | Stock exchange |
| `sedol` | Char | SEDOL |
| `isin` | Char | ISIN |
| `cusip` | Char | CUSIP |
| `url` | Char | Website URL |
| `naics_code` | Char | NAICS industry code |
| `cik` | Char | CIK |
| `lei` | Char | LEI |
| `linkedin_url` | Char | Company LinkedIn URL |
| `child_rcid` | Int | Largest subsidiary RCID |
| `child_company` | Char | Largest subsidiary name |
| `child_linkedin_url` | Char | LinkedIn URL of largest subsidiary |
| `ultimate_parent_rcid` | Int | Ultimate parent company RCID |
| `ultimate_parent_company_name` | Char | Ultimate parent company name |
| `gvkey` | Char | GVKEY |
| `ein` | Float | Employer Identification Number |
| `hq_street_address` | Char | Headquarters street address |
| `hq_zip_code` | Char | Headquarters ZIP code |
| `hq_city` | Char | Headquarters city |
| `hq_metro_area` | Char | Headquarters metro area |
| `hq_state` | Char | Headquarters state |
| `hq_country` | Char | Headquarters country |
| `hq_region` | Char | Headquarters region |
| `rics_k50` | Char | Revelio Industry Classification K=50 |
| `rics_k200` | Char | Revelio Industry Classification K=200 |
| `rics_k400` | Char | Revelio Industry Classification K=400 |
| `phone_number` | Char | Phone number |
| `slogan` | Char | Slogan |
| `description` | Char | Description |

## revelio_individual.individual_user

| Variable | Type | Description |
|---|---|---|
| `user_id` | Decimal | Revelio Labs user ID |
| `fullname` | Char | Full name |
| `f_prob` | Float | Female probability |
| `m_prob` | Float | Male probability |
| `white_prob` | Float | Non-Hispanic White probability |
| `black_prob` | Float | Black or African American probability |
| `api_prob` | Float | Asian/Pacific Islander probability |
| `hispanic_prob` | Float | Hispanic or Latino probability |
| `native_prob` | Float | American Indian or Alaskan Native probability |
| `multiple_prob` | Float | Multiracial probability |
| `prestige` | Float | Prestige |
| `highest_degree` | Char | Highest level of education |
| `sex_predicted` | Char | Predicted sex |
| `ethnicity_predicted` | Char | Predicted ethnicity |
| `profile_linkedin_url` | Char | Profile LinkedIn URL |
| `user_location` | Char | User location |
| `user_country` | Char | User country |
| `updated_dt` | Date | Date profile was last refreshed |
| `numconnections` | Int | Number of connections |

## revelio_individual.individual_positions

| Variable | Type | Description |
|---|---|---|
| `user_id` | Decimal | User ID |
| `position_id` | Decimal | Position ID |
| `country` | Char | Country |
| `region` | Char | Region |
| `state` | Char | State |
| `metro_area` | Char | Metropolitan area |
| `startdate` | Date | Position start date |
| `msa` | Char | Metropolitan Statistical Area |
| `enddate` | Date | Position end date |
| `city` | Char | City |
| `remote_suitability` | Float | Remote suitability proportion |
| `weight` | Float | Individual sample weight |
| `role_k1500_v2` | Char | Role category K=1500 version 2 |
| `start_salary` | Decimal | Salary at start date |
| `role_k17000_v3` | Char | Role category K=17000 version 3 |
| `end_salary` | Decimal | Salary at end date |
| `seniority` | Int | Seniority level |
| `salary` | Decimal | Predicted salary |
| `position_number` | Int | Position number |
| `total_compensation` | Decimal | Total compensation |
| `additional_compensation` | Decimal | Additional compensation |
| `onet_code` | Char | O*NET occupation code |
| `rcid` | Int | Revelio Labs Company ID |
| `ultimate_parent_rcid` | Int | Ultimate parent company RCID |
| `company` | Char | Company name |
| `ultimate_parent_company_name` | Char | Ultimate parent company name |
| `url` | Char | Company URL |
| `linkedin_url` | Char | Company LinkedIn URL |

## revelio_individual.individual_user_education

| Variable | Type | Description |
|---|---|---|
| `user_id` | Decimal | Revelio Labs user ID |
| `university_name` | Char | School name, mapped |
| `rsid` | Float | Revelio school ID |
| `education_number` | Float | Education number |
| `startdate` | Date | Start date |
| `enddate` | Date | End date |
| `degree` | Char | Degree title, mapped |
| `field` | Char | Degree field, mapped |
| `university_country` | Char | School country |
| `university_location` | Char | School location |

## revelio_individual.individual_user_education_raw

| Variable | Type | Description |
|---|---|---|
| `user_id` | Decimal | Revelio Labs user ID |
| `university_raw` | Char | Raw school name from profile |
| `education_number` | Float | Education sequence index; join to mapped education on `user_id` and `education_number` when available |
| `degree_raw` | Char | Raw degree text from profile |
| `field_raw` | Char | Raw field-of-study text from profile |
| `description` | Char | Free-text education/program description |

## revelio_individual.individual_user_skills

| Variable | Type | Description |
|---|---|---|
| `user_id` | Decimal | Revelio Labs user ID |
| `skill_raw` | Char | Skill, raw |
| `skill_translated` | Char | Skill, translated |
| `skill_source` | Char | Skill source, P=Predicted, R=Reported |
| `first_reported` | Date | Date skill was first reported |
| `skill_k35000` | Char | Skill category K=35000, mapped |

## revelio_individual.individual_user_skill_lookup

April 2026 taxonomy note: current WRDS skill hierarchy should be verified live. The new join key is `skill_k35000`, with broader categories up to `skill_k15`.

| Variable | Type | Description |
|---|---|---|
| `skill_k35000` | Char | Most granular mapped skill category |
| `skill_k15000` | Char | Broader skill category, if present |
| `skill_k5000` | Char | Broader skill category, if present |
| `skill_k1000` | Char | Broader skill category, if present |
| `skill_k500` | Char | Broader skill category, if present |
| `skill_k150` | Char | Broader skill category, if present |
| `skill_k50` | Char | Broader skill category, if present |
| `skill_k25` | Char | Broader skill category, if present |
| `skill_k15` | Char | Broadest skill category, if present |

Older schemas may instead expose `skill_mapped`, `skill_k25`, `skill_k50`, and `skill_k75`; verify before joining.

## revelio_individual.individual_role_lookup_v2 / individual_role_lookup_v3

Individual positions use versioned role columns such as `role_k1500_v2`, `role_k1500_v3`, and `role_k17000_v3`. Lookup table column names may omit the version suffix, so verify live column names before joining.

| Variable | Type | Description |
|---|---|---|
| `role_k1500` | Char | Fine role category / join key in older lookup layout |
| `role_k1000` | Char | Role category K=1000 |
| `role_k500` | Char | Role category K=500 |
| `role_k300` | Char | Role category K=300, if present |
| `role_k150` | Char | Role category K=150 |
| `role_k50` | Char | Role category K=50 |
| `job_category` | Char | High-level job category |
| `onet_code` | Char | O*NET occupation code |
| `onet_title` | Char | O*NET occupation title |

## revelio_common.school_mapping

| Variable | Type | Description |
|---|---|---|
| `rsid` | Int | Revelio school ID |
| `school_name` | Char | School/department name |
| `school_cleaned` | Char | Normalized school name |
| `ultimate_parent_rsid` | Int | Parent institution RSID |
| `ultimate_parent_school_name` | Char | Parent institution name |
| `country` | Char | School country |
| `state` | Char | State/province |
| `city` | Char | City |
| `metro_area` | Char | Metro area |
| `whed_id` | Char | WHED external ID |
| `factset_entity_id` | Char | FactSet ID |
| `website` | Char | School website |
| `region` | Char | Geographic region |
| `corresponding_rcid` | Decimal | Corresponding company RCID if school maps to a company entity |
| `corresponding_company_name` | Char | Corresponding company name |
| `whed_url` | Char | WHED URL |

## revelio_job_postings.postings_cosmos

| Variable | Type | Description |
|---|---|---|
| `job_id` | Int | Posting key |
| `company` | Text | Company name |
| `country` | Text | Country |
| `role_k1500_v2` | Text | Role category K=1500 version 2 |
| `state` | Text | State |
| `role_k17000_v3` | Text | Role category K=17000 version 3 |
| `metro_area` | Text | Metropolitan area |
| `onet_code` | Text | O*NET code |
| `salary` | Float | Salary |
| `salary_min` | Float | Salary minimum |
| `salary_max` | Float | Salary maximum |
| `salary_predicted` | Bool | Salary predicted flag |
| `post_date` | Date | Posting date |
| `remove_date` | Date | Removal date |
| `rcid` | Int | Revelio company ID |
| `ultimate_parent_rcid` | Int | Ultimate parent RCID |
| `ultimate_parent_company_name` | Text | Ultimate parent company name |
| `remote_type` | Text | Remote type |
| `expected_hires` | Float | Expected hires |
| `source_company_sites` | Bool | Source: company sites |
| `source_linkedin` | Bool | Source: LinkedIn |
| `source_indeed` | Bool | Source: Indeed |
| `source_zhaopin` | Bool | Source: Zhaopin |
| `source_51job` | Bool | Source: 51job |
| `source_liepin` | Bool | Source: Liepin |
| `source_other_aggregators` | Bool | Source: other aggregators |
| `source_staffingfirms` | Bool | Source: staffing firms |
| `source_regional_aggregators` | Bool | Source: regional aggregators |

## revelio_job_postings.postings_cosmos_raw

| Variable | Type | Description |
|---|---|---|
| `description` | Text | Job description |
| `job_id` | Decimal | Posting key |
| `jobtitle_translated` | Text | Translated job title |
| `location_raw` | Text | Raw location |
| `title_raw` | Text | Raw title |

## revelio_job_postings.postings_role_lookup_v3

| Variable | Type | Description |
|---|---|---|
| `onet_code` | Text | O*NET code |
| `onet_title` | Text | O*NET title |
| `role_k10000_v3` | Text | Role category K=10000 version 3 |
| `role_k1000_v3` | Text | Role category K=1000 version 3 |
| `role_k10_v3` | Text | Role category K=10 version 3 |
| `role_k1500_v3` | Text | Role category K=1500 version 3 |
| `role_k150_v3` | Text | Role category K=150 version 3 |
| `role_k17000_v3` | Text | Role category K=17000 version 3 |
| `role_k5000_v3` | Text | Role category K=5000 version 3 |
| `role_k500_v3` | Text | Role category K=500 version 3 |
| `role_k50_v3` | Text | Role category K=50 version 3 |

## revelio_layoffs.layoffs

| Variable | Type | Description |
|---|---|---|
| `rcid` | Decimal | Revelio Labs company ID |
| `company_raw` | Char | Raw company name |
| `company` | Char | Company name |
| `ultimate_parent_rcid` | Decimal | Ultimate parent company RCID |
| `state_raw` | Char | Raw state |
| `ultimate_parent_company_name` | Char | Ultimate parent company name |
| `state` | Char | State |
| `city_raw` | Char | Raw city |
| `city` | Char | City |
| `msa_raw` | Char | Raw MSA |
| `county_or_region_raw` | Char | Raw county or region |
| `layoff_date` | Date | Layoff date |
| `num_employees` | Int | Number of employees |
| `metro_area` | Char | Metro area |
| `notice_date` | Date | Notice date |
| `layoff_start_date` | Date | Layoff start date |
| `layoff_end_date` | Date | Layoff end date |
| `layoff_type` | Char | Layoff type |
| `num_employees_temporary` | Int | Number of temporary employees |
| `num_employees_furlough` | Int | Number of furloughed employees |

## revelio_sentiment.sentiment_individual_reviews

| Variable | Type | Description |
|---|---|---|
| `rcid` | Int | Revelio Labs company ID |
| `company_id` | Int | Glassdoor company ID |
| `company` | Char | Company name |
| `review_id` | Int | Review ID |
| `review_language_id` | Char | Review language |
| `location_raw` | Char | Raw location |
| `country` | Char | Country |
| `metro_area` | Char | Metro area |
| `state` | Char | State |
| `role_k17000` | Char | Role category K=17000 |
| `job_title_raw` | Char | Raw position title |
| `seniority` | Int | Seniority |
| `review_iscovid19` | Char | COVID-19 mentioned |
| `reviewer_employment_status` | Char | Employment type |
| `reviewer_job_ending_year` | Float | Final year of employment |
| `reviewer_length_of_employment` | Float | Years worked at company |
| `reviewer_current_job` | Char | Current employee |
| `rating_overall` | Float | Overall rating |
| `rating_business_outlook` | Char | Business outlook rating |
| `rating_career_opportunities` | Float | Career opportunities rating |
| `rating_ceo` | Char | CEO approval |
| `rating_compensation_and_benefits` | Float | Compensation and benefits rating |
| `rating_culture_and_values` | Float | Culture and values rating |
| `rating_diversity_and_inclusion` | Float | Diversity and inclusion rating |
| `rating_recommend_to_friend` | Char | Recommend-to-friend sentiment |
| `rating_senior_leadership` | Float | Senior management rating |
| `rating_work_life_balance` | Float | Work-life balance rating |
| `review_summary` | Char | Review title |
| `review_advice` | Char | Reviewer's advice to management |
| `review_pros` | Char | Reviewer's positive comments |
| `review_cons` | Char | Reviewer's negative comments |
| `review_count_helpful` | Int | Helpful count |
| `review_count_not_helpful` | Int | Unhelpful count |
| `ultimate_parent_rcid` | Int | Ultimate parent company RCID |
| `onet_code` | Char | O*NET occupation code |
| `ultimate_parent_company_name` | Char | Ultimate parent company name |
| `review_date` | Date | Review posting date |
| `review_time` | Time | Review posting time |

## revelio_sentiment.sentiment_scores

| Variable | Type | Description |
|---|---|---|
| `company` | Char | Company name |
| `management_sentiment` | Float | Management sentiment score |
| `innovative_technology_sentiment` | Float | Innovative technology sentiment score |
| `work_life_balance_sentiment` | Float | Work-life balance sentiment score |
| `mentorship_sentiment` | Float | Mentorship sentiment score |
| `career_advancement_sentiment` | Float | Career advancement sentiment score |
| `div_and_inclusion_sentiment` | Float | Diversity and inclusion sentiment score |
| `coworkers_sentiment` | Float | Coworkers sentiment score |
| `compensation_sentiment` | Float | Compensation sentiment score |
| `culture_sentiment` | Float | Culture sentiment score |
| `co_and_division_size_sentiment` | Float | Company and division size sentiment score |
| `perks_and_benefits_sentiment` | Float | Perks and benefits sentiment score |
| `onboarding_sentiment` | Float | Onboarding sentiment score |
| `remote_work_sentiment` | Float | Remote work sentiment score |
| `num_reviews` | Int | Number of reviews factored into the scores |
| `rcid` | Int | Revelio Labs company ID |

## revelio_workforce_dynamics.workforce_dynamics_geo

| Variable | Type | Description |
|---|---|---|
| `rcid` | Int | Revelio Labs company ID |
| `country` | Char | Country |
| `state` | Char | State |
| `metro_area` | Char | Metropolitan area |
| `seniority` | Int | Predicted seniority |
| `role_k10` | Char | Role category K=10 |
| `count` | Float | Number of employees |
| `inflow` | Float | Total inflow |
| `outflow` | Float | Total outflow |
| `external_inflow` | Float | External inflows |
| `raw_count` | Int | Unadjusted count |
| `external_outflow` | Float | External outflows |
| `raw_inflow` | Int | Unadjusted inflows |
| `raw_outflow` | Int | Unadjusted outflows |
| `scaled_count` | Float | Adjusted count |
| `scaled_inflow` | Float | Adjusted inflows |
| `scaled_outflow` | Float | Adjusted outflows |
| `scaled_external_inflow` | Float | Scaled external inflows |
| `scaled_external_outflow` | Float | Scaled external outflows |
| `salary` | Decimal | Predicted salary |
| `duration` | Float | Employee tenure |
| `remote_suitability` | Float | Remote suitability proportion |
| `datemonth` | Date | Year and month |
| `raw_external_inflow` | Int | Raw external inflows |
| `raw_external_outflow` | Int | Raw external outflows |

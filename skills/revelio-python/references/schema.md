# Revelio Schema Notes

Core identifiers:

| Identifier | Meaning |
|---|---|
| `user_id` | Person/profile identifier |
| `position_id` | Position spell identifier |
| `rcid` | Employer identifier |
| `ultimate_parent_rcid` | Parent employer identifier |
| `rsid` | School identifier |

Core tables:

| Table | Grain | Common columns |
|---|---|---|
| `individual_user` | user | `user_id`, `user_country`, `highest_degree`, `sex_predicted`, `f_prob`, `m_prob`, `updated_dt` |
| `individual_positions` | job spell | `user_id`, `position_id`, `rcid`, `country`, `startdate`, `enddate`, `role_k1500`, `seniority`, `salary`, `position_number` |
| `individual_user_education` | education spell | `user_id`, `rsid`, `university_name`, `university_country`, `degree`, `field`, `startdate`, `enddate` |
| `individual_user_skills` | user-skill | `user_id`, `skill_raw`, `skill_mapped`, `skill_source` |
| `company_mapping` | company/subsidiary | `rcid`, `company`, `ultimate_parent_rcid`, `ultimate_parent_company_name`, `naics_code`, `hq_country`, `rics_k50` |
| `individual_role_lookup` | role code | `role_k1500`, `role_k150`, `role_k50`, `job_category`, `onet_code`, `onet_title` |
| `individual_user_skill_lookup` | skill code | `skill_mapped`, `skill_k25`, `skill_k50`, `skill_k75` |

Sensitive fields:

- Avoid exporting `fullname`, `profile_linkedin_url`, raw person-level locations, or row-level combinations that could identify individuals.
- Aggregate externally shared outputs to safe cell sizes.


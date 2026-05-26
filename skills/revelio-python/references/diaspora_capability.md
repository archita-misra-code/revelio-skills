# Diaspora and Capability Workflows

This workflow is country-neutral. It was developed from Morocco work, but `HOME_COUNTRY` should be replaced with the study country or origin group. Morocco examples are illustrative only.

## Core Boundary

Revelio has no nationality field. Diaspora, origin, and return must be inferred from observed career and education histories. Treat the result as an observed, LinkedIn-visible professional segment, not a population migration estimate.

Use language like:

```text
observed HOME_COUNTRY-connected professional profiles
observed abroad spell
returnee in observed career history
LinkedIn-visible diaspora segment
```

Avoid language like:

```text
national diaspora rate
emigration rate
all migrants from HOME_COUNTRY
population return migration
```

## Origin and Connection Signals

Signal hierarchy:

| Signal | Source | Use | Concrete risk |
|---|---|---|---|
| Job spell in HOME_COUNTRY | `individual_positions.country` | Strongest labor-market connection | A foreign national may have worked in HOME_COUNTRY for a multinational and later left; that person is not necessarily part of the origin-country diaspora. |
| Education in HOME_COUNTRY | `individual_user_education.university_country` | Recovers people who studied in HOME_COUNTRY but left before working there | International students can be misclassified as origin-connected if they studied in HOME_COUNTRY but were never from there. |
| Profile location | `individual_user.user_country` | Useful for current/most-recent location checks | Profile country can be stale, vague, or reflect where someone lives while working remotely for an employer elsewhere. It should not define origin by itself. |

Decision checkpoint:

- Jobs only: cleaner evidence of labor-market connection, but misses people who leave before their first observed job.
- Jobs + education: broader origin connection, often better for capability/diaspora maps, but requires contamination checks.
- Profile location alone should not define origin.

## Country Normalization

Normalize country strings before matching:

```text
lowercase
trim whitespace
handle aliases and translated country names
```

Example `HOME_COUNTRY` aliases for Morocco:

```text
morocco
maroc
royaume du maroc
kingdom of morocco
```

Build a country-specific alias list rather than relying on one `LIKE` pattern.

## Diaspora Classification

Useful groups:

- `stayer`: HOME_COUNTRY-connected, no observed foreign spell.
- `one_way_emigrant`: HOME_COUNTRY-connected, observed HOME_COUNTRY -> abroad, no observed return.
- `returnee`: observed HOME_COUNTRY -> abroad -> HOME_COUNTRY sequence.
- `circular_mover`: two or more HOME_COUNTRY/abroad cycles.
- `current_or_recent_abroad`: latest observed job/profile location is abroad.

Core derived variables:

```text
ever_home_country
ever_abroad
first_home_country_date
first_abroad_date
last_observed_country
returnee
one_way_emigrant
circular_mover
years_abroad
destination_country
role_family_at_departure
role_family_at_return
seniority_change_on_return
```

## Current Location Decision

Compare latest observed position country to profile country:

| Pattern | What it may mean |
|---|---|
| profile abroad + last job abroad | Strongest current-abroad signal. The person both lists an abroad profile location and has an abroad latest job. |
| profile abroad + last job home | Could be a remote worker for a home-country employer, an old home-country job still listed as current, or a person who moved abroad without updating job history. Do not automatically count as diaspora without checking freshness and examples. |
| profile home + last job abroad | Could be a returnee whose profile location is current, a stale profile location, or an incomplete latest job record. This is a high-priority ambiguity for returnee analysis. |
| profile home + last job home | Clean domestic signal, assuming the profile was recently refreshed. |
| missing profile country or missing job country | Unknown location. Keep as unknown; do not silently assign to home or abroad. |

Use `updated_dt` to assess whether profile country is trustworthy.

## Edge Cases and What They Mean

- **Stale profile:** `updated_dt` is old, so the profile may reflect a job or location from years ago. This can make someone look like a current domestic worker or current diaspora member when they have since moved. Report stale share and test a freshness filter.
- **Remote worker ambiguity:** Job country and person location may differ because the person lives abroad but works for a home-country employer, or vice versa. This is not necessarily migration. Treat it as ambiguous unless the research question is explicitly about remote work.
- **Expat contamination:** A foreign professional who worked in HOME_COUNTRY can look origin-connected using job-spell rules. Cross-check education, career sequence, names only if ethically appropriate, and manual spot checks.
- **Foreign-student contamination:** A non-origin student educated in HOME_COUNTRY can look origin-connected using education rules. Inspect school/country patterns and decide whether education-only cases should be included.
- **Returnee vs current diaspora:** A person with an abroad spell who is now back in HOME_COUNTRY is not current diaspora, but is central for return/circulation analysis. Keep returnees as their own group.
- **Circular mover:** Multiple home-abroad cycles indicate circulation rather than one-way loss. These cases are analytically useful but can be misread if collapsed into simple emigrant/returnee categories.
- **Missing country:** Missing location is not home-country location. Keep unknowns explicit and report their share.
- **Short spell:** A one-month foreign position may be an internship, data artifact, or short assignment. Use minimum-tenure sensitivity before treating it as emigration.
- **Overlapping spells:** Concurrent jobs can look like a transition when they are actually simultaneous. Flag overlaps and avoid counting overlapping links as sequential moves.
- **Recent-period lag:** People update profiles slowly after moves. Avoid strong claims about the most recent months unless you account for update lag.
- **Small cells:** Highly specific role/skill/destination cells can identify people or produce unstable rates. Suppress or footnote small cells.

## Tenure and Timing

- Require a minimum tenure threshold for origin/destination evidence when short spells would distort interpretation; six months is a reasonable starting point, not a universal rule.
- Keep all dated spells in audit counts, but use thresholded spells for main diaspora/mobility classification when appropriate.
- Check coverage by year and choose an earliest reliable year before time-series claims.
- Avoid overinterpreting recent months because profile update lag can distort timing.

## Capability Measures

Capability can be proxied by:

- Role family or role code.
- Skill category, after validating current skill taxonomy.
- Sector/industry via company mapping.
- Seniority level.
- Prestige, cautiously.
- Education institution/field, if coverage is sufficient.

Main summaries:

- Domestic vs diaspora role composition.
- Domestic vs diaspora skill RCA/enrichment.
- Diaspora share within each role/skill/sector cell.
- Return probability by role/skill/sector/destination.
- Returnee vs non-returning diaspora composition.
- First employer/sector/role after return.

## RCA and Enrichment

Use RCA to describe relative concentration, not population totals:

```text
RCA(group, capability) =
  share of group in capability /
  share of reference population in capability
```

Useful contrasts:

- diaspora RCA vs domestic RCA
- returnee RCA vs non-returning diaspora RCA
- scarce-at-home but dense-abroad capabilities

Always report denominator and suppress/flag small cells.

## University Pipeline

For university-to-diaspora pathways:

- Use `rsid` and `school_mapping` where possible, not only raw school text.
- Use `individual_user_education_raw` for QA and finer field/degree text.
- Report education coverage before claiming pipeline patterns.
- Separate home-country universities, foreign universities, and unknown school country.

## Bias and Limitations

Diaspora analysis has stronger selection bias than ordinary domestic Revelio work:

- emigrants on LinkedIn are disproportionately high-skill and formal-sector
- informal and lower-skill migrants are undercovered
- profile location can be stale
- foreign students and expatriates can contaminate origin definitions
- remote jobs can confuse person location and job location

State these limits in every diaspora/capability output.

## Analysis Checkpoints

Before finalizing:

- Origin signal counts: jobs in HOME_COUNTRY, education in HOME_COUNTRY, overlap, incremental gain.
- Expat-risk and foreign-student-risk sample inspection.
- Profile freshness distribution for `updated_dt`.
- Latest job country vs profile country cross-tab.
- Stayer/one-way/returnee/circular counts.
- Destination country distribution with small-cell rules.
- Capability coverage: roles, skills, sectors, education.
- Robustness to origin definition and recency/tenure thresholds.


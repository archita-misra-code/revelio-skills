# Diaspora and Capability Workflows

This reference captures reusable workflow memory from the Morocco Revelio diaspora/capability work. It is intentionally methodological, not project-private.

## Core Boundary

Revelio has no nationality field. Diaspora and origin must be inferred from observed career and education histories, not asserted as population migration.

Use language like:

```text
observed Morocco-connected professional profiles
observed abroad spell
returnee in observed career history
LinkedIn-visible diaspora segment
```

Avoid language like:

```text
national diaspora rate
emigration rate
all Moroccan migrants
population return migration
```

## Origin and Connection Signals

Signal hierarchy:

| Signal | Source | Use | Main risk |
|---|---|---|---|
| Job spell in Morocco | `individual_positions.country` | Strongest Morocco connection | Expat foreign nationals working in Morocco |
| Education in Morocco | `individual_user_education.university_country` | Recover pre-labor-market leavers | Foreign students |
| Profile location | `individual_user.user_country` | Current/most recent profile location only | Stale or remote profiles |

Decision checkpoint:

- Jobs only: cleaner labor-market connection, misses students who leave before working.
- Jobs + education: broader Morocco connection, recommended for capability/diaspora maps if contamination is inspected.
- Profile location alone should not define origin.

## Country Normalization

Normalize before matching:

```text
lowercase
trim whitespace
handle aliases
```

Known Morocco variants:

```text
morocco
maroc
royaume du maroc
kingdom of morocco
```

Build a country-specific variant list rather than relying on one `LIKE` pattern.

## Diaspora Classification

Useful groups:

- `stayer`: Morocco-connected, no observed foreign spell.
- `one_way_emigrant`: Morocco-connected, observed Morocco -> abroad, no observed return.
- `returnee`: observed Morocco -> abroad -> Morocco sequence.
- `circular_mover`: two or more Morocco/abroad cycles.
- `current_or_recent_abroad`: latest observed job/profile location is abroad.

Core derived variables:

```text
ever_morocco
ever_abroad
first_morocco_date
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

| Pattern | Interpretation |
|---|---|
| profile abroad + last job abroad | clean current-abroad signal |
| profile abroad + last job Morocco | possible remote worker, stale job, or profile-location ambiguity |
| profile Morocco + last job abroad | possible returnee, stale profile, or incomplete latest job |
| profile Morocco + last job Morocco | clean domestic signal |

Use `updated_dt` to assess whether profile country is trustworthy.

## Tenure and Timing

- Require a minimum tenure threshold for origin/destination evidence when needed; six months is a common starting point.
- Keep all dated spells in audit counts, but use thresholded spells for main diaspora/mobility classification when short spells would distort interpretation.
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
- Separate Moroccan universities, foreign universities, and unknown school country.

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

- Origin signal counts: jobs-in-Morocco, education-in-Morocco, overlap, incremental gain.
- Expat-risk and foreign-student-risk sample inspection.
- Profile freshness distribution for `updated_dt`.
- Latest job country vs profile country cross-tab.
- Stayer/one-way/returnee/circular counts.
- Destination country distribution with small-cell rules.
- Capability coverage: roles, skills, sectors, education.
- Robustness to origin definition and recency/tenure thresholds.


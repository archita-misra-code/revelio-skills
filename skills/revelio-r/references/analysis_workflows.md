# Revelio Analysis Workflows and Checkpoints

This reference captures reusable institutional practice from the Morocco Revelio work. Use it before generating cleaning notebooks, mobility panels, geography variables, transition tables, or report-ready outputs.

## Interpretation Boundary

Always state the boundary:

- Revelio/LinkedIn captures formal, online-visible, high-skill labor-market activity.
- It supports relative comparisons in capability composition and observed mobility.
- It does not estimate national migration rates, unemployment, FLFP, informal employment, or population aggregates.

## Progressive Analysis Pattern

Build analyses in checkpoints:

1. Sample definition and extraction audit.
2. Quality filters and retention table.
3. Missingness and coverage diagnostics.
4. Descriptive distributions.
5. Relationship/mobility analysis.
6. Robustness/sensitivity checks.
7. Export only the plots/tables the user asks to preserve.

Each output should state unit, sample, time period, N, and relevant denominator.

## User/Profile Quality Filters

Baseline Morocco-style filters:

- Geographic filter: retain `user_country = 'Morocco'` for Morocco user samples.
- Connection filter: remove profiles with `numconnections == 0`.
- Recency filter: retain recently refreshed profiles, commonly a 24-month window using `updated_dt`.
- Organization/spam filter: remove implausible person accounts with extreme company/school counts or other organization-like patterns.
- Propagate the final quality-checked `user_id` set to positions, education, and skills.

Checkpoint outputs:

- Retention funnel by filter step.
- Before/after demographics: gender, prestige, education, geography.
- Dataset retention across users, positions, education, skills.
- Counts of stale profiles using `updated_dt` buckets.

Robustness:

- Compare no connection filter, `>=1`, `>=5`, and `>=10`.
- Compare no recency filter, 12-month, 24-month, and 36-month windows.
- Do not silently change the baseline; show robustness in appendix or sensitivity table.

## Missingness Rules

Report coverage before analysis. Do not hide missingness.

- Missing below 20%: create missing category/dummy as appropriate.
- Missing 20-50%: report coverage and analyze available cases with caution.
- Missing above 50%: use as diagnostic or appendix unless central to the question.
- `rcid` missingness: report company-ID coverage for position/employer analyses.
- Degree text can be sparse; prefer `rsid`/school fields when degree fields are weak.
- Skill analyses require taxonomy/schema validation first, especially after the `skill_k35000` update.

## Position/Spell Quality

Before mobility or tenure work:

- Parse `startdate` and `enddate`; document missing and implausible dates.
- Keep missing-start spells in extraction/audit counts, but exclude from tenure and transition calculations requiring dates.
- Treat zero-tenure spells as date-rounding artifacts unless the context proves otherwise.
- Keep short spells by default; flag `<30 days` as diagnostic rather than deleting.
- For current/ongoing spells, use censored tenure with a clearly stated censor date.

Optional high-quality position subset:

- Has `rcid`.
- Has role category.
- Has valid `startdate`.

Use this only when the estimand needs it, and report how much sample is lost.

## Transition Construction

Canonical pattern:

1. Sort spells by `user_id`, `startdate`, `enddate`, and `position_number`.
2. Use lead/lag within `user_id` to create prior/next employer, role, country, seniority, and dates.
3. Define transition denominators explicitly: all observed next jobs, external exits only, cross-company moves only, etc.
4. Exclude or flag overlapping transitions rather than pretending all overlaps are sequential.

Overlap rule:

- Same-RCID overlaps: resolve only high-confidence artifacts, such as same user, same RCID, detailed role/seniority, and overlap over 30 days.
- Retain other overlaps in spell-level data, but filter overlapping transition links when analyzing movement.
- Use an explicit field like `valid_next_transition_30d` for transition analyses.

Destination rules:

- Destination firm tables need both counts and denominator/rate columns.
- Use strict external exits for destination concentration.
- Check unknown destination share by exit year/cohort.
- Internal promotions or same-RCID moves should not be interpreted as external mobility.

## Geography Rules

Keep geography semantics sharp:

- Position geography is not company headquarters geography.
- Split known Morocco, abroad, and missing country; never count missing country as Morocco-located.
- For international flags, use position `country` unless the research question is specifically about firm HQ or parent ownership.
- Raw user location is useful for QA/geocoding, but outputs should rely on standardized country/state/metro fields when possible.

Common flags:

```text
is_morocco
is_abroad
country_missing
prior_abroad_before_event
next_spell_abroad_after_exit
```

## Employer and Parent Boundaries

- Report whether analysis uses `rcid`, `ultimate_parent_rcid`, or a hand-validated employer group.
- Parent links may reflect current ownership rather than historical ownership; flag parent-expansion sensitivity separately.
- For SOE/OCP/UM6P-style work, seed extraction from validated RCIDs and then pull complete observed career histories for those users.
- Cross-group workers should be flagged, not automatically dropped.

## Small Cells and Reporting

- Suppress or footnote cells with `N < 50` in public-facing outputs.
- Use generated tables/meta files for report numbers; do not hand-code unverified stats.
- Every plot/table title or caption should include N, denominator, and time/sample context.
- For role/skill composition, report coverage before comparing groups.

## Visualization and Table Standards

Figures:

- No bar borders.
- Legends outside the plot when practical.
- Avoid gridlines by default.
- Remove top/right spines.
- Save at 300 DPI with tight bounding box and white background.

Tables:

- Use counts plus shares/rates.
- Use clear denominators.
- Use booktabs LaTeX only when explicitly requested.

## Methods Text Template

Use and adapt:

```text
We analyze LinkedIn-derived public profile data from Revelio Labs. The sample
captures Morocco's formal, online-visible, high-skill labor market and should
not be interpreted as a population-level measure of employment or migration.
We apply profile-quality filters for public-profile freshness and account
quality, then report retention and missingness diagnostics before estimating
composition or mobility patterns.
```


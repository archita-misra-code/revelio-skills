# Revelio Skills

Reusable AI-agent skills for working with Revelio Labs career-history data in Python and R.

These skills are designed for external sharing. They contain workflow guidance, schema notes,
and safe code templates only. They do not include raw Revelio data, WRDS credentials, local
paths, private project outputs, or personal user details.

## Contents

- `skills/revelio-python/` - Python workflows for querying, cleaning, and analyzing Revelio data.
- `skills/revelio-r/` - R workflows for querying, cleaning, and analyzing Revelio data.

## Install

Copy one or both skill folders into your agent skills directory.

For Codex:

```bash
mkdir -p ~/.codex/skills
cp -R skills/revelio-python ~/.codex/skills/
cp -R skills/revelio-r ~/.codex/skills/
```

## Credential Safety

Never commit WRDS usernames, passwords, API keys, local `.Renviron` files, notebook outputs,
or extracted Revelio data.

Use environment variables instead:

```bash
export WRDS_USERNAME="your_wrds_username"
export WRDS_PASSWORD="your_wrds_password"
```

## Data Boundary

Revelio data is licensed data. This repository only provides reproducible workflow scaffolding.
Users are responsible for complying with their institution's data access and sharing rules.


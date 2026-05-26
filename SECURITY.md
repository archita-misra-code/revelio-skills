# Security Policy

This repository must never contain credentials, local private paths, or licensed Revelio data.

## Before Publishing

Run:

```bash
rg -n --hidden --glob '!.git/**' --glob '!SECURITY.md' \
  '(password|passwd|pwd|secret|token|api[_-]?key|WRDS_PASSWORD|BEGIN [A-Z ]*PRIVATE KEY)'
```

If available, also run:

```bash
gitleaks detect --no-git --source .
```

## Credential Pattern

Use environment variables:

- `WRDS_USERNAME`
- `WRDS_PASSWORD`

Do not hardcode credentials in R scripts, Python scripts, notebooks, Quarto files, or Markdown.


# migration-safety-check

**CLI Contract.** Review SQL migration notes for destructive operations and rollout gaps.

## Promise

Database migrations are high-risk even when small. This CLI catches destructive operations, missing transactions, and weak rollback notes.

## Accepted Files

`migration-safety-check` accepts SQL migration file or migration plan in text, JSON, JSONL, or CSV form.

## Exit Codes

```bash
python -m pip install -e ".[dev]"
migration-safety-check examples/sample.txt
migration-safety-check examples/sample.txt --json --fail-on medium
```

## Sample

| Rule | Severity | Meaning |
|---|---:|---|
| `drop-operation` | high | destructive migration operation detected |
| `missing-rollback` | medium | rollback plan is missing |
| `no-transaction` | low | transaction behavior is unclear |

## Development

```bash
ruff check .
pytest
python -m migration_safety_check --help
```

License: MIT

### Example Input

```text
ALTER TABLE users DROP COLUMN legacy_id; rollback missing; transaction none
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the migration-safety-check policy surface explicit.

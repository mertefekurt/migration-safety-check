# Migration Safety Check

Review SQL migration notes for destructive operations and rollout gaps.

## First impression

![Migration Safety Check cover](assets/readme-cover.svg)

When this tool reports something, I want the finding to be boringly explicit: what matched, how severe it is, and what a reviewer should clean up.

## Tripwires

- `drop-operation` (high): destructive migration operation detected. Fix: Use expand-contract rollout and verify backups before deploy..
- `missing-rollback` (medium): rollback plan is missing. Fix: Add rollback or recovery steps to the migration plan..
- `no-transaction` (low): transaction behavior is unclear. Fix: State whether the migration can run transactionally..

## Runbook

```bash
git clone https://github.com/mertefekurt/migration-safety-check.git
cd migration-safety-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Then:

```bash
migration-safety-check examples/sample.txt
migration-safety-check examples/sample.txt --json
```

## Development note

The policy lives in `rules.py`; parsing and rendering stay separate so the rule list is easy to audit.

from __future__ import annotations

from migration_safety_check.models import Rule

PROJECT_NAME = 'migration-safety-check'
SUMMARY = 'Review SQL migration notes for destructive operations and rollout gaps.'
SAMPLE_RISK = 'ALTER TABLE users DROP COLUMN legacy_id; rollback missing; transaction none'
SAMPLE_CLEAN = 'ADD COLUMN display_name nullable; backfill batched; rollback documented'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='drop-operation',
        severity='high',
        pattern='\\b(drop table|drop column|truncate)\\b',
        message='destructive migration operation detected',
        recommendation='Use expand-contract rollout and verify backups before deploy.',
    ),
    Rule(
        code='missing-rollback',
        severity='medium',
        pattern='\\brollback\\s*(missing|none|not planned)\\b',
        message='rollback plan is missing',
        recommendation='Add rollback or recovery steps to the migration plan.',
    ),
    Rule(
        code='no-transaction',
        severity='low',
        pattern='\\btransaction\\s*(none|disabled|missing)\\b',
        message='transaction behavior is unclear',
        recommendation='State whether the migration can run transactionally.',
    ),
)

# PR Review Checklist

## Issue alignment
- [ ] PR title references the issue number
- [ ] Scope matches issue description

## Code quality
- [ ] Tests pass: run `pytest -v`
- [ ] No hardcoded secrets
- [ ] Docstrings present and cite sources

## Data standards (JFE compliance)
- [ ] Output has clear column names
- [ ] No missing values in output CSVs
- [ ] Data dictionary updated if new variables added

## AI disclosure
- [ ] AI-generated code is noted in docstrings
- [ ] Human author reviewed and edited all AI output

## Verdict
- [ ] **Accept** — all checks pass
- [ ] **Revise** — note required changes below

## Notes
[Reviewer notes here]

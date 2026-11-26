# Documentation Quality Checker

A lightweight Markdown checker that helps catch common issues before editorial review.

## Checks
- Missing Markdown heading
- Placeholder terms: TODO, TBD, FIXME, and Lorem ipsum
- Broken relative/local Markdown links
- Prose lines above a configurable word threshold

## Run
```bash
python check_docs.py samples
python check_docs.py samples --max-words 25
```

## Test
```bash
python -m unittest -v
```

## Scope
This is a starter linter, not a full Markdown parser, accessibility audit, or editorial review. External URL availability is intentionally not checked to avoid unreliable network-dependent results.
# AI Release Notes Generator

A deterministic CLI tool that converts structured JSON product changes into grouped Markdown release notes. It does not require an LLM or API key and does not invent product behavior; a human reviewer approves the resulting draft.

## Run
```bash
python generate.py changes.json --output RELEASE_NOTES.md
```

## Test
```bash
python -m unittest -v
```

Input changes require `type`, `title`, and `description`. Supported types are feature, improvement, fix, security, and deprecated. Optional fields include audience and area.

## Responsible workflow
1. Start with approved engineering or release records.
2. Describe customer impact and audience.
3. Generate the draft.
4. Verify technical accuracy with Product and Engineering.
5. Publish only after human approval.
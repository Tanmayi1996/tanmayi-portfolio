# API Documentation Toolkit

A fictional REST API documentation package demonstrating an API-first workflow.

## Contents
- `specs/openapi.yaml` — OpenAPI 3.1 contract with endpoints, schemas, examples, and responses.
- `API_GUIDE.md` — human-readable endpoint guide and usage examples.
- `validate_spec.py` — lightweight structural checks using the Python standard library.

## Run
```bash
python validate_spec.py
```
The script checks for required OpenAPI markers; it is not a full OpenAPI parser. Use a dedicated OpenAPI 3.1 validator in production.

## Important
The API and its data are fictional. `api.example.com` is an example hostname and is not a live service.
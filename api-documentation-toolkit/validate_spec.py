"""Basic structural checks for the sample OpenAPI YAML contract."""
from pathlib import Path
import sys

REQUIRED = ["openapi: 3.1.0", "info:", "title:", "version:", "paths:", "components:"]

def validate(path):
    text = Path(path).read_text(encoding="utf-8")
    issues = [f"Missing required marker: {marker}" for marker in REQUIRED if marker not in text]
    if "https://api.example.com/v1" not in text:
        issues.append("Expected the sample server URL.")
    if "operationId:" not in text:
        issues.append("At least one operationId is required.")
    return issues

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "specs/openapi.yaml"
    problems = validate(target)
    if problems:
        print("\n".join(f"- {problem}" for problem in problems))
        raise SystemExit(1)
    print(f"Basic contract checks passed: {target}")
    print("For full conformance, use a dedicated OpenAPI 3.1 validator.")
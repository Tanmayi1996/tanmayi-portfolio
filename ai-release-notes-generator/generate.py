"""Generate consistent Markdown release notes from structured JSON."""
import argparse
import json
from datetime import date
from pathlib import Path

LABELS = {"feature":"New features","improvement":"Improvements","fix":"Bug fixes","security":"Security","deprecated":"Deprecations"}
ORDER = ["feature", "improvement", "fix", "security", "deprecated"]

def load_changes(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data.get("changes"), list):
        raise ValueError("Input must contain a 'changes' array.")
    for i, item in enumerate(data["changes"], 1):
        for field in ("type", "title", "description"):
            if not str(item.get(field, "")).strip():
                raise ValueError(f"Change #{i} is missing required field: {field}")
        if item["type"] not in LABELS:
            raise ValueError(f"Unsupported change type: {item['type']}")
    return data

def render(data):
    product = data.get("product", "Product")
    version = data.get("version", "Unversioned")
    release_date = data.get("release_date", date.today().isoformat())
    lines = [f"# {product} {version}", "", f"**Release date:** {release_date}", ""]
    for kind in ORDER:
        items = [c for c in data["changes"] if c["type"] == kind]
        if not items:
            continue
        lines += [f"## {LABELS[kind]}", ""]
        for item in items:
            audience = item.get("audience", "all")
            area = item.get("area")
            suffix = f" *({audience}; {area})*" if area else f" *({audience})*"
            lines.append(f"- **{item['title']}** — {item['description']}{suffix}")
        lines.append("")
    if not data["changes"]:
        lines += ["No customer-facing changes are included in this release.", ""]
    lines += ["---", "*Draft generated from structured change records. Review with Product and Engineering before publication.*"]
    return "\n".join(lines).strip() + "\n"

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="changes.json")
    parser.add_argument("-o", "--output", default="RELEASE_NOTES.md")
    args = parser.parse_args()
    data = load_changes(args.input)
    Path(args.output).write_text(render(data), encoding="utf-8")
    print(f"Release notes written to {args.output}")

if __name__ == "__main__":
    main()
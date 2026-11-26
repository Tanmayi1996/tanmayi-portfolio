"""Check Markdown files for common documentation quality issues."""
import argparse
import re
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+\S", re.M)
PLACEHOLDERS = ("TODO", "TBD", "FIXME", "Lorem ipsum")

def check_file(path, max_words=30):
    text = path.read_text(encoding="utf-8")
    issues = []
    if not HEADING_RE.search(text):
        issues.append((1, "No Markdown heading found."))
    for token in PLACEHOLDERS:
        for match in re.finditer(re.escape(token), text, re.I):
            line = text.count("\n", 0, match.start()) + 1
            issues.append((line, f"Placeholder text found: {token}"))
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = (path.parent / target.split("#", 1)[0]).resolve()
        if not target_path.exists():
            line = text.count("\n", 0, match.start()) + 1
            issues.append((line, f"Broken local link: {target}"))
    in_code = False
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or not line.strip() or line.lstrip().startswith("#"):
            continue
        words = re.findall(r"\b[\w'-]+\b", line)
        if len(words) > max_words and not line.lstrip().startswith(("-", "*", "|")):
            issues.append((line_no, f"Long line ({len(words)} words; recommended max {max_words})."))
    return issues

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default="samples")
    parser.add_argument("--max-words", type=int, default=30)
    args = parser.parse_args()
    target = Path(args.path)
    files = [target] if target.is_file() else sorted(target.rglob("*.md"))
    if not files:
        print("No Markdown files found.")
        return
    total = 0
    for file in files:
        issues = check_file(file, args.max_words)
        if issues:
            print(f"\n{file}:")
            for line, message in issues:
                print(f"  L{line}: {message}")
                total += 1
        else:
            print(f"PASS {file}")
    print(f"\nChecked {len(files)} file(s); found {total} issue(s).")
    raise SystemExit(1 if total else 0)

if __name__ == "__main__":
    main()
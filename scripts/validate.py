"""Validate the installable skill and its portable documentation (stdlib only)."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

REQUIRED = (
    "SKILL.md", "references/model-routing.md", "README.md", "AGENTS.md",
    "CODEX_PROGRESS.md", "CHANGELOG.md", "LICENSE", ".gitignore", "scripts/validate.py",
)


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")
    markdown = [p for p in root.rglob("*.md") if ".git" not in p.relative_to(root).parts]
    for path in markdown:
        label = path.relative_to(root).as_posix()
        try:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"{label}: cannot read UTF-8: {exc}")
            continue
        if raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"{label}: UTF-8 BOM is not allowed")
        if re.search(r"[A-Za-z]:[\\/]Users[\\/][^\s/\\]+", text):
            errors.append(f"{label}: device-specific user path")
        if path == root / "SKILL.md":
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
            if not match:
                errors.append("SKILL.md: missing opening frontmatter")
            else:
                fields = match.group(1)
                if not re.search(r"^name: team-development\s*$", fields, re.M):
                    errors.append("SKILL.md: name must be team-development")
                if not re.search(r"^description: \S[^\r\n]*$", fields, re.M):
                    errors.append("SKILL.md: missing single-line description")
        # Check actual inline local file links, excluding fenced code examples.
        prose = text
        prose = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", prose)
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", prose):
            target = target.strip().strip("<>")
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            resolved = (path.parent / unquote(parts.path)).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"{label}: local link escapes repository: {target}")
            elif not resolved.is_file():
                errors.append(f"{label}: broken local link: {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"Not a directory: {root}")
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("PASS: skill metadata, UTF-8, required files, portable paths and local links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

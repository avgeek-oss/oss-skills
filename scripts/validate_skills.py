"""Check portable skill metadata and the entry point's local Markdown links."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ALLOWED_FIELDS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)\)")


def validate_skill(directory: Path) -> list[str]:
    source = directory / "SKILL.md"
    if not source.is_file():
        return ["missing SKILL.md"]
    content = source.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", content, re.S)
    if not frontmatter:
        return ["expected YAML frontmatter followed by Markdown"]
    try:
        fields = yaml.safe_load(frontmatter[1])
    except yaml.YAMLError as error:
        return [f"invalid YAML: {error}"]
    if not isinstance(fields, dict):
        return ["frontmatter must be a mapping"]
    errors = []
    unknown = fields.keys() - ALLOWED_FIELDS
    if unknown:
        errors.append(f"unsupported metadata fields: {', '.join(map(str, unknown))}")
    name = fields.get("name")
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        errors.append("name must be 1–64 lowercase letters/digits with single hyphens")
    elif name != directory.name:
        errors.append("name must match its directory")
    description = fields.get("description")
    if (
        not isinstance(description, str)
        or not description.strip()
        or len(description) > 1024
    ):
        errors.append(
            "description must be a non-empty string of at most 1024 characters"
        )
    for field, limit in [
        ("compatibility", 500),
        ("license", None),
        ("allowed-tools", None),
    ]:
        if field in fields:
            value = fields[field]
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{field} must be a non-empty string")
            elif limit and len(value) > limit:
                errors.append(f"{field} must be at most {limit} characters")
    if "metadata" in fields:
        metadata = fields["metadata"]
        if not isinstance(metadata, dict) or not all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in metadata.items()
        ):
            errors.append("metadata must map strings to strings")
    body = frontmatter[2]
    if not body.strip():
        errors.append("instructions must not be empty")
    for target in LINK.findall(body):
        parsed = urlsplit(target.strip("<>"))
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        path = (directory / unquote(parsed.path)).resolve()
        if not path.is_relative_to(directory.resolve()):
            errors.append(f"reference leaves the skill folder: {target}")
        elif not path.exists():
            errors.append(f"missing reference: {target}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1] / "skills"
    directories = sorted(path for path in root.iterdir() if path.is_dir())
    if not directories:
        print("No skills found", file=sys.stderr)
        return 1
    failed = False
    for directory in directories:
        errors = validate_skill(directory)
        for error in errors:
            print(f"{directory.name}: {error}", file=sys.stderr)
        failed |= bool(errors)
    if not failed:
        print(f"Validated {len(directories)} skill(s)")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())

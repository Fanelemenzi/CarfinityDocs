"""Create Sphinx pages from the archived Markdown guides."""

from pathlib import Path
import re
import sys


PROJECT_DIR = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_DIR / "source"
ARCHIVE_DIR = PROJECT_DIR / "CarfinityDocs"
GUIDES_DIR = SOURCE_DIR / "guides"
GUIDE_ENTRY = re.compile(
    r"^\s+(?:.*?<)?guides/([A-Za-z0-9_.-]+)>?\s*$",
    re.MULTILINE,
)
INTENTIONALLY_EMPTY = {"assessment-workflow-system.md"}
PAGE_TITLES = {"popup": "Popup Dialog Example"}


def main() -> int:
    references = set()
    for page in SOURCE_DIR.glob("*.rst"):
        references.update(GUIDE_ENTRY.findall(page.read_text(encoding="utf-8")))

    missing_files = sorted(name for name in references if not (ARCHIVE_DIR / f"{name}.md").is_file())
    if missing_files:
        print("Sphinx navigation references missing Markdown files:", file=sys.stderr)
        for name in missing_files:
            print(f"  {name}.md", file=sys.stderr)
        return 1

    empty_pages = sorted(
        name for name in references
        if not (ARCHIVE_DIR / f"{name}.md").read_text(encoding="utf-8").strip()
    )
    if empty_pages:
        print("Sphinx navigation references empty Markdown files:", file=sys.stderr)
        for name in empty_pages:
            print(f"  {name}.md", file=sys.stderr)
        return 1

    archived_pages = {path.name for path in ARCHIVE_DIR.glob("*.md")}
    included_pages = {f"{name}.md" for name in references}
    unpublished = sorted(archived_pages - included_pages - INTENTIONALLY_EMPTY)
    if unpublished:
        print("Non-empty Markdown files are not in the Sphinx navigation:", file=sys.stderr)
        for name in unpublished:
            print(f"  {name}", file=sys.stderr)
        return 1

    GUIDES_DIR.mkdir(exist_ok=True)
    for name in sorted(references):
        source = (ARCHIVE_DIR / f"{name}.md").read_text(encoding="utf-8")
        source = re.sub(
            r"(?m)^[ \t]*(?:-{3,}|\*{3,}|_{3,})[ \t]*\r?\n"
            r"(?=(?:[ \t]*\r?\n)*[ \t]*#{1,6}\s)",
            "",
            source,
        )
        if not re.search(r"(?m)^#\s+\S", source):
            title = PAGE_TITLES.get(name)
            if title is None:
                print(f"Markdown page has no top-level title: {name}.md", file=sys.stderr)
                return 1
            source = f"# {title}\n\n{source}"
        (GUIDES_DIR / f"{name}.md").write_text(source, encoding="utf-8")

    print(f"Created {len(references)} Sphinx pages from {ARCHIVE_DIR.name}/.")
    if INTENTIONALLY_EMPTY & archived_pages:
        print("Excluded empty page: assessment-workflow-system.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

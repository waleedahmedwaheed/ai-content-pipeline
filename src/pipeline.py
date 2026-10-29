"""Content pipeline entrypoint stub."""

from __future__ import annotations
import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    args = parser.parse_args()
    out = Path("out")
    out.mkdir(exist_ok=True)
    (out / "research.md").write_text(f"# Research\n\nTopic: {args.topic}\n", encoding="utf-8")
    (out / "draft.md").write_text(f"# Draft\n\nTopic: {args.topic}\n", encoding="utf-8")
    (out / "linkedin.md").write_text(f"LinkedIn draft for: {args.topic}\n", encoding="utf-8")
    (out / "short-script.md").write_text(f"Short script for: {args.topic}\n", encoding="utf-8")
    print(f"Wrote starter artifacts to {out.resolve()}")


if __name__ == "__main__":
    main()

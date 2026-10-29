# AI Content Pipeline

AI content automation pipeline for research, drafting, and multi-platform publishing.

Turn a topic brief into researched notes, a draft, and channel-ready variants (blog, LinkedIn, short video script).

## Pipeline stages

1. **Research** — gather source notes and key points  
2. **Draft** — produce a long-form base article  
3. **Adapt** — create platform-specific variants  
4. **Review** — checklist / human edit gate  
5. **Publish** — export or push to destinations  

## Project layout

```text
src/
  research.py
  draft.py
  adapt.py
  publish.py
  pipeline.py
templates/         # prompt templates per stage
out/               # generated artifacts
requirements.txt
```

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env

python -m src.pipeline --topic "Trends in agentic AI tooling"
```

## Outputs

- `out/research.md`
- `out/draft.md`
- `out/linkedin.md`
- `out/short-script.md`

## Fit with real workflows

Pair this with schedulers, social APIs, or CMS hooks. Keep a human review step before anything goes live.

## License

MIT

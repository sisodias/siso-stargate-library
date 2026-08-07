# .agents/

Agent infrastructure for this repository.

- `scratchpad/` — temporary agent writes. Contents gitignored; use this rather
  than `/tmp` so work survives a session and stays attributable to the repo.
- `runs/` — durable run records.
- `briefs/` — agent briefs and prompt packs.

Machine and agent-to-agent artifacts are HTML. Human-facing READMEs stay Markdown.

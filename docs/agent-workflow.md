# Native Codex engineering workflow

Open this repository in the Codex App and use the main thread as Lead. Start with:

> Act as Lead under AGENTS.md. Deliver <task> on a feature branch. Delegate
> architecture/test-boundary analysis to an Architect and implementation to a
> Developer when useful. Have a separate Reviewer/QA review the final diff.
> Collect every result and validation command here. Open a Draft PR only;
> do not merge, deploy or publish.

The roles are task instructions in `AGENTS.md`, using native subagent tools.
No custom role files are needed: the Lead assigns each role in its spawn prompt.
No orchestrator, service, daemon or infrastructure was added. Models and reasoning
inherit from the parent. `.codex/config.toml` enables agents and sets
`agents.max_concurrent_threads_per_session = 5`, excluding the Lead. The Lead also
limits the whole task to five children and forbids nested delegation. A lower
managed/session limit wins. These settings do not increase account/runtime capacity.

Project configuration applies when the local client loads this trusted project;
open a fresh project chat if needed. This setup does not modify user-level trust,
models, sandbox or approvals. Read-only role instructions are a policy, not a
separate sandbox. If the client ignores project settings or hides native tools,
report that limitation; do not claim delegation from role names alone.

Before work: inspect status and main, preserve local changes, assign file ownership
and acceptance criteria. After work: collect results, run relevant existing checks,
obtain independent final-diff review, resolve findings, and report exact evidence.
Keep the PR draft. `AGENTS.md` lists repository checks and escalation boundaries.

Configuration reference: [official OpenAI subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Setup smoke test — 2026-11-21

The Lead invoked native `collaboration.spawn_agent` twice, receiving distinct
threads `/root/architecture_test_boundaries` and `/root/ci_review_regressions`.
Both completed read-only repository inspection and returned independent findings
to the Lead. Neither edited files, ran application tests/builds, committed,
mutated remote resources or spawned children. Actual delegation was observed.
The session offered four total concurrency slots (Lead plus three children);
only two children ran concurrently. Five-child capacity and project-config
hot reload were not tested. This smoke test verified native delegation, not
custom-agent selection or permission isolation.

This public repository was inspected in a clean feature-branch clone. Initially
there was no AGENTS.md, project Codex config, tracked GitHub workflow, PR template
or CODEOWNERS. Remote branch protection and live Pages settings were not verified.

Architect findings: the website is static HTML/CSS with local assets and no
runtime JavaScript/backend. `tools/check_site.py` covers links, fragments,
metadata and image/script constraints. Browser/device checks remain necessary
for rendering, keyboard use and QR decoding when website content changes.

Reviewer/QA findings: README documents GitHub Pages publishing main/root; merging
can change the live site. Keep the configuration PR on a feature branch and in
Draft. No publication settings or production files were changed. Retain the
public/private repository boundary when coordinating related app work.

For this configuration/documentation-only setup, run TOML parsing, independent
review, whitespace/scope checks and `python3 tools/check_site.py`. Browser visual
checks are unnecessary because HTML, CSS and assets remain unchanged.

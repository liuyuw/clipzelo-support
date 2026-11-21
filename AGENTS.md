# Engineering agent workflow

## Lead Agent
The main Codex thread is the Lead. Own the user request, acceptance criteria,
plan, delegation, integration, validation evidence and final report. Inspect Git
status and applicable instructions first. Preserve unrelated edits; use a clean
feature branch/worktree from current main when the checkout is dirty. Never
reset, stash or commit the owner's work without authorization.

## Roles
- **Architect:** Read-only exploration of affected paths, architecture, invariants,
  interfaces and test boundaries. Return a small plan with file references and risks.
- **Developer:** Implement only the Lead-assigned scope and file ownership. Preserve
  architecture and security boundaries; add regression tests for behavior changes.
  Report changed files, exact commands, results, skips and unresolved issues.
- **Reviewer/QA:** Independently inspect the final diff and affected execution paths,
  challenge assumptions and identify regressions, security risks and test gaps.
  Review read-only; return severity, file/line, evidence and required fixes, or
  explicitly state no findings plus remaining limitations. Do not self-approve.

## Delegation and coordination
For engineering changes, the Lead should use native Codex subagents for bounded
architecture analysis and independent review when useful. Small documentation
changes may skip architecture analysis, but still require independent review.
Give every task the checkout/base revision, objective, acceptance criteria,
read/write scope, owned files, constraints and expected evidence. Use at most
five concurrent subagents across the task (including descendants), or the lower
session limit. Only the Lead spawns agents; children must not delegate further.
Parallelize independent reads. Serialize edits to shared files; use separate
worktrees for overlapping implementation. No worker commits, pushes or opens PRs
unless the Lead explicitly assigns it. The Lead collects all results, resolves
conflicts and verifies the integrated diff. Stop/reuse finished agents before
spawning replacements if thread limits require it.

If native tools are absent or spawning fails, report delegation unavailable and
proceed only with clearly labeled single-agent work. Never present roleplay,
separate shell commands or an unobserved run as verified subagent delegation.

## Validation and independent review
Choose checks from the repository guidance below based on changed behavior.
Record exact commands, checkout/commit, passed/failed/skipped counts and limits;
never turn historical results, mocks or skipped cases into new passing evidence.
The Reviewer/QA must be a different agent from the implementer and review the
final candidate. Fix material findings and request re-review of affected changes.
The Lead reruns affected checks after fixes. Documentation/configuration-only
changes need diff/scope, TOML/schema and relevant link checks; full app builds
are unnecessary unless a runtime/build file changed. Report unavailable checks.

## Draft PR and approval boundaries
The Lead creates a feature branch, stages only assigned files, reviews the final
diff, commits and opens a **Draft PR** against main when authorized by the user.
Include problem/behavior, scope, validation, independent findings, limitations
and approvals needed. Keep it draft; never merge, enable auto-merge, deploy,
publish, upload/distribute builds or change production resources without explicit
separate authorization. Check existing branch-triggered automation before pushing;
if it may deploy/upload, stop and ask before that action. Preserve tests, CI,
GitHub workflows, signing, entitlements, privacy and permission boundaries.
Escalate conflicting requirements, destructive operations, credentials/access
changes, security-boundary changes, new dependencies/services/costs and blocked
approval requests. Do not weaken safeguards or bypass a rejected approval.
Instructions are coordination policy, not a separate sandbox: all agents inherit
the current session's permissions and approval rules.

## Public support site boundaries and checks
This is `liuyuw/clipzelo-support`: static `index.html`, `privacy.html`,
`styles.css` and local assets, served by GitHub Pages. Read `README.md` and
`assets/README.md`. Preserve support/privacy URLs and anchors, accessibility,
responsive layout, no runtime JavaScript/backend/analytics and current privacy
claims unless explicitly scoped and supported by evidence.

Run `python3 tools/check_site.py` for site edits. For HTML/CSS/asset changes,
preview locally with `python3 -m http.server 8766 --bind 127.0.0.1`; verify phone
and desktop widths, keyboard navigation, FAQ/support/privacy links, and changed
assets. Stop the preview server afterward. These are existing checks, not new CI.
This repository has no app build or package installation step.

README records Pages publishing main/root: merging can publish immediately.
Feature-branch Draft PRs do not authorize merge/publication. Keep private app
source, implementation findings, credentials and app-repository history out of
this public repository. Cross-repository tasks need separate Draft PRs and a
Lead summary; unresolved product/privacy wording requires owner resolution.

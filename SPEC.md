# App Studio decisions

The durable agreement between learner and AI. Update only agreed decisions and
actual evidence; pending is a valid state. Keep explanations/help in
[LEARNING.md](LEARNING.md), not a second copy here.

## Current stage

- **Current feature:** APP-002 (scope agreed).
- **Status:** APP-001 was kept and merged. Issue #1 is closed; PR #2 and the
  post-merge `check` and `windows` jobs are verified. APP-002 routes and forms
  are implemented; contracts and Chromium journeys pass. The learner's check
  interpretation, browser observation and keep decision are recorded; the
  learning summary is reviewed and approved. The marker is 2. The learner reports the
  post-marker elevated full check passed; the standard non-elevated run here
  still fails only at Windows symlink creation.
- **Next step:** Commit, push and open the PR linked to issue #3; verify both CI
  jobs before merging.
- **Implementation marker:** `studio.json` declares `implemented_through: 2`.

This repository owns application code. Server/proxy changes and production
deployment are outside these three local-development lessons. Prepared helpers
are reusable foundations, not evidence that unfinished routes are implemented.

## APP-001 · Branded homepage

**Scope:** make the neutral FastAPI homepage express one chosen identity with
a simple original SVG mark, coherent copy, navigation and shared style tokens.
Keep account actions honest about their unfinished state.

| Decision | Agreement |
|---|---|
| Visitor and concrete use situation | College student working part-time; before registering for classes, checks which class times fit around work shifts. |
| Reused IS117 brand, or name / promise / primary archetype | New brand: ShiftCheck. Promise: “Check how class times fit around your work shifts before you register.” Primary archetype: Guide. |
| One visible choice and visitor benefit | Visible name: “ShiftCheck.” The learner says it reminds students to check work hours before signing up and may help them avoid changing their schedule later. |
| Voice / design direction | Helpful advisor; short and friendly copy; warm cream background, white sections and deep-green buttons. |
| Own issue / branch / PR | [#1](https://github.com/GerardA8/Gerards-app-studio/issues/1); `feature/app-001-branded-homepage`; PR pending. |

**Keep when:** the agreed identity is visible and usable at desktop/narrow widths;
full foundation + APP-001 checks pass; AI review and the learner's actual check
interpretation/browser observation/keep reason are recorded; reviewed evidence
and verified GitHub state are linked below.

## APP-002 · Signup, login and logout

**Scope:** add browser forms and REST behavior for member signup, login, a private
dashboard and logout backed by SQLite. Reuse the prepared password/JWT/CSRF/session
helpers; keep data local. New accounts cannot choose their role.

| Decision | Agreement |
|---|---|
| Expected public/private behavior and account flow | Member signup, login, private dashboard and logout using local SQLite and prepared security helpers; browser forms and REST API follow the same login rules. |
| Request behavior before / after login | Before login, the browser redirects to login and REST returns 401 without dashboard data; after login, the browser shows the member's private dashboard and REST returns 200 with that member's data. |
| Valid and rejected cases to demonstrate | Prepared contracts cover signup/login, duplicate and invalid signup, wrong credentials, CSRF rejection, unauthenticated access, and logout revocation. |
| Own issue / branch / PR | [Issue #3](https://github.com/GerardA8/Gerards-app-studio/issues/3); `feature/app-002-member-accounts`; PR pending. |

**Keep when:** the agreed forms/API work; duplicate/invalid signup and wrong
credentials are rejected; passwords are hashed; authentication uses validated,
expiring JWTs with protected cookies and CSRF; private requests require a live
session and logout revokes it. Full cumulative checks, AI review, actual learner
contributions and GitHub state are recorded. This is not a production-security certification.

## APP-003 · Server-enforced roles

**Scope:** enforce a small member/admin boundary in the API and browser. Assign
roles only through the trusted local terminal command; use current server-side
permissions, including for an existing session after a role change.

| Visitor | Homepage | Member area | Admin area/API |
|---|---|---|---|
| Anonymous | Allowed | Login required | Login required |
| Member | Allowed | Allowed | Forbidden |
| Admin | Allowed | Allowed | Allowed |

| Decision | Agreement |
|---|---|
| Intended admin-only result | Pending |
| Actual allowed/denied request evidence | Pending |
| Own issue / branch / PR | Pending |

**Keep when:** a direct request cannot bypass the role boundary, role changes
take effect as specified, new signup remains member-only, and full cumulative
checks plus AI review pass. Link the learner's actual interpretation/observation,
reviewed record and verified GitHub result. Hidden navigation alone is insufficient.

## Evidence

Link actual files/checks and the student's own issues/PRs. No fabricated URLs,
customer research or claims that a timestamp proves learning.

| Feature | Files / own issue / PR | Actual checks and learner observations | Kept / GitHub state |
|---|---|---|---|
| APP-001 | `app/brand.json`, `app/templates/home.html`, `app/static/logo.svg`, `studio.json`; [issue #1](https://github.com/GerardA8/Gerards-app-studio/issues/1); branch `feature/app-001-branded-homepage`; [PR #2](https://github.com/GerardA8/Gerards-app-studio/pull/2) | Initial unelevated cumulative run: foundation pytest 95 passed, 2 skipped, 1 failed with Windows WinError 1314 creating a symlink; APP-001 contract pytest 2 passed; Chromium 2 passed. After marker 1, learner reports normal full check: foundation pytest 96 passed, 2 skipped, 2 deselected; APP-001 contract pytest 2 passed; Chromium 2 passed. PR `check`/`windows` passed on the updated head; post-merge main run [#4](https://github.com/GerardA8/Gerards-app-studio/actions/runs/42339628835) also passed both jobs. AI browser review at 390px found no horizontal overflow. Learner says the contract can catch stale “Your Project” branding, but not phone readability. At phone width, learner reports the headline wraps to “Plan classes with” / “work in mind.” Initial neutral-page observation: heading “A small idea. A real application.” | Learner chose keep; issue #1 closed; PR #2 merged; CI verified |
| APP-002 | `app/features/accounts.py`, `app/templates/signup.html`, `app/templates/login.html`, `app/templates/dashboard.html`; [issue #3](https://github.com/GerardA8/Gerards-app-studio/issues/3); branch `feature/app-002-member-accounts` | Learner reports the post-marker elevated `python3 studio.py check` passed: foundation 96 passed, 2 skipped, 2 deselected; contracts 14 passed; Chromium 2 passed. AI's standard non-elevated run passed Black/Pylint, contracts 14 and Chromium 2, but foundation had 95 passed, 2 skipped, 2 deselected and 1 WinError 1314 symlink failure. Focused account/security tests: 62 passed, 1 skipped. AI browser review found no horizontal overflow at 390px or desktop width. The learner says the check could catch `/api/me` disclosing account details before login or including a private value such as a password hash after login. After logout, the learner clicked Member space and says ShiftCheck asked them to log in before they could see the dashboard; they would keep the behavior because it protects the dashboard after logout. | Learner chose keep; PR pending |
| APP-003 | Pending | Unfinished; explicit contracts not yet passed | Pending |

The instructor's reference branches show possible implementations. They do not
establish this repository's completion or the learner's own reasoning.

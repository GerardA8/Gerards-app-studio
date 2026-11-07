# Conversation evidence

AI-drafted task summary, not a transcript or grade. It may be public. Use actual
short words or labeled paraphrases; disclose help and leave missing responses
pending. The learner reviews, corrects or removes new excerpts before commit/push.
Accuracy approval is not proof of understanding. Label simulated trials explicitly.

**Available conversation context:** This conversation includes local setup, the
foundation check and the learner's initial neutral-page observation. No earlier
lesson contributions are recorded.

## APP-001

- Prediction: The learner expects a student who sees “ShiftCheck” to think it
  helps check whether a class overlaps with a work shift before registration.
- Check interpretation: The learner says the contract could catch the old
  “Your Project” name remaining and does not show whether the headline and logo
  are easy to read on a phone.
- Browser observation: At phone width, the learner reports the headline wraps
  onto two lines: “Plan classes with” / “work in mind,” and confirms the second
  line keeps “work in mind” together. On the initial neutral page, the learner
  reported: “The homepage heading says ‘A small idea. A real application.’”
- Keep decision: The learner would keep this version because the headline is
  easy to read at phone width and the second line keeps “work in mind” together.
- Review: Learner reviewed and approved the summary with a clarification about
  the name's origin; this confirms record accuracy, not understanding.
- Help/gaps: AI helped prepare the local environment and open the prepared issue
  form. The learner chose a new brand, ShiftCheck, for a part-time college
  student checking class times against work shifts before registration. The
  learner says the name is a “quick reminder to check work hours before signing
  up” and may help avoid changing the schedule later. Issue #1 was created and
  `feature/app-001-branded-homepage` was created. AI proposed a promise; the
  learner approved: “Check how class times fit around your work shifts before
  you register.” AI suggested Guide; the learner accepted it and said ShiftCheck
  should sound like “a helpful advisor” as students compare class times with
  work shifts. The learner accepted a calm visual suggestion and specified a
  warm cream background, white sections, deep-green buttons, and short, friendly
  wording. The learner reports ChatGPT helped phrase their brand decisions,
  prediction, check interpretation and keep reason. The learner says ChatGPT
  suggested “ShiftCheck” in a separate chat; they chose the name and brought it
  into this chat. That separate conversation is not available here. AI
  implemented the agreed homepage and SVG. The initial unelevated foundation
  run had 95 passed, 2 skipped and 1 failure because Windows denied symlink
  creation (WinError 1314); its 2 APP-001 contract tests and 2 Chromium journeys
  passed. After marker 1, the learner reports the normal full check had 96
  foundation tests passed, 2 skipped and 2 deselected, with 2 APP-001 contract
  tests and 2 Chromium journeys passed. AI browser review at 390px found no
  horizontal overflow.
  The learner reviewed and approved the record, including the clarification
  about the name's origin. The initial unelevated symlink failure is documented;
  the learner reports both later elevated checks passed.
- Evidence links / next step: [APP-001 issue #1](https://github.com/GerardA8/Gerards-app-studio/issues/1),
  [merged PR #2](https://github.com/GerardA8/Gerards-app-studio/pull/2);
  APP-001 is complete. Agree APP-002 scope next.

## APP-002

- Prediction: The learner expects an unauthenticated browser dashboard request to
  redirect to login and REST to return 401 without data; after valid login, the
  browser should show the member's dashboard and REST should return 200 with
  that member's data.
- Check interpretation: The learner says the check could catch `/api/me`
  disclosing account details before login or including a private value such as a
  password hash after login.
- Browser observation: After logging out, the learner clicked Member space again
  and says ShiftCheck asked them to log in before they could see the dashboard.
- Keep decision: The learner would keep the behavior because, as they put it,
  it protects the dashboard after logout.
- Review: The learner reviewed and approved the APP-002 summary and asked to
  include that ChatGPT helped phrase their contributions.
- Help/gaps: The learner approved member signup, login, a private dashboard and
  logout using local SQLite and the prepared security helpers. They said browser
  forms and REST should “enforce the same login rules” and deferred member/admin
  permissions to APP-003. Issue #3 and `feature/app-002-member-accounts` were
  ready before implementation. AI connected the HTML forms and REST routes to
  the prepared security helpers and added signup, login and private dashboard
  templates; no role/admin behavior was added. Focused account/security tests
  passed 62 with 1 skipped; cumulative contracts passed 14 and Chromium
  journeys passed 2. AI's non-elevated full run had 95 passed, 2 skipped, 2
  deselected and one symlink-privilege failure (WinError 1314); the learner
  reports the post-marker elevated full check passed with foundation 96 passed,
  2 skipped, 2 deselected, 14 contracts passed and 2 Chromium journeys passed.
  AI browser review found no horizontal overflow at desktop and 390px; AI used a
  generated throwaway local account for this review, not as learner evidence.
  The learner reports ChatGPT helped phrase their prediction, check
  interpretation, browser observation and keep decision.
- Evidence links / next step: [APP-002 issue #3](https://github.com/GerardA8/Gerards-app-studio/issues/3);
  review this summary before committing and opening the PR.

## APP-003

- Prediction: Pending.
- Check interpretation: Pending.
- Browser observation: Pending.
- Keep decision: Pending.
- Review: Pending.
- Help/gaps: Pending.
- Evidence links / next step: Keep APP-002 before agreeing this lesson.

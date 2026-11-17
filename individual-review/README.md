# Gerard Almenares | IS 373 Individual Plan

## 1. Portfolio + career research

My target reader is a hiring manager for a junior full-stack developer. I want them to find a project, identify my contribution, and open evidence of one tested feature.

Employer sources located for the November 17, 2026 review:

- [Authentic — New Grad Software Engineer](https://job-boards.greenhouse.io/authenticinsurance/jobs/4114318009), NYC on-site. Build React and FastAPI features, collaborate with operations, and improve internal tools. The posting accepts web-app coursework and specifies degree and graduation requirements. React, FastAPI, and PostgreSQL are preferred. My crypto app and ShiftCheck show work at both layers. By Nov 24, I plan to trace one feature from the browser to the database.
- [Palantir — Forward Deployed Software Engineer, New Grad](https://jobs.lever.co/palantir/2e6b0ac8-83e9-4be5-a3aa-cf319f751728), NYC hybrid. Understand customer operations, identify the problem, and build a solution. Requires programming proficiency, an engineering degree, and December 2026 or spring 2027 graduation. My ShiftCheck design addresses a working student's scheduling problem. By Nov 24, I plan to collect outside reader feedback.
- [Spur — Applied AI Product Engineer](https://jobs.ashbyhq.com/spur/3e021029-67f0-4574-a1b2-8517fa531529), NYC on-site. Design features, test them, and own them after deployment. My ShiftCheck record shows browser testing. By Nov 24, I plan to add an AI answer evaluation. Junior eligibility and the required versus preferred qualifications still need verification.

FDE work starts with investigating a customer's problem. Full-stack development is my provisional target because I can already show how a browser action connects to a backend decision. I compared a single scrolling page with a short homepage linking to two case studies. I chose the second layout so a reader can open the individual RAG app or my contribution to the group project directly. Each case study will link code, a demo when available, and a check. About and Contact will include my resume, GitHub, and a professional contact route.

- **Changed** — Selected the reader, case studies, and layout.
- **Checked** — Opening the admin page as a member showed access denied. After promotion, the same account could open it. [My observations](../LEARNING.md#app-003) and [PR checks](https://github.com/GerardA8/Gerards-app-studio/pull/6/checks).
- **Next** — Ask a peer which role the portfolio suggests and which skill is hardest to verify. Record their answer and my decision. At Build, check links, keyboard navigation, mobile readability, and signed-out access.

## 2. RAG app + technical research

My Scheduling Database Assistant will help students understand my SQLite scheduling project. Permitted sources are my own schema notes, data dictionary, and SQL examples with fictional employees.

[Chroma](https://docs.trychroma.com/docs/querying-collections/query-and-get) uses embeddings, numeric representations that support similarity search. A [graph database](https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/context-providers/neo4j) could follow relationships from employee to assignment to shift. I chose vector retrieval because the reader needs explanations from a small document collection and may use different wording.

**Planned source trace.** My draft note says each assignment connects an employee to a shift. I will verify the column names against the schema and import the note with its SQL example as one chunk with a stable ID, filename, and heading. FastAPI will embed the question, retrieve three chunks, and pass them to the answer model. The answer should cite the supporting section.

**Planned checks**

1. Ask how to list employees assigned to one shift. Expect the relationship note in the top three, a filter by shift ID, and a join by employee ID. A missing note indicates a retrieval problem. A wrong join despite the right note indicates an answer problem.
2. Ask “Who's working this shift?” Expect the same explanation without invented names.
3. Ask about overtime policy. Expect an insufficient-evidence response.
4. Import the same documents twice. Expect a stable chunk count and working citations.
5. Restart the app. Expect the saved index and cited passage to remain available.

- **Changed** — Selected the sources, retrieval approach, and evaluation questions.
- **Checked** — The documentation review confirmed Chroma supports similarity queries. App tests have not run.
- **Next** — Verify the schema, run the first question locally, and save the retrieved passage and answer. Before hosting on DigitalOcean, measure free memory and disk, confirm persistent storage, and check model cost.

AI helped locate sources and draft this plan. Personal source verification and peer feedback are pending.

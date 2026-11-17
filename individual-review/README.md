# Individual Portfolio and RAG App — Plan
Gerard Almenares | IS 373 | November 17, 2026

## 1. Portfolio + career research

### Reader and career direction

My portfolio will help a hiring manager evaluate me for junior full-stack developer positions. I want the reader to understand my interests, open my projects, and find evidence of my contributions.

I compared full-stack development with forward deployed engineering. Full-stack development is my provisional target because I have experience with frontend interfaces, backend APIs, and databases. Forward deployed engineering interests me because it involves understanding users’ problems and building solutions around their needs.

### Employer research

The following original employer sources were located with AI assistance for this review. My personal verification of current availability and eligibility remains pending.

| Employer and posting | Responsibilities and qualifications | Evidence, gap, and next action |
|---|---|---|
| [Authentic — New Grad Software Engineer](https://job-boards.greenhouse.io/authenticinsurance/jobs/4114318009) | NYC, on-site. Build React/FastAPI features, collaborate with product and operations, and improve internal tools. Requires web application experience, programming fundamentals, and specified degree/graduation timing. React, FastAPI, PostgreSQL, and cloud experience are desirable. | My React coursework and ShiftCheck FastAPI project provide relevant examples. I need to explain the connection between frontend and backend work more clearly. By November 24, document one feature with code and check links. |
| [Palantir — Forward Deployed Software Engineer, New Grad, Commercial](https://jobs.lever.co/palantir/2e6b0ac8-83e9-4be5-a3aa-cf319f751728) | NYC, hybrid. Understand customer operations, investigate problems, and build technical solutions. Requires programming proficiency, an engineering degree, and December 2026 or spring 2027 graduation. Preferred degree fields include computer science and software engineering. My eligibility needs verification. | ShiftCheck addresses a working student’s scheduling problem. I need outside feedback on whether the design communicates that purpose. By November 24, record a peer’s observation and my response. |
| [Spur — Applied AI Product Engineer](https://jobs.ashbyhq.com/spur/3e021029-67f0-4574-a1b2-8517fa531529) | NYC, on-site. Design features, test them, and own them after deployment. This is a reference for AI product work. Required/preferred qualifications and junior eligibility still need verification. | My ShiftCheck record includes browser checks. My proposed RAG app needs evaluated answers. By November 24, document one question, retrieved passage, answer, and evaluation result. |

### Portfolio outline and layout decision

The planned pages are:

- Home with an introduction, target direction, and featured projects.
- Individual RAG case study with sources, architecture, my contribution, checks, and a demo when available.
- Group-project case study identifying my contribution and linking the team’s work.
- About and Contact with my résumé, GitHub, and professional contact information.

I compared a biography-first homepage with a project-first homepage using the same content. I chose project-first so a hiring manager can quickly find evidence. This is a proposed design decision that still needs peer feedback.

Public portfolio pages will work without login. Administration actions will require server-side authorization.

### Changed / checked / next

**Changed:** Selected a provisional career direction, target reader, and portfolio layout.

**Checked:** My existing ShiftCheck record documents that a member was denied access to the admin page. After promoting the test account, access worked. Demoting it restored the denial.

[Recorded observations](https://github.com/GerardA8/Gerards-app-studio/blob/main/LEARNING.md#app-003)  
[Role implementation and check history](https://github.com/GerardA8/Gerards-app-studio/pull/6)

**Next:** Complete employer-source verification and ask a peer whether my target role and featured evidence follow from the postings. Record their feedback, my decision, and the resulting edit. During Build, check mobile readability, keyboard navigation, links, and signed-out access.

**Peer feedback:** Pending.

## 2. RAG app + technical research

### Reader and user story

My proposed Scheduling Database Assistant will help a student understand my SQLite scheduling project.

As a student, I want an explanation linked to a schema note or SQL example so I can verify how employees, assignments, and shifts connect.

### Permitted sources

I plan to use my own schema notes, data dictionary, and annotated SQL examples with fictional employees and shifts. The exact files and contents still need verification. Each source will receive a stable ID and version.

### Research and technology comparison

RAG retrieves relevant source material and supplies it to a language model as context for an answer. Embeddings represent text numerically for similarity search. Chunking divides documents into retrievable passages. A graph represents entities and explicit relationships.

| Approach | Potential benefit | Limitation |
|---|---|---|
| Keyword search | Simple baseline for exact table names and SQL terms. | May miss questions using different wording. |
| Vector retrieval | May find related explanations when a question paraphrases the notes. | Similarity alone does not establish that a passage supports an answer. |
| Graph retrieval | Could follow relationships among employees, assignments, and shifts. | Requires explicit modeling and maintaining those relationships. |

I provisionally chose Chroma vector retrieval because the initial questions focus on short explanations. I will compare its results with keyword search before claiming it improves retrieval.

Technical sources:

- [Chroma query documentation](https://docs.trychroma.com/docs/querying-collections/query-and-get)
- [Neo4j graph retrieval overview](https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/context-providers/neo4j)
- [SQLite foreign key documentation](https://sqlite.org/foreignkeys.html)

### Proposed import and answer flow

Permitted documents will be cleaned, chunked, embedded, and stored in a persistent index. Each chunk will retain its source ID, version, and heading.

I will compare heading-based chunks with 300-word chunks using 50-word overlap. Heading-based chunks are my initial choice because they can keep a SQL example with its explanation. I will inspect whether either method separates necessary context.

FastAPI will receive a question, retrieve relevant chunks, and provide them to the answer model. The response will include references that open the supporting passages.

For example, a schema note could explain that an assignment links an employee to a shift. A question asking how to find employees assigned to one shift should retrieve that note and the relevant SQL example. If the expected passage is missing, retrieval needs investigation. If it is present but the answer describes the wrong join, answer generation needs investigation.

### Planned evaluation questions

| Question | Expected source |
|---|---|
| How are employees connected to shifts? | schema-01, covering assignment relationships |
| How do I find who is working a particular shift? | query-01, containing the relevant join |
| What information does an assignment store? | dictionary-01 |
| Why must an assignment reference an existing employee? | constraints-01 |
| What is my employer’s overtime policy? | No supporting source. The app should report insufficient evidence. |

These source IDs are proposed. I will verify their contents before running the questions.

### Five observable checks

1. A supported answer cites a relevant passage that the reader can open.
2. A paraphrased question retrieves the expected evidence.
3. A question outside the documents produces an insufficient-evidence response.
4. Reimporting unchanged documents creates no duplicate chunks.
5. A visitor cannot access import or administration actions.

### Hosting and resource limits

I plan to reuse FastAPI and investigate hosting on my existing DigitalOcean server. Before deployment, I will measure available memory and disk, confirm persistent storage, and check API costs.

The embedding model, generation model, API access, and final hosting capacity remain pending. The query and document embeddings must use a compatible model. Initial testing will use a small source collection.

### Changed / checked / next

**Changed:** Defined the reader, proposed source collection, retrieval comparison, workflow, and evaluation questions.

**Checked:** Technical documentation was reviewed with AI assistance. App import, retrieval, answer quality, and hosting checks have not run.

**Next:** Verify the source files, complete the model and resource decisions, and run one question locally. Save the expected source, retrieved passages, generated answer, and evaluation result together.

### Contribution and assistance

My existing ShiftCheck decisions and browser observations are documented in the linked project record. AI assisted with source discovery, comparisons, and drafting this plan. Personal source verification, peer feedback, and RAG evaluation results remain pending.

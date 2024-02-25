---
title: "Managing the FreeCAD Grant Program"
description:
    "How to manage the FreeCAD Grant Program"
layout: default
mermaid: true
---

# {{page.title}}

## Managing resources

### Main program page

The program page is expected to provide the latest information on the program: current stage, up-to-date rules, up-to-date list of this year’s issued grants, a link to the program’s archive of past issued grants.

### Program archive

The program archive pages should list past issues grants grouped by year, in reverse chronological order. Information about each grant should include:

- Who it was issued to
- For what project (short name)
- When the grant was voted on
- Scope of the project (description, deliverables)
- Status of the project: successful, unsuccessful

### Git repository for grant applications

All applications are managed through a dedicated [git
repository](https://github.com/FreeCAD/FPA-grant-proposals/).

Applicants submit an issue using one of the two available issue templates: for
fixed goal or for time commitment.

For grant applications that have been approved, issues stay open until either
proposed work is done or the grant contract has been terminated.

For grant applications that have been declined, issues get closed immediately
after voting.

All management is done by either the grant program manager or any member of
the FPA general assembly.

## Annual program lifecycle

### Program preparation 

1. January each year — propose 1) a timeline to the general assembly and the technical committee, 2) a budget.
2. Have the FPA general assembly vote on the timeline and the budget.
3. See if the git repository for grant applications needs a cleanup: issues that need closing etc.

### Program announcement checklist

1. Ask if everyone's still ready, especially the technical review committee.
2. Update the program page for the new timeline.
3. Write the announcement post stating: 

- Program objectives (1-2 sentences)
- How much money the FPA is releasing for the program
- General timeline
- Mention that out-of-program grants will still be possible
- Say where rules are listed
- State where applications can be submitted

4. Publish the blog post.

### Collecting applications

All grant applications are submitted to the dedicated git repository.

### Analyzing applications

This is done in two steps.

Step 1: The grant review committee studies grant applications using the following criteria (order is important):

1. Whether the proposal is technically sound:

- Does it aim to fix a real issue?
- Does it look like a good solution to the issue?
- Has the applicant demonstrated understanding of the issue?
- Is the proposed fix or a new feature technically correct or bogus?

2. Whether the goal appears to be achievable in the proposed timeframe

Step 2: The FPA general assembly takes grant review committee’s verdict into consideration and further looks at the following:

1. Whether the project would improve FreeCAD or its ecosystem in a significant manner. Significance criteria:

- Contributes to achieving [FreeCAD Roadmap](https://freecad.github.io/DevelopersHandbook/roadmap/) items
- Improves projects that FreeCAD depends on

2. Whether the applicant has demonstrated the technical ability to work on the project in general:

- Has a public track record of programming CAD software or work on algorithms used in the program
- Has a public track record of contributing to FreeCAD and/or an ecosystem project of interest (e.g. OCCT, Coin3D)

3. Whether the scope of the project matches demonstrable skills of the developer and is doable in the proposed time frame

4. Whether the requested compensation is generally in line with what’s expected (not too little, not too much; e.g. $5/hour is too little, $200/hour is too much)

### Voting for grants

The general assembly reads reviews made by the technical review committee and votes for proposals.

### Announcing grants

1. Update the list of ongoing projects on the FPA website
2. Publish the same list of approved projects in the FreeCAD blog.

For each approved project state:

- Name and/or nickname of the applicant
- Name of the project
- Descriptions of the project with deliverables
- Link to detailed description on GitHub (public grant proposal with implementation details, stages etc.)
- Estimated time of submission of final results
- Date when the grant was approved
- Grant amount

### Interim updates

All contributors who received grants are obligated to submit interim reports.

For contributors working on fixes goal projects, reports are expected at the
end of each stage.

For contributors working on time commitment projects, reports are generally
expected every two weeks.

Each report should contain a list of work done, preferably as a list of submitted pull requests with status on each one: in draft, open and waiting for review, passed review with further changes pending, merged. Reports are also expected to outline further planned work. Contributors are encouraged to talk about challenges to give the FPA heads up on complications.

### Closing grant projects

1. The contributor submits the last pull request.
2. The PR passes code review and is merged.
3. The contributor writes and submits the final report.
4. The program manager verifies that all work has been done.
5. The treasurer issues the last payment.

### Wrapping up the program

1. The grant program manager collects information about all grants issued during the year and writes a public report:

- What grants were issued during the year
- Which projects were successful and which weren't
- What was the outcome of each successful project
- What's salvageable in unsuccessful projects
- What was the planned and the actual budget

2. The grant program manager writes and publishes shorter version of the report for the FreeCAD blog and links to the full report.

### Post-mortem

1. The grant program manager collects feedback from all stakeholders: what things worked well, what things need rethinking, what things need scrapping entirely.
2. The grant program manager proposes changes to program rules as a PR to the 'FPA' git repository.
3. The FPA general assembly reviews the proposal and requests further changes or merges the PR.

## Out-of-program grants

For grants applications submitted outside of the annual programs, the same rules generally apply:

- Grant application requirements are the same.
- Applications are first reviewed by the technical committee, then by the general assembly.
- voting is done within two weeks since submission.
- The first payment is issued by the treasurer within a week since confirmation.
- Information about the approved grant application is published on both the grant program page and the FreeCAD blog.
- The contributor submits pull requests (for coding work) and interim progress reports.
- The treasurer issues payments for each completed stage.
- Once the work is completed, the respective issue in the grant program git repository is closed, the entry on the website is moved to the archive, a blog post is published in the FreeCAD blog to notify on completion of the project.

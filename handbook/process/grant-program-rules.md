---
title: "Grant Program Rules"
description:
    "How the grant program works"
layout: default
---

# {{page.title}}

The FreeCAD Grant Program aims to foster rapid development of FreeCAD and its ecosystem by hiring developers and non-programming contributors. Their work is to be funded by the community, grants are issued by the FreeCAD Project Association.

## Stakeholders

The FreeCAD grant program has multiple stakeholders with different roles:

* **The grant committee**: reviews grant applications, issues recommendations for accepting or denying an application
* **The FPA general assembly**: assesses grant applications and reviews made by the technical committee and votes on the budget allocated to the program.
* **The FPA board**: only serves as the treasurer: allocates money for each annual grant program and individual grants, does payouts, publishes reports. Does not make decisions on technical topics, does not vote for or against particular grant applications.
* **Contributors**: developers and non-programming contributors. Their job is to pick a project, decompose it into stages, estimate the cost, submit a grant application, then upon approval, complete the project within the agreed timeframe.
* **PR reviewers**: a group of FreeCAD maintainers who provide feedback on submitted pull requests and have the privileges to merge patches. Their role is to review and merge PRs submitted by contributors working on a grant, as part of their routine work.
* **General community**: other developers and users of FreeCAD who can provide feedback on issued grants and raise concerns if they think that some of the grant assignments have been misplaced.

## General timeline for the annual program

1. The FPA board submits a proposal for annual grant program budget to the general assembly and then announces the budget as part of the annual program announcement.
2. A contributor comes up with a project idea, looks into existing code, consults with other developers / module maintainers, comes up with a grant application (see below). The grant application is then submitted to the grant committee for review using a GitHub issue in a dedicated GitHub repository.
3. The grant committee reviews each application and provides public feedback on technical aspects of the proposal within one week after the submission deadline.
4. The FPA general assembly votes on each proposal within one week after the grant committee’s review deadline.
5. Within three days after the voting has been done, The FPA updates the program page listing each confirmed grant, its scope, ETA, developers, and overall expected cost. Then the FPA publishes a blog post at blog.freecad.org, that lists approved projects.
6. The contributor starts writing code, submits PRs, sends progress reports on completion of each stage, and receives the compensation for each stage.
7. The FPA publishes the annual recap of the program.

## Annual program vs individual grants

The program is streamlined for issuing multiple grants at once to batch all the work by the grant review committee, the general assembly, and the FPA treasurer. However individual grants outside the program will continue to be reviewed and voted on by the general assembly. Such applications can be submitted at any time.

## Fixed goal vs time commitment

The grant program allows for two types of grants:

1. **Fixed goal.** Grant is provided to accomplish a certain task such as development of a new feature. This type of project assumes stages of development and a deadline.
2. **Time commitment.** Grant is provided for continuous work on a complex project that assumes many small tasks not necessarily related to each other. Examples: code refactoring, topological naming issue mitigation. Grant applications for such projects do not require stages. This type of project assumes an estimation of hours to be spent on the project and a per-hour rate.

## Who qualifies as developer

Both individuals and groups of individuals can qualify as grant acceptees.

The FPA welcomes applicants of all ethnicities, nationalities, sexes, and genders to apply for participation at the program.

The only age restriction is the minimum age required to 1) perform work legally in the country of applicant’s residence, and 2) sign a contract with the FPA on behalf of themselves.

Presently we do not know of any restrictions that would forbid us to issue grants to residents of countries under EU sanctions, unless those residents are under personal sanctions or sending a wire transfer is impossible. Nevertheless, we reserve the right to regretfully decline such an application should serious legal concerns arise.

The program is geared towards individual contributors. However, the FPA grant committee will accept grant applications from a group of contributors as long as the group is either an incorporated company or a group of individuals represented by a single person. Neither the grant committee, nor the FPA general assembly, nor the FPA board members can resolve any disputes arising inside the group of contributors.

_Example:_ three former GSoC students can form a group and submit a grant application with a scope of work for three developers, however only one will be the official representative of the group. This person is expected to submit the application and then progress reports, as well as receive and distribute payouts between group members.

## Grant topics

The grant committee accepts applications to improve both FreeCAD and its ecosystem.

For FreeCAD-related projects an overall preference is given to projects that address major issues that are covered by the [roadmap](https://freecad.github.io/DevelopersHandbook/roadmap/).

Ecosystem includes (but is not limited to) FreeCAD infrastructure, as well as projects that are hard dependencies for FreeCAD, such as OCCT and Coin3D libraries.

As neither the grant committee nor FPA members have control over ecosystem projects, the applicant is expected to demonstrate familiarity with external project’s source code, e.g. merged pull requests, as well as a written agreement that ecosystem project maintainers are aware of the proposal, support the development, and are ready to review patches. The FPA cannot issue a grant for work on an ecosystem project if the said project is unwilling to accept proposed patches.

## How to submit a grant application

Grant applications are managed in a [public GitHub repository](https://github.com/FreeCAD/FPA-grant-proposals) in the FreeCAD project.

To submit a grant application, the applicant creates an issue and chooses the application template in the form, then fills all the fields.

## Passing criteria

Grant applicants must demonstrate:

* Hands-on experience within the scope of the proposal
* Public track record that confirms their qualification to accomplish the proposed project, such as commits or merged pull requests to the Git repository of FreeCAD or its ecosystem projects.
* Ability to plan their own work.
* Ability to estimate risks and come up with a plan to mitigate them.
* Ability to come up with a market-level estimation of the cost and reasoning for effort estimation.

The FPA general assembly expects groups of contributors to present proof of qualification of each involved member.

The grant review committee can ask the applicants questions in the submitted GitHub issues before reaching the conclusion.

## Compensation scheme and payouts

We treat the planning of a project as a project stage of its own, so contributors whose applications were approved get the first payout within 10 days after the announcement of the voting on grant proposals.

We divide payouts between stages. Example: a project has 3 development stages. The contributor gets 4 payouts: 1 for planning, 1 for the first complete stage, 1 for the second stage, and 1 for the last stage. It's possible to divide payouts not evenly between stages, if some of the stages assume either more or less work than the other ones. The applicant should provide reasoning for that.

We use wire transfers and Wise.com for paying contributors. It is up to the contributor to provide correct bank account details and intermediary bank details (where applicable).

## Progress reports

**For grants with fixed goals**, we expect a progress report at the end of each stage. It’s best to find a sweet spot between general statements and an overly detailed account:

* List major changes and respective pull requests.
* Tell us what the challenges were (if any).
* Tell us if you think the rest of the project should be reorganized based on what you’ve learned, and why.
* Tell us if you are ready to continue working on the project as agreed.

**For grants with time commitment**, we expect reports every two weeks. For each of the two weeks please provide:

* Short descriptions of what was going on
* List pull requests with a quick overview (PR titles will be sufficient)

Example: [https://github.com/FreeCAD/FPA/blob/main/reports/Toponaming/bgbsww_report1.md](https://github.com/FreeCAD/FPA/blob/main/reports/Toponaming/bgbsww_report1.md)

## Code submission

For work on upstream FreeCAD source code, the requirements are:

* Smaller pull requests that can be integrated without breaking existing functionality.
* Pull requests will go through the same contributing process as all other submissions. Therefore PRs must be rebased, pass CI/CD, and fix known problems.
* Contributors should respond to requests for information and improvements in PR comments.
* Contributors should be willing to appear at weekly merge meetings if asked to discuss the contribution.

For ecosystem projects, we expect you to align with maintainers of those projects on best practices for submitting changes.

## Termination of a grant

The FPA reserves the right to terminate a grant in the following cases:

* The grant acceptee failed to complete the next stage of work entirely.
* The grant acceptee abruptly stopped the work without warning.
* The quality of code is inconsistent with credentials provided in the grant application.

The FPA can still issue a partial payment for an incomplete stage. The prerequisites for that are:

1. The grant acceptee communicated their change of plans in a timely manner.
2. The grant acceptee submitted part of the work as a pull request that has been reviewed and merged.

The amount of partial compensation will be decided on in each individual case.

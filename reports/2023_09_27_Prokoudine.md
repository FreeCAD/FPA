---
title: "Revamping the grant program of the FreeCAD Project Association"
description: "A research into ways to improve the FPA's own grant program based on best practices in FOSS"
layout: default
---

By [Alexandre Prokoudine](email:alexandre.prokoudine@gmail.com), 2023

[TOC]

## About the research

### Why the FPA needs this research

The FreeCAD Project Association has sufficient funds to give grants to developers who are capable and willing to improve the program, CI, QA etc. However, as a relatively new entity, the FreeCAD Project Association doesn’t have enough experience with grant programs apart from their own participation at Google Summer of Code as a mentoring organization.

During the briefing, the following major issues were outlined:

* There have been very few grant applications so far, and the reason is unclear.
* There’s an overall impression shared by FPA members that the program could do with becoming more professional: more planning, more communication, better execution.
* There’s a certain lack of experience in how to take money and apply it with success.

Additionally, it was pointed out that the pre-existing bounties program hasn’t been very successful, nobody knows how to do it.

### Objectives

The FPA is particularly interested in answers to the following questions:

* What to do to start increasing engagement?
* How to find talent and bring them to the project?
* If people think this looks too much like work, do we want to change how it looks or do we find devs who don’t think like that?
* How do other organizations and applicants structure grants? Too specific or too open in scope? How much specificity to do? Is it like GSoC project ideas?
* Do they do small/medium/large projects?

### Scope

For the purpose of this research focus should be given to the operation of the FPA, as well as to studying best practices by other non-profit and for-profit organizations issuing grants to open-source developers.

### Deliverables

1. A research document that contains:
    1. A study of what the FPA does to communicate the program
    2. A study of what other organizations do with their grant programs
    3. Major takeaways from the research
    4. Actionable recommendations for the FPA based on the takeaways
2. A blog post summarizing key findings of the research

## Project plan

1. Do a briefing call with the FPA members
2. Identify organizations of interest: FOSS projects, foundations, and companies
3. Take a closer look at what the FPA does: grant program page, public communication etc.
4. Do a quick study of each one to see whether it qualifies for a deeper analysis
5. Study organizations that passed qualification: research publicly available information, do calls or emails with managers and applicants (where possible)
6. Identify best practices as applicable to the FreeCAD Project Association
7. Prepare and send the report that encompasses the entire work done
8. Collect feedback from all parties, improve the first revision
9. Finalize the research
10. Write a blog post

### Budget

This research is a $1,500 grant from the FreeCAD Project Association.

## What the FPA currently does with its grant program

### How the grant program is presented

According to the [FPA Development Fund](https://fpa.freecad.org/programs/fpadf-announcement) page, grant applicants are expected to come up with their own idea of a new feature, improvement, or fix, as well as provide a timeline with milestones. The page suggests to forward a grant application to any member of the FPA for consideration, but does not list any contacts nor does it provide an estimation of how long the reviewing process generally takes.

### The budget and the real spending

The FPA accumulates ca. $8K a month. The project also has infrastructure and travel expenses. Given that, the organization is prepared to spend between $50K and $75K a year on development grants and supervision.

The [Development Fund](https://fpa.freecad.org/programs/fpadf-announcement) page states:

    Grants are capped at US$5000 and will be awarded only for work on the FreeCAD code base. The cap may be raised as the FPA gains experience in the awarding of grants and as available funds allow.

So far, there have been four grants issued to three people:

* $1,000 to RealThunder
* $1,000 to Adjinkya Dahale for work on Sketcher
* $1,000 twice to Adrián Insaurralde Avalos for release management

Several more grants are at various stages of planning, all either for quality-of-life improvements or build system improvements/updates.

### How grant expenses have been estimated so far

The first two grants have been “honorary”. What it means is people were paid for doing the work they were already doing anyway, so it was more of a token of gratitude and encouragement. No project cost estimation was done.

The third and the fourth grants had a very basic estimation done by Adrián — essentially, how much time he would need to do his work.

One of the upcoming grant projects has a per-hour rate and a more sophisticated estimation of time expenses.

Another potential grant could be paid in the same “honorary” fashion to a developer who has been working on a per-document unit picker.

### How grants are being paid

So far, all payments have been done 100% upfront. The FPA is considering a switch to a more sophisticated system:

* Small projects: 50% upfront, 50% upon completion.
* Medium projects: ⅓ after initial research, ⅓ after PoC code is delivered, ⅓ after the project has been merged.
* Large projects: equal sums after each successful stage, starting with research.

### Project supervision

At the moment, there is no formal supervision over grant projects. Code submission goes through the same code review routine by the same maintainers.

The FPA members generally agree that in the future, grant projects need to be supervised, and people who do supervision need to be compensated for their time, similar to mentorship at GSoC.

At the same time, at least one FPA member voiced an opinion that the best kind of a project is one where you don’t need to supervise anybody, because the person who received the grant knows what (s)he is doing.

### How the grant program is communicated to users

This page of the blog specifically mentions grants, but can’t be accessed directly from the menu: [https://blog.freecad.org/jobs/](https://blog.freecad.org/jobs/).

The grant program announcement is available at [https://fpa.freecad.org/programs/fpadf-announcement](https://fpa.freecad.org/programs/fpadf-announcement). It is linked from just one announcement on FreeCAD’s blog: [https://blog.freecad.org/2023/01/18/wip-wednesday-18-jan-2023/](https://blog.freecad.org/2023/01/18/wip-wednesday-18-jan-2023/).

The following blog posts at freecad.org mention the grant program:

* [First FPA sponsored development](https://blog.freecad.org/2022/09/26/first-fpa-sponsored-development/) (September 2022), talks about the B-Spline project, says that the next stage is being sponsored by the FPA, invites donations, doesn’t invite more contributors to the grant program.

Additional mentions:

* Ajinkya Dahale [mentioned the FPA grant](https://forum.freecad.org/viewtopic.php?p=630610#p630610) for B-Spline development in the forum.
* Brad Collette [mentions a potential FPA grant](https://forum.freecad.org/viewtopic.php?p=693234#p693234) in the post about the hackathon in Vancouver

Very little discussion about the grant program has been found online.

### Quick summary

The overall impression is that the FPA hesitates to go big on its grant program while having sufficient funds to do so.

## What other organizations do

All organizations studied, as well as organizations in the honorary mentions list are one of the three types:

* FOSS projects
* Non-profit organizations
* For-profit companies

### QGIS

#### About the project

QGIS is a FOSS geographic information system.

#### About the grants program

This project has been running a grant program since 2016. All projects are related to hacking on QGIS code, or CI, or QA, or release procedures. They haven’t changed how the program is organized and run in 2023. The changes in 2022 were: 1) accounting for PR review in the budget estimation, 2) a short summary of proposal discussion should be submitted within a week after the discussion has taken place, this is required for voting on proposals.

#### How it’s organized

The process is described in . Every year, the team makes a public call for grant applications in the blog ([here’s 2023 announcement](https://blog.qgis.org/2023/04/04/qgis-grants-8-call-for-grant-proposals-2023/)). Applicants submit issues to a [dedicated GitHub repository](https://github.com/qgis/QGIS-Enhancement-Proposals) that explains the entire procedure and provides templates (those submissions are called QGIS Enhancement Proposals, or QEPs). The project steering committee (PSC) then reviews submissions and runs a voting process amongst QGIS.ORG voting members to select the best projects.

Example of a successful submission and, subsequently, a successful project: [https://github.com/qgis/QGIS-Enhancement-Proposals/issues/192](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/192).

#### Project ideas

The QGIS team does not provide a list of ideas.

#### Project paperwork

The progress is documented in the QGIS PSC repo, e.g. [here](https://github.com/qgis/PSC/issues/58) is the entire progress in the 2023 program. 

#### Project supervision

No supervision is provided ([source](https://blog.qgis.org/2016/08/04/qgis-grants-call-for-applications/)):

    We expect that you are already an established developer or contributor to the QGIS project and do not need any ‘hand holding’ other than via normal community consultation processes like QEP’s.

#### Scope and size of projects

QGIS doesn’t seem to have a categorization of projects into small/medium/large. However, the budget they assigned to various projects, as well as the nature of those projects, suggest that the organization welcomes projects of different size and scope. Here are the 2023 projects:

* QGIS Bug Tracker cleanup — €6,000
* Porting to C++ and harmonization of Processing algorithms — €10,000
* Add vertical CRS handling to QGIS — €20,000
* Improve test result handling on QGIS CI — €1,000

Looking at the entire lifespan of the program, their smaller projects look like this:

* Update macOS CMake bundling scripts (€1,800)
* Review process on plugins.qgis.org process and improvements (€1,200)
* Improve test results handling on QGIS CI (€1,000)

Their medium projects look like this:

* Implement a task manager for long-running background tasks (€4,500)
* Improve deep relations with Postgres editing (€6,000)
* QA methodology and infrastructure (€5,000)

And their larger projects projects look like this:

* Implement a flexible properties framework (€10,000)
* Porting to C++ and harmonization of processing algorithms (€10,000)
* Add vertical coordinate reference system handling (€20,000)

#### Payouts

There doesn’t seem to be any public information available about that.

#### Annual budget

The project alternates between 20K and 40K euro budget for grants.

<table>
  <tr>
   <td><strong>Year</strong></td>
   <td><strong># of grants</strong></td>
   <td><strong>Min project budget</strong></td>
   <td><strong>Max project budget</strong></td>
   <td><strong>Overall budget</strong></td>
  </tr>
  <tr>
   <td>2016</td>
   <td>3</td>
   <td>€4,500.00</td>
   <td>€10,000.00</td>
   <td>€20,500.00</td>
  </tr>
  <tr>
   <td>2017</td>
   <td>6</td>
   <td>€1,800.00</td>
   <td>€10,000.00</td>
   <td>€25,600.00</td>
  </tr>
  <tr>
   <td>2018</td>
   <td>7</td>
   <td>€2,500.00</td>
   <td>€7,500.00</td>
   <td>€35,500.00</td>
  </tr>
  <tr>
   <td>2019</td>
   <td>6</td>
   <td>€1,400.00</td>
   <td>€6,000.00</td>
   <td>€22,200.00</td>
  </tr>
  <tr>
   <td>2020</td>
   <td>10</td>
   <td>€2,000.00</td>
   <td>€8,000.00</td>
   <td>€40,000.00</td>
  </tr>
  <tr>
   <td>2021</td>
   <td>8</td>
   <td>€1,200.00</td>
   <td>€4,500.00</td>
   <td>€22,500.00</td>
  </tr>
  <tr>
   <td>2022</td>
   <td>4</td>
   <td>Unknown</td>
   <td>Unknown</td>
   <td>Unknown</td>
  </tr>
  <tr>
   <td>2023</td>
   <td>4</td>
   <td>€1,000.00</td>
   <td>€20,000.00</td>
   <td>€37,000.00</td>
  </tr>
</table>

#### Communication about the program

QGIS team typically makes several posts about the grants program per year: a call for grant proposals (typically, in the spring), a post announcing winning projects (typically a few months after that), a post with reports about the program (typically early next year). Examples:

* [QGIS Grants #7: Call for Grant Proposals 2022](https://blog.qgis.org/2022/01/16/qgis-grants-7-call-for-grant-proposals-2022/) (January 2022)
* [QGIS Grant Programme 2022 Results](https://blog.qgis.org/2022/03/12/qgis-grant-programme-2022-results/) (March 2022)
* [Reports from the winning grant proposals 2022](https://blog.qgis.org/2023/03/24/reports-from-the-winning-grant-proposals-2022/) (March 2023)

There is no public communication about interim results between announcement of winning projects and reports. In 2022, only one grant receiver posted reports to the project steering committee’s mailing list.

The grant program is mentioned on multiple pages on the main website (mainly in the blog), but there is no easy single “place of entry” or a dedicated page.

### GRASS GIS Student Grants

#### About the project

GRASS GIS offers powerful raster, vector, and geospatial processing engines in a single integrated software suite.

#### About the grants program

Student Grants is a stipend program for students. Funded projects can include actual coding, bug fixing, or documentation and the creation of educational resources. The program [started in 2021](https://www.mail-archive.com/grass-psc@lists.osgeo.org/msg02070.html), both participants were their 2021 GSoC students effectively continuing the work they started. 

A total of three grants have been issued so far: two in 2021 and one in 2022..

#### How it’s organized

The Project Steering Committee (PSC) updates the [Student Grants](https://grasswiki.osgeo.org/wiki/Student_Grants) page to place a call for submissions and sets a deadline, then votes for proposals.

Students can select one of the project topics [listed by the PSC](https://grasswiki.osgeo.org/wiki/Student_Grants#Topics) or suggest their own.

In 2023, selected participants are given 3 months to complete their assignment (2 months in 2021 and 2022). The start of their work is flexible.

Once the student submits their final report, the PSC votes on accepting or declining the results.

#### Project ideas

The GRASS GIS team provides a list of “topics highly relevant to the community” with a short description and requirements.

#### Project paperwork

Proposals are submitted to the GitHub issues section. Progress is reported on the mailing list, students use Trac pages to store project description and the timeline of their progress. Examples:

* [GH issue for the 2022 project](https://github.com/OSGeo/grass/issues/2017)
* [Trac page for the 2022 project](https://trac.osgeo.org/grass/wiki/wxGUIDevelopment/RedesigningStatusbar)

#### Project supervision

Similarly to GSoC, GRASS GIS provides mentoring to students who received grants.

#### Scope and size of projects

Only three students participated, all three projects were similar in scope. As the available budget is comparatively low, grants are capped at $1,000 USD (smaller grants are possible), and duration of work is now expected to be 3 months tops, there isn’t a lot of potential for larger projects. At the same time, the organization doesn’t limit the number of applications, so a student could potentially chain multiple projects as much as the budget allows.

#### Payouts

Money is paid on two rounds:

* 50% at the beginning of the work phase
* 50% after reception and approval of the final report by the PSC

#### Annual budget

GRASS GIS started with a $2,000 USD budget in 2021, upgraded it to $3,000 USD in 2022, then once again to $4,000 in 2023. The funds are provided by the [Open Source Geospatial Foundation](https://www.osgeo.org/) and people who make individual direct donations.

#### Public communication about the program

There was limited public communication in 2021 and 2022. The students were already connected to the community and did projects in the past. The 2023 program hasn’t been publicly announced yet.

**Mailing list.** There was no announcement of the 2021 program in the mailing lists. The 2022 was announced in the grass-user mailing list. Weekly reports and final reports from all the 2021 and 2022 projects were posted to grass-dev and grass-user (work completed in spring 2022 and 2023 respectively).

**Blog.** The GRASS project never announced the program in the blog, they posted two separate final reports from their 2021 students, they published no reports from their 2022 student (work was completed in spring 2023).

**Twitter.** The start of the 2021 program wasn’t announced. There’s a total of 15 tweets by the project's account mentioning the grant program, Two of them from 2022 link to the program page. Others are suggestions to donate to fund the program and links to students’ reports.

### Cesium

#### About the project

An open platform for building 3D geospatial applications. Has CesiumJS, an open-source JavaScript library for 3D globes and maps.

#### About the grants program

That grant program was started to increase engagement and use of technology in the 3D geospatial ecosystem, as well as to build a larger pool of talent around the project. None of the applicants are working on Cesium source code directly. Rather, they create/improve projects that benefit the ecosystem and/or make a social impact.

2023 is the first year they are giving grants, but they already made two rounds of grants. The program is managed by Danielle Stollak who has experience in building fellowship and outreach programs.

When asked why their program seems to be so successful so soon after its inception, Danielle Stollak responded: “We have a very large social media following, both the company’s account and our CEO’s account. That really helps”.

#### How it’s organized

Cesium is currently using a rolling model for receiving and reviewing submissions (Epic MegaGrants does it and they were an inspiration), but the company is comparatively small (48 employees at Cesium vs 9,442 employees at Epic Games as per LinkedIn) and its grants pool is 1/100 of Epic’s ($1 mln vs $100 mln). So it’s within the realm of possibility that they will eventually begin batching the collection of applications and reviewing them. They already batch announcing the winners.

A grant proposal is supposed to have a project description, a timeline with milestones, and a budget estimation. The Cesium team sets priorities in a certain way. First of all, the project has to meet their requirements. Secondly, the applicant (person or organization) need to provide sufficient proof that they are the right people to take it on. Only then the team looks at the budget estimation to see if it makes sense for the suggested scope of work.

One of the key indicators is applicant’s online presence (e.g. GitHub profile and some activity in it). If the proposal is sketchy and the applicant’s skills don’t check out, the proposal will be declined.

#### Project ideas

Cesium provides general directions and lists already successful applications, nothing beyond that.

#### Scope and size of projects

The vast majority of projects so far are scheduled to be done within 2 to 6 months, 4 months on average. So far, there has been just one project that is supposed to last a year.

Grants are anywhere between $5,000 and $50,000 for organizations and between $5,000 and $15,000 for individuals.

#### Project paperwork

Applicants are expected to submit the following:

* Project description
* Timeline and milestones
* Budget estimation

#### Project supervision

The idea is this:

* For projects that are supposed to take 2 months or less, there is no expected communication on interim progress, but developers/orgs are welcome to reach out with issues or questions.
* Projects that last 4 months or more typically have at least a few milestones, 1.5-2 months apart, communication happens at the end of each milestone.

#### Payouts

50% is paid before the start, 50% is paid after the end of the project.

#### Annual budget

The entire grant budget is $1,000,000. There is no formal annual cap, but they are keeping it tight to pick really great projects.

#### Public communication about the program

So far, Cesium’s communication is exemplary. They publicly announced the program in March, did a [webinar](https://vimeo.com/818844566) in April (175 visitors at the time, and then twice as many views on Vimeo), announced all winners in two batches, and they also regularly remind people via social media that there’s an ongoing grant program.

The program page clearly explains what the program is, has a very good FAQ, and links to a [directory of already awarded grants](https://cesium.com/cesium-ecosystem-grants/grant-directory/) to give idea what projects are considered good enough.

### Open Toolchain Foundation

#### About the project

“The Open Toolchain Foundation aims to democratize engineering, making it available to anyone who wants to design, exchange designs, or manufacture products. The Open Toolchain Foundation is initiated by members of Fab City Hamburg, HIWW [Hamburger Institut für Wertschöpfungssystematik und Wissensmanagement], and Open Source Ecology Germany.”

#### About the grants program

2023 is the first year they are giving grants, so far, they appear to have given just 5 grants, all to [various FreeCAD developers](https://opentoolchain.org/2023/02/26/FOSDEM-2023/).

#### How it’s organized

There is no open application process in place. So far, the Open Toolchain Foundation issued only grants to FreeCAD developers.

According to Pieter Hijma, the team worked with the community to identify developers who could be grant recipients. They chose this approach to cut the overhead that the usual grant application routine would otherwise impose on both themselves and developers. Some developers they contacted felt that others would benefit more from this kind of funding and referred those other developers to the Open Toolchain Foundation team.

#### Project ideas

They have no such thing.

#### Scope and size of projects

There doesn’t seem to be a distinction at play so far. All five projects were awarded the same grant, €6,000, although it looks like projects vary in complexity and scope.

#### Project paperwork

Based on quick interviews with Pierre-Louis Boyer and Yorik van Havre, the Open Toolchain Foundation and grant receivers make a 1-pager description of a project with a list of deliverables.

#### Project supervision

According to Pieter Hijma, the Open Toolchain Foundation checked the progress by grant recipients regularly, mostly by just reading public reports. They expected that little supervision would be required, because they had chosen strong community members, and this is exactly how it played out in the end.

#### Payouts

All work is post-paid.

#### Annual budget

No annual budget is ever mentioned. The cost of the FreeCAD round of grants was €30,000, that is, €6,000 per each project.

#### Public communication about the program

The Open Toolchain Foundation did a [blog post](https://opentoolchain.org/2023/02/26/FOSDEM-2023/) and a [talk](https://www.youtube.com/watch?v=SxViWgR1F3Q) at Fab City Hamburg. Pieter Hijma is also active in the FreeCAD community.

### Blender

#### About the project

Blender is a free and open-source 3D computer graphics software tool used for creating animated films, visual effects, art, 3D-printed models, motion graphics, interactive 3D applications, and virtual reality.

#### About the grants program

First off, here is the important distinction:

* There are _full-time employees_ hired directly, they are typically based in the EU.
* There are _remote employees_ who are registered as self-employed individuals in the country of their residence. They have contracts and send invoices.
* There are _grant recipients_. They receive monthly payments as a token of gratitude for continuous work on Blender.

The grant program was launched in 2011. According to Ton Roosendaal, developer grants are gifts the Foundation gives to people with as sole reason to free up their time to work on Blender. Grant recipients have no obligations, other than that the Foundation won't renew grants if they stop contributing. After a couple of years of successful work the Foundation offers the grant recipients to become remote staff or employees.

#### How it’s organized

A developer who wants to receive a grant needs to submit a request supported by at least two core developers. When an application arrives, the BF team checks with owners of the module in question and informs the admins ([see here](https://wiki.blender.org/wiki/Modules/Roles) for information about roles).

Module owners review the proposal and reach a decision. The main reason why a development grant project would not be supported is planning considerations. This is to prevent adding too much stress and burden on other people's shoulders. If there's no consensus, the admin board makes the decision.

Usually the grant starts with a 3 month trial.

#### Project ideas

Blender Foundation does not list project ideas for grants.

#### Project paperwork

There’s no public paperwork. Developers are at liberty to write blog posts or make YouTube videos about their progress.

#### Project supervision

Work coordination is usually done by [module teams](https://projects.blender.org/blender/blender/wiki/Home).

#### Scope and size of projects

There is no formal differentiation between grant projects of different scope and size, nor does it seem to matter.

#### Payouts

Payouts to grant recipients are done on a monthly basis.

#### Annual budget

According to the 2022 report, the 2022 budget for grants was €337,538.

#### Public communication about the program

Blender Foundation is very open about who they hire and for what projects. They make blog posts giving updates on changes, there’s also annual reports that list developers and provide overall expenses.

### Godot

#### About the project

The Godot Engine is a free, all-in-one, cross-platform game engine that makes it easy for you to create 2D and 3D games. The project is currently in transition from Software Freedom Conservancy to [Godot Foundation](https://godot.foundation/).

#### About the program

Including Godot into this research is arguable. They do not have a grant program per se, but their approach to hiring contractors resembles grant programs by other organizations to an extent that is hard to ignore. They are also in a unique position here, because, due to the nature of game development, their users are developers too. So they have a naturally larger pool of talent to choose from.

#### How it’s organized

The core team identifies people who already do great work for the project and asks them to spend more time on that for money. Some developers work full-time for the project, others have a part-time job with the Foundation.

#### Project ideas

There is no such thing by design.

#### Project paperwork, supervision, scope and size

Hired developers do their work with little supervision, they take ownership of the areas they contribute to and report directly to the production team. There is no public information about project paperwork or categorization of projects (smaller vs. larger).

#### Payouts

Hired developers appear to be paid a fixed amount per month.

#### Annual budget

According to [this recent post](https://godotengine.org/article/funding-breakdown-and-hiring-process/), they currently have 10 contractors (some part-time, some full-time) for a total cost of roughly $40,000 (USD) per month (or ca. $480K per year).

The Godot Foundation recently publicly launched a [development fund](https://fund.godotengine.org/) that is designed to eventually phase out their Patreon campaign, cut down intermediary fees, and generally improve the fund’s visibility.

#### Public communication about hiring devs

The Godot team admits that they rarely post information about job openings, because they don’t follow the usual hiring process ([source](https://godotengine.org/article/funding-breakdown-and-hiring-process/)):

    We typically do not make public job postings, we identify individuals who are already knowledgeable about Godot, have experience in areas that need more contributions, and work well with other contributors.

Much of the information about the hiring practice became known after a [blog post in July 2023](https://godotengine.org/article/funding-breakdown-and-hiring-process/).

### Honorary mentions

#### Google Summer of Code

While it seems like a no-brainer pick for the research, Google/Alphabet only makes the final call on slot allocations and provides funds, the rest is on mentoring organizations. So it isn’t fair to include it. At the same time, let’s give credit where credit is due: both FreeCAD, QGIS, and GRASS reflect on their experience as GSoC mentoring organizations when planning their own programs and draw from it where possible.

#### Krita Foundation

Even though Krita Foundation has paid developers and sometimes uses “grants” in their official texts, they really don’t have a grant program. Rather, they hire developers to work on specific parts of the program and pay them a salary based on a per-hour rate. However, not including Krita while including Godot is arguable as their approach to hiring is similar.

#### Python Foundation

This organization mostly provides grants for education projects and Python events such as local conferences.

#### Epic MegaGrants

[From the website](https://www.unrealengine.com/en-US/megagrants):

    Epic Games has committed to providing financial grants to creative, noteworthy, and innovative projects built in and around Unreal Engine or projects that enhance the open source 3D graphics ecosystem.

    Our average grants range from $5,000 to $250,000, with some extraordinary projects receiving up to $500,000! Projects selected cover a variety of endeavors from game development, architecture projects, and film production, to educational uses and software tool development. No matter what size grant you receive, you will continue to own your IP and will be free to publish it however you wish.

Epic supported several important FOSS projects in the past: Blender, Dust3D, IfcOpenShell, ArmorPaint, Godot.

#### NLnet Foundation

The foundation focuses on projects that contribute to an open information society and provides grants to open-source developers.

#### Prototype Fund

This is a German proxy fund that issues grants by the Federal Ministry of Education and Research to open-source developers and prioritizes civic tech, data security, data literacy and software infrastructure.

## Main takeaways from the study

### General approach to hiring talent

There are four general approaches:

* Hiring full-time or part-time developers: Blender Foundation / Institute
* Giving grants to people who are known in the community and already do great work: Godot and Cesium Ecosystem Grants (both to some extent), Blender Foundation / Institute
* Accepting grant applications from people you don’t necessarily know: QGIS
* Accepting grant applications from former GSoC students: GRASS

But when you look closer, these things become apparent:

* Only a handful of team members in Blender are random people who came out of the blue. Most are long-time contributors who had already proven their worth prior to being hired or receiving a grant. In fact, you have to be recommended by two core developers to qualify as a grant recipient.
* QGIS in particular has a strong bias towards people who already have experience hacking on the program and know what they are doing.
* The organizations that allow “random” people in also request project documentation that clearly explains the scope of the project, deliverables, and a timeline (milestones).

**Takeaway:** focus on people who have experience hacking on FreeCAD, request project proposals that clearly demonstrates that the person:

* understands the idea behind their proposal;
* can decompose future work into milestones and tasks in a sensible manner;
* can do a realistic budget estimation.

### Rolling vs batching

There is a strong bias towards batching proposal submissions and making annual runs of the grant program.

**Takeaway:** do an annual call for proposals, batch evaluation of submissions, announce winners in a single shot, allow for some flexibility for small vs medium vs large projects in terms of project completion time.

### Project ideas

Just one organization, GRASS GIS, provides a list of topics for potential grant applicants. However, even they don’t write detailed project descriptions (a-la GSoC). Organizations mostly expect applicants to be people with hands-on experience, capable of planning their own project.

**Takeaway:** list most important work you’d love to see done, possibly refer to the roadmap; give applicants enough room to demonstrate that they know what they want to do, understand the implications, can plan their own work, and do a sensible budget estimation.

### Project paperwork

Organizations mostly request a grant proposal that clearly demonstrates that the applicant understands what they are doing. The proposal is supposed to generally look like this:

* General project description
* Expected completion time
* Timeline/milestones
* List of deliverables
* Budget

**Takeaway:** adopt a similar approach.

### Project supervision

Organizations mostly expect applicants to be experienced enough to not require much supervision. Except for GRASS, mentorship is not provided except for the usual code review procedures or communication in chat rooms for developers. Developers who received grants are mostly encouraged to make regular interim reports. All organizations expect developers to submit a final report, since the final payout depends on that.

**Takeaway:** expect developers to be self-sufficient, encourage progress reports, demand final reports.

### Project categorization (scope/size)

Except for GRASS GIS who have limited funds, organizations typically allow both small, medium, and large projects even if it only shows through project descriptions and allocated budgets.

**Takeaway:** allow for small, medium, and large projects.

### Payouts

Organizations mostly pay 50% before the project and 50% after successful completion of the project.

**Takeaway:** adopt 50/50 split for pre- and post-paid for small and medium projects; for large projects, issue payments after each successful milestone, but also do a pre-payment before the first milestone and after the upfront work (planning).

### Public communication

It’s all over the place between organizations. Some are very active, some would definitely do with improving their communication. Others don’t even have a single place of entry for people willing to learn more about the program.

**Takeaway:** model your public communication on the best practices of Cesium and Blender.

## Research failures

The available sampling and specific challenges that the FreeCAD project is facing make it difficult to provide meaningful advice on how to increase the amount of grant applications. However, here are some initial considerations.

1. Organizations that have been studied typically attract experienced developers who have already been part of the community one way or another. Some are past GSoC students, e.g. both grant receivers in GRASS GIS are ones. But also Krita Foundation, which was excluded from the study, actually _employs_ former GSoC students. Having a better understanding who contributors to the project are would be really helpful. One way to approach this would be a developers survey.

2. So far, there hasn’t been much public communication about the program, the rules are not 100% clear, the direct contacts for submitting a proposal are missing, the payout is not impressive although the FPA has the funds to improve the latter. Compare “We’ve given $1,000 per project so far and will give more some time later” and “We have a $75K fund for grants, please apply here”.

So the approach to dealing with this limitation of the research would be surveying FreeCAD contributors and shaping the communication based on results of that survey.

## Recommendations

As a relatively new non-profit organization with relatively little spare resources, the FPA needs to demonstrate transparency and efficiency. Based on the takeaways, here are recommendations for the organization:

1. **Create a steering committee.** The most important consideration here is that the FPA cannot make development decisions for the FreeCAD project, thus it needs an active team of contributors (both maintainers and developers) to vote on proposals. So before you launch the program, you need to make sure that maintainers are aware of the start of the program before it’s announced, you know who you can rely on and what their conditions for participation are.

2. **Organize grants in waves.** Batch submissions, submissions review, announcement of accepted proposals. This helps planning. Start a regular wave in Q1 of 2024 (FOSDEM is a great time for announcement), allow for projects as long as 9 months, repeat next year.

3. **Manage proposal submissions in a dedicated GitHub repository.** This brings more transparency to the process.

4. **Aim for developers who know their way around FreeCAD.** An applicant should have some track record with regards to the project: either working on FreeCAD source code directly or hacking on 3rd party add-ons for the software.

5. **Request a sensible amount of prior work.** Provide general guidance for higher priority development topics, but give enough room for applicants to demonstrate their ability to study the codebase, decompose future work into smaller bits, and plan their work. Expect the applicant to submit a general project description, expected completion time, timeline/milestones, a list of deliverables, and a budget estimation.

6. **Be strict when reviewing proposals.** Drop submissions where the proposed idea is great, the developer failed to demonstrate the ability to think it through and doesn’t respond well to criticism. Keep the funds for a better project.

7. **Be flexible for project scope and size.** Allow both small, medium, and large projects. Someone with a successful small project can come back with a medium project next year, then with a large project the year after that.

8. **Do a mix of pre-paid and post-paid model.** Small/medium projects: pay 50% on start, 50% after a final report and approval from the steering committee. Large projects: divide the payment into equal sums per milestone (e.g. 25/25/25/25%), consider upfront work a milestone and do a milestone-sized payment before the start of the coding phase. 

9. **Adopt the Cesium/QGIS models for public communication** in the blog and on social media. Publicly announce the start of a wave, publicly announce winners, retweet interim progress reports, publish program recaps. Pay grant receivers a bonus for insightful blog posts at [blog.freecad.org](https://blog.freecad.org/) (the usual $100, unless you upgrade that to something more fitting for larger posts).

10. **Come up with a program name.** It doesn’t have to be fancy like Epic MegaGrants, but it needs to just be there for easy reference. Something fairly generic like “FreeCAD grant programme” should do. But if you feel like you could go fancy, by all accounts, please do.

11. **Update the [Development Fund](https://fpa.freecad.org/programs/fpadf-announcement) page.** The page should include the following information: basic information about the program, high-priority topics, status of the current wave (expecting proposals, submissions not accepted anymore this year, etc.), a quick guide to submitting a proposal, an FAQ answering questions about program organization, proposal expectations, payouts etc.

12. **Move the [blog.freecad.org/jobs/](https://blog.freecad.org/jobs/) page to fpa.freecad.org.**  Make one page at fpa.freecad.org that lists available jobs that are not necessarily grants and link to the grant program from there.

13. **Do a wave post-mortem.** The history of QGIS’s grant program suggests that they reflect on the results of the program every year and make adjustments for future waves. Adopt that and explain changes in the program as compared to the previous wave when you post an announcement in the blog.

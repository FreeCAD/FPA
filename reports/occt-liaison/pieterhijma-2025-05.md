## Summary of Activities - OCCT Liaison - May 2025

### Update the project

The [OCCT Liaison project](https://github.com/orgs/FreeCAD/projects/32/views/1?layout=table) has
received continuous updates on issues although I'm now running behind as well.

### Discussion on OCCT bug reporting and versions

Last month, I wrote that this needed follow up and I did.  Oursland writes this:

> It's not a genuine compatibility issue as some other build systems are using OCCT 7.9.0, but the conda-forge smesh still needs to be updated.

I'm still waiting for this but Adrian is now also looking into this, I believe.

### Suggest a process for a 10 year roadmap

I haven't done this, so I should still hold another meeting with a slightly
larger group of people.  I discussed this briefly with Brad now that he's
working on the FreeCAD Professional Network.  He suggested to present the OCCT
Liaison project to the FPA, which I did.

### Present the OCCT Liaison project to the FPA

I presented the project in the FPA meeting to discuss that there are so many
issues that I can't handle everything myself.  The reaction to the project page
was in general very positive.  I suggested that I could ask for a grant to
provide educational material for the community.  This was well received as well
and it was suggested to present it in the Developers Meeting and to present it
to OCCT.

### Present the OCCT Liaison project in the Developers Meeting

I presented the OCCT Liaison project in the Developers Meeting of 17 May.  [The
minutes](https://github.com/FreeCAD/FreeCAD-developer-meetings/blob/main/Minutes/minutes-2025-05-17.md#4-open-cascade-occ-liaison-update)
show that there is wide support for reporting issues more efficiently.  The
next step is to ask OCCT about it.

### Contact with Dmitrii/OCCT:

I contacted Dmitrii with various questions.  I got a positive answer where
Dmitrii is happy to see this level of collaboration between the FreeCAD and
OCCT communities.

#### The OCCT Liaison GitHub project

Positive reaction.  It is a good idea to involve the community.  Tooling and
educational material to accelerate the process is promising.  Clarity and
reproducibility are key.  There should be no FreeCAD dependencies.  DRAW
scripts that import files are also acceptable.

#### Directing resources from the FPA to OCCT

Possible.  There is a "Bug Fixing and Corrections" service.  It is
cost-effective and task-estimated where the tasks should be aligned with the
OCCT development goals.

Off-roadmap work is also possible.

Most interesting part is now the Data Exchange formats.

#### Data Exchange

Technical work mostly done, making DE plugins available: https://occt3d.com/data-exchange-formats/

Integration can go in two directions and they are happy to discuss how to integrate:
- tightly integrated
- loosely coupled

#### Roadmap for FreeCAD

Suggestions from OCCT that could benefit both OCCT and FreeCAD:
- Modernized Python bindings or a lightweight C++ interface that could help make OCCT more accessible.
- Improved modularization, bringing more third-party functionality in the OCCT
  core could improve monolithic usage and reduce external dependencies.
- Visualization, migration to WebAssembly looks promising.  This would require
  validating and improving OCCT kernel functionality to match WASM constraints
  and performance.

### DRAW Test Harness

I tried to create a test for
[#11654](https://github.com/FreeCAD/FreeCAD/issues/11654) but I failed to
complete it.  While doing this, I'm trying to learn about how to automate this
(partially), so the community can help with sorting through the issues.

### Part Design / Part interaction

I did not put this on the agenda of a Developer meeting.  I will do that for
June.

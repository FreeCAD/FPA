## Summary of Activities - OCCT Liaison - April 2025

### Contact with Dmitrii: Data Exchange

In the last report, I wrote that this needed follow up, which I haven't done
yet.  I will do that in May.

### Discussion on OCCT bug reporting and versions

Last month, I wrote that this needed follow up and I did.  Oursland writes this:

> It's not a genuine compatibility issue as some other build systems are using OCCT 7.9.0, but the conda-forge smesh still needs to be updated.

So, I'm waiting for that.

### Suggest a process for a 10 year roadmap

I've had a meeting with Brad in which we discussed the idea.  I've also had a
meeting with Hyarion and Kadet1090 on which I reported in the FPA meeting.
Some interesting points that came out of this meeting:
- It would be good if FreeCAD could work with a company that uses FreeCAD in industry.
- It would be nice to have a label "AdoptionBlocker" similar to the "Blocker"
  label for 1.0.  The new label indicates that these issues are blockers for
  widespread adoption of FreeCAD.
- Idea from Kadet1090: make a document with 100 problems for the next 10 years.
- Hold another meeting with a slightly larger group of people.

### Check forum on OCCT issues

I wrote last month that I wanted to participate on the forum.  I announced
myself there, but it was an old post.  I haven't had any reactions.

### Update the project

The [OCCT Liaison project](https://github.com/orgs/FreeCAD/projects/32/views/1?layout=table) has
received continuous updates on issues.

### Draw Test Harness

I've investigated creating Draw Test Harnesses.  I studied the Draw Test
Harness that bgbsww created in
[#9760](https://github.com/FreeCAD/FreeCAD/issues/9760).

Given the results of this study, I focused my attention to
[#10760](https://github.com/FreeCAD/FreeCAD/issues/10760), a fillet with a
crash.  I could confirm the crash.  The process was:

- make a minimal example, finding out the (in this case) two features that cause the problem
- make a Draw test case that mimics the minimal example
- verify the stack traces to confirm that the test case is indeed the same problem
- report it to OCCT ([#501](https://github.com/Open-Cascade-SAS/OCCT/issues/501).

Please note, that this was a fairly complicated test case to create.

### Part Design / Part interaction

I studied [#19702](https://github.com/FreeCAD/FreeCAD/issues/19702) and came to
the conclusion that this may be an OCCT problem, but there is also a problem
with the interaction between Part and Part Design.

I have created [#](https://github.com/FreeCAD/FreeCAD/issues/20735) for that
problem and I have raised this in the DEV meeting of 19 April.  Unfortunately,
this was a meeting without many developers, so we could not make progress on
this matter.  I will put this back on the agenda at a next meeting.

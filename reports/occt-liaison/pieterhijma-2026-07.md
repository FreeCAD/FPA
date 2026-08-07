## Summary of Activities - OCCT Liaison - July 2026

### Find a solution for an OCCT 8 regression

Last month issue [#31067](https://github.com/FreeCAD/FreeCAD/pull/31067)
reported a regression on OCCT 8.  I've investigated in direct collaboration
with OCCT and I created a PR with a workaround suggested by OCCT: [#31067
(merged)](https://github.com/FreeCAD/FreeCAD/pull/31067).  This needed
deprecation of duplicate code and I created an issue on that, see below.

### Discuss Python API Deprecation

Based on the discussion above, I've created [#31169
(closed)](https://github.com/FreeCAD/FreeCAD/issues/31169).  It turned out that
tritao had already a [PR
#30136 (merged)](https://github.com/FreeCAD/FreeCAD/pull/30136).  With the CQWG and the
help of mnescaro, we got a nice solution that tritao implemented in the PR.

### Arrange weekly OCCT Dev meeting

Together with Dmitrii, I've arranged a weekly OCCT Dev meeting in which we can
discuss issues and foster collaboration between the two projects.  OCCT
identified [candidate
issues](https://github.com/Open-Cascade-SAS/OCCT/issues?q=is%3Aissue%20state%3Aopen%20label%3A%220.%20Good%20candidate%22)
on which we can work, I documented [FreeCAD on OCCT
compilation](https://wiki.freecad.org/Compile_with_OCCT) and [creating DRAW
test harnesses](https://wiki.freecad.org/OCCT_DRAW).

We have the weekly meeting on Sunday 14:30 UTC and we had one on 19 and 26
July.

### Work on OCCT issue

To prepare for the meeting and document for FreeCAD developers I worked on
[OCCT #1363](https://github.com/Open-Cascade-SAS/OCCT/issues/1363) and
documented that in quite some detail on
[Discord](https://discord.com/channels/870877411049357352/1464258784024330372/threads/1530540221572055060).

### Request for help on fillet issues

In the meeting, it turned out that Dmitrii is working on fillets.  Instead of
me working on the above OCCT issue, he prefers to have all fillet-related
issues that we have submitted to OCCT.  Since that is much better value of my
time, I'm going to focus on that.

Since this is a good opportunity for the community to help me, I created a
[request for help](https://forum.freecad.org/viewtopic.php?p=899853#p899853) on
the forum.

### Helped out with CAM slicer improvements

I was requested to help out with
[#31056](https://github.com/FreeCAD/FreeCAD/pull/31056), reviewed [PR OCCT
#1331 (merged)](https://github.com/Open-Cascade-SAS/OCCT/pull/1331) from the author and
suggested version guards.

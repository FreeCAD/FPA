## Summary of Activities - OCCT Liaison - October 2026

### Weekly OCCT Dev meeting

We've had weekly OCCT Dev meetings on 4, 11, 18, and 25 October.

Among things that are discussed are PRs and issues brought forward by audience
members or me, the role of AI, growing number of issues and PRs, regressions.
We discussed OCCT creating an addon for FreeCAD to leverage OCCT's Data
Exchange.  We invited Chris Hennes to the meeting for the addon details.  We
discussed priorities regarding OCCT's upcoming patch release.  Since there is
lots of work on fillets, crashes are now more important to report.

### Issues with crashes

As discussed in the meetings, it is now useful to report as much as possible
crashes.  I've submitted:

- [#1684](https://github.com/Open-Cascade-SAS/OCCT/issues/1684)
- [#1688](https://github.com/Open-Cascade-SAS/OCCT/issues/1688)
- [#1691](https://github.com/Open-Cascade-SAS/OCCT/issues/1691)
  - contains 3 separate crashes and 1 case with unexpected behavior (the
    FreeCAD issue has been there for 9 years and had already been submitted to
    OCCT then).

Closed FreeCAD PRs because of fixes in OCCT:

- [#6538 (closed)](https://github.com/FreeCAD/FreeCAD/issues/6538)
  - will need to take another look because of a reproduce though
- [#18956 (closed)](https://github.com/FreeCAD/FreeCAD/issues/18956)
  - will need to take another look because of a reproduce though
- [#22580 (closed)](https://github.com/FreeCAD/FreeCAD/issues/22580)
- [#21527 (closed)](https://github.com/FreeCAD/FreeCAD/issues/21527)

Partial fixes in OCCT

- [#5642 (closed)](https://github.com/FreeCAD/FreeCAD/issues/5642)



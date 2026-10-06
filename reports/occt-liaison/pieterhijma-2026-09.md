## Summary of Activities - OCCT Liaison - September 2026

### Weekly OCCT Dev meeting

We've had weekly OCCT Dev meetings on 6, 20, and 27, September.

Among things that are discussed are PRs and issues brought forward by audience
members or me, the technical articles Dmitrii is writing, specific technical
topics such as shape fingerprints, evaluation representations, B-splines in
Sketcher and solvers, mingw compiler for Windows, implicit solids, global
variable tolerances, BRep-Graph, and the data-exchange framework.

The fillet rework is underway and triggers many parts and problems in OCCT.
More fillet issues are welcome.

### Fillet issues

As discussed in the last meeting, it is useful for Dmitrii to have as much as
possible fillet issues.  I've submitted:

- [#1568](https://github.com/Open-Cascade-SAS/OCCT/issues/1568)
- [#1569](https://github.com/Open-Cascade-SAS/OCCT/issues/1569)
- [#1570](https://github.com/Open-Cascade-SAS/OCCT/issues/1570)
- [#1571](https://github.com/Open-Cascade-SAS/OCCT/issues/1571)
- [#1576](https://github.com/Open-Cascade-SAS/OCCT/issues/1576)

Closed FreeCAD PRs because of fixes in OCCT:

- [#10760 (closed)](https://github.com/FreeCAD/FreeCAD/issues/10760)
- [#16644 (closed)](https://github.com/FreeCAD/FreeCAD/issues/16644)
- [#18078 (closed)](https://github.com/FreeCAD/FreeCAD/issues/18078)
- [#18056 (closed)](https://github.com/FreeCAD/FreeCAD/issues/18056)
- [#28828 (closed)](https://github.com/FreeCAD/FreeCAD/issues/28828)
- [#22519 (closed)](https://github.com/FreeCAD/FreeCAD/issues/22519)
- [#22386 (closed)](https://github.com/FreeCAD/FreeCAD/issues/22386)
- [#23484 (closed)](https://github.com/FreeCAD/FreeCAD/issues/23484)
- [#25146 (closed)](https://github.com/FreeCAD/FreeCAD/issues/25146)
- [#31396 (closed)](https://github.com/FreeCAD/FreeCAD/issues/31396)


### Adapt FreeCAD to OCCT 8.1-dev

As reported last month, FreeCAD didn't compile with OCCT 8.1-dev.  This has
been mostly fixed but small issues still persist.  I created a [PR #33062
(draft)](https://github.com/FreeCAD/FreeCAD/pull/33062) with a small set of
changes that are still necessary.  I don't think this PR needs to be merged.
When 8.1 is released (targeted January), most likely FreeCAD simply compiles
with it.



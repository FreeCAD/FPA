## Activity Report 1

### Week 1

This week was spent simultaneously ramping up and executing several pull requests as well as generating some process documentation.  Tests were written for methods transferred from the RealThunder TopoNaming branch. Work completed included:

* [#12138](https://github.com/FreeCAD/FreeCAD/pull/12138) Toponaming: FeaturePartCommon *merged*
* [#12137](https://github.com/FreeCAD/FreeCAD/pull/12137) Toponaming: Add helper methods *merged*
* [#12134](https://github.com/FreeCAD/FreeCAD/pull/12134) Toponaming: makeElementShape transfer and tests *opened*
* [#12098](https://github.com/FreeCAD/FreeCAD/pull/12098) Tweak resetElementMap to default to empty defined element map *merged*
* [#12087](https://github.com/FreeCAD/FreeCAD/pull/12087) Toponaming makeElementShell *merged*
* [#12086](https://github.com/FreeCAD/FreeCAD/pull/12086) Toponaming: makeElementBoolean *opened*
* [#12028](https://github.com/FreeCAD/FreeCAD/pull/12028) Toponaming move makEFace as makeElementFace and dependencies *merged*
* Started [log of issues and discoveries](https://github.com/FreeCAD/DevelopersHandbook/issues/92)
* Team communications and assistance on the Telegram chat

Most of the work was very much the underwater portion of an iceberg.  While only one actual python / Gui level feature was transferred, the bulk of the support work will apply to other features as well.

Next week should see multiple other features with new tests transferred onto the main branch.

### Week 2

This week was spent cleaning up and adding tests, and dependencies necessary to complete more of the high level FeatureX cards in week 3.  Also raising the level of PRs to minimize review feedback.  There is still more work to go on this.  Work completed included:

* [#12249](https://github.com/FreeCAD/FreeCAD/pull/12249) ( partial dup, cleaner API) Ensure that resetElementMap results in an element map existing, unless overridden *merged*
* [#12247](https://github.com/FreeCAD/FreeCAD/pull/12247) Stop tests from leaving files around after execution *opened*
* [#12237](https://github.com/FreeCAD/FreeCAD/pull/12237) Transfer in makeElementRefine *opened*
* [#12229](https://github.com/FreeCAD/FreeCAD/pull/12229) Transfer in Geometry.x changes from RT branch *merged*
* [#12201](https://github.com/FreeCAD/FreeCAD/pull/12201) Toponaming: transfer in getElementName and dependencies	*opened*
* [#12134](https://github.com/FreeCAD/FreeCAD/pull/12134) Toponaming: makeElementShape transfer and tests *merged*
* Pending work on a comprehensive tutorial test ( currently in [#12201](https://github.com/FreeCAD/FreeCAD/pull/12201) )
* Pending work on a performance test script

Next week is about pushing as many of those cards along as I can.

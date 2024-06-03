## Activity Report 1

All remaining code that was known at the time of this proposal has been moved, including everything in Mod/Part/App and Mod/PartDesign/App.  It turned out that the code in in Mod/PartDesign/App in the toponaming branch was incomplete and incorrect, and so extensive time was spent in moving code from the LinkStage3 code base instead; this process was more difficult as it required disambiguating toponaming mitigation code and the substantial feature changes that were in place.

I also built code to performance test and profile the application; this can be seen in Tools/profile.  Runs against a test corpus of 100 files revealed very little performance difference with the TNP mitigation code in place.

The TNP mitigation code is now on by default in the codebase, and some of the bugs have been addressed; a quick summary would be that there are still issues to be resolved with subshapebinders and certain sketches.

However, the work for this grant is long complete, and in fact some of the bugfixing has strayed beyond the allocated time.

PRs completed related to this proposal are:

* [#14243](https://github.com/FreeCAD/FreeCAD/pull/14243) Toponaming use mapped index to find shape. fix #14194  *merged*
* [#14202](https://github.com/FreeCAD/FreeCAD/pull/14202) Toponaming fix sub shape binder and restore multishape tests  *merged*
* [#14178](https://github.com/FreeCAD/FreeCAD/pull/14178) Toponaming: Cleanup verified face calls  *merged*
* [#14169](https://github.com/FreeCAD/FreeCAD/pull/14169) Toponaming: replace MultiFuse implementation to fix face colors  *merged*
* [#14136](https://github.com/FreeCAD/FreeCAD/pull/14136) Toponaming: adjust tests  *merged*
* [#14100](https://github.com/FreeCAD/FreeCAD/pull/14100) Toponaming: Minor test tweaks, and small fixes to pass tests  *merged*
* [#14071](https://github.com/FreeCAD/FreeCAD/pull/14071) Toponaming: Simplify offset tests  *merged*
* [#14045](https://github.com/FreeCAD/FreeCAD/pull/14045) Toponaming: Fix point crash bug #13910  *merged*
* [#14035](https://github.com/FreeCAD/FreeCAD/pull/14035) Toponaming: Bring in Chamfer, Fillet code and add tests  *merged*
* [#13966](https://github.com/FreeCAD/FreeCAD/pull/13966) Toponaming: Missing code fragments in Sketcher  *merged*
* [#13965](https://github.com/FreeCAD/FreeCAD/pull/13965) Toponaming: Add missing code fragments in PartDesign  *merged*
* [#13964](https://github.com/FreeCAD/FreeCAD/pull/13964) Toponaming Add missing code elements in Part  *merged*
* [#13963](https://github.com/FreeCAD/FreeCAD/pull/13963) Toponaming: missing code bits in App  *merged*
* [#13962](https://github.com/FreeCAD/FreeCAD/pull/13962) Toponaming: Rework makeElementChamfer to match current parms, and add PartDesign …  *merged*
* [#13917](https://github.com/FreeCAD/FreeCAD/pull/13917) Toponaming: Support saving the tnp recalculated file in profile testing  *merged*
* [#13870](https://github.com/FreeCAD/FreeCAD/pull/13870) Fix #13858  *merged*
* [#13867](https://github.com/FreeCAD/FreeCAD/pull/13867) Toponaming/Part: Fix fillet/pad bug, add tests  *merged*
* [#13860](https://github.com/FreeCAD/FreeCAD/pull/13860) Update ToolBarManager.cpp for QT 6.7  *merged*
* [#13800](https://github.com/FreeCAD/FreeCAD/pull/13800) Toponaming: performance testing  *merged*
* [#13799](https://github.com/FreeCAD/FreeCAD/pull/13799) Toponaming: merge in revolution code  *merged*
* [#13773](https://github.com/FreeCAD/FreeCAD/pull/13773) Toponaming: Add toponaming missing methods in app  *merged*
* [#13651](https://github.com/FreeCAD/FreeCAD/pull/13651) Toponaming/Part: Fix all getBaseTopoShape calls. Tests and missing c…  *merged*
* [#13582](https://github.com/FreeCAD/FreeCAD/pull/13582) Ensure we set up a valid sketch even with invalid external references  *merged*
* [#13486](https://github.com/FreeCAD/FreeCAD/pull/13486) Toponaming/Part: Fix hashing, hasher mismatches, and adjust test results to match  *merged*
* [#13447](https://github.com/FreeCAD/FreeCAD/pull/13447) Toponaming/Part: Initialize the hasher so that it operates  *merged*
* [#13411](https://github.com/FreeCAD/FreeCAD/pull/13411) Toponaming/Part: feature dressup and transform  *merged*
* [#13401](https://github.com/FreeCAD/FreeCAD/pull/13401) Toponaming/Part: Enhance testing for primitive features  *merged*
* [#13394](https://github.com/FreeCAD/FreeCAD/pull/13394) Have grbl_post not write - file just like other postprocessors  *merged*  Technically not TNP, but affected workflow.
* [#13387](https://github.com/FreeCAD/FreeCAD/pull/13387) Toponaming/Part Transfer more python ElementMapVersion and add feature pad testing  *merged*
* [#13374](https://github.com/FreeCAD/FreeCAD/pull/13374) Toponaming/Part: Upgrade Part Design tests  *merged*
* [#13354](https://github.com/FreeCAD/FreeCAD/pull/13354) Toponaming/Part transfer in part design dependencies  *merged*
* [#13285](https://github.com/FreeCAD/FreeCAD/pull/13285) Toponaming/Part FeatureDressup and FeatureTransformed  *merged*
* [#13283](https://github.com/FreeCAD/FreeCAD/pull/13283) Toponaming/Part: move in shape binder  *merged*
* [#13263](https://github.com/FreeCAD/FreeCAD/pull/13263) Rewrite PropertyTopoShape::getShape to fix dangling reference  *merged*
* [#13258](https://github.com/FreeCAD/FreeCAD/pull/13258) Toponaming/Part feature sketch based  *merged*
* [#13233](https://github.com/FreeCAD/FreeCAD/pull/13233) Add an initial test to show TNP  *merged*
* [#13197](https://github.com/FreeCAD/FreeCAD/pull/13197) Toponaming/Part: move in AppPartPy  *merged*
* [#13196](https://github.com/FreeCAD/FreeCAD/pull/13196) Toponaming/Part move in PyImps  *merged*
* [#13195](https://github.com/FreeCAD/FreeCAD/pull/13195) Toponaming/Part: TopoShapePyImp and dependencies move  *merged*
* [#13184](https://github.com/FreeCAD/FreeCAD/pull/13184) Toponaming/Part: Bug fix for #13169 while we sort out required sketcher changes.  *merged*
* [#13156](https://github.com/FreeCAD/FreeCAD/pull/13156) Toponaming/Part: move ToposhapePyImp get methods into place  *merged*
* [#13126](https://github.com/FreeCAD/FreeCAD/pull/13126) Toponaming/Part: Fix elementMatch to use full clause and be deterministic  *merged*
* [#13101](https://github.com/FreeCAD/FreeCAD/pull/13101) Toponaming/Part: Additional testing for attacher  *merged*
* [#13096](https://github.com/FreeCAD/FreeCAD/pull/13096) Toponaming/Part Bring in Python layer for ComplexGeoData  *merged*
* [#13084](https://github.com/FreeCAD/FreeCAD/pull/13084) Toponaming/Part: Move sketcher override of getElementName over  *merged*
* [#13082](https://github.com/FreeCAD/FreeCAD/pull/13082) Toponaming/Part: Move missed attacher code into place  *merged*
* [#13054](https://github.com/FreeCAD/FreeCAD/pull/13054) Toponaming/Part: Add c++ testing framework for PartDesign, ShapeBinder  *merged*


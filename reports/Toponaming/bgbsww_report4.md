## Activity Report 4

The majority of the c++ code, and all of it within the Part directory appears to be moved.

There is a small amount of remaining work for items in the Sketcher and PartDesign that need to be made element aware, and then the Python layer interface left to go. 
### Week 7
* [#12804](https://github.com/FreeCAD/FreeCAD/pull/12804) Toponaming/Part: methods in part feature and dependencies for correct elementMaps   *opened*
* [#12750](https://github.com/FreeCAD/FreeCAD/pull/12750) Toponaming/Part element cache extras  *merged*
* [#12726](https://github.com/FreeCAD/FreeCAD/pull/12726) 
Toponaming/Part: Correct elementsMatch to test all entries 
*merged*

### Week 8
* [#13030](https://github.com/FreeCAD/FreeCAD/pull/13030)  Toponaming/Part Move in feature extrusion *opened in draft*
* [#12982](https://github.com/FreeCAD/FreeCAD/pull/12982) Toponaming/Part feature mirroring and offset *opened*
* [#12957](https://github.com/FreeCAD/FreeCAD/pull/12957) Toponaming/Part make element offset *opened*
* [#12943](https://github.com/FreeCAD/FreeCAD/pull/12943) Toponaming/part features chamfer, fillet; dependencies and test updates  *opened*
* [#12885](https://github.com/FreeCAD/FreeCAD/pull/12885) Toponaming/Part: Bring over attacher differences  Toponaming  *merged*

This completes the time commitment.  The remaining known open pieces of pure c++ code to transfer include the code outside of the Part directory referenced in tickets #10398 through #10402.  Subsequently the python interface layer ( transferring c++ code and ensuring appropriate tests at the python layer ) needs to be completed.  All work to date has been tested with the FC_USE_TNP_FIX #define both off and on, so there should be no initial problems with switching it on, although there will certainly be bugs to stamp out.

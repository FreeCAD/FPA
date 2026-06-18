## Summary of Activities - OCCT Liaison - May 2026

### OCCT 8 Release

This month, most of the effort went into the OCCT 8 release:
- Prepare [#25502 (merged)](https://github.com/FreeCAD/FreeCAD/pull/25502)
  - Fix small things
  - Split the commits (per module) into:
	- logic that works both for OCCT 7 and 8
	- logic that works only for OCCT 8 (with guards)
  - Incorporate feedback from OCCT on deprecated API usage
- Provide feedback to OCCT on FreeCAD on the new release regarding porting issues.
  - Resulted in [OCCT #1268](https://github.com/Open-Cascade-SAS/OCCT/pull/1268).
- Performance comparison for OCCT of FreeCAD between OCCT 7 and 8.
- Debugged failing tests together with OCCT.
  - Tests ported to OCCT.
  - Note: `BUILD_RELEASE_DISABLE_EXCEPTIONS` needs to be `OFF` in CMake.
- Verified [OCCT #1269](https://github.com/Open-Cascade-SAS/OCCT/pull/1269) on FreeCAD for OCCT.

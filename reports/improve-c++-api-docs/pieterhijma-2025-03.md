## Summary of Activities - Improve C++ API Documentation - March 2025

I have picked up this project again in March.  I'm still waiting for DrLite to
join the effort and to collaborate, but DrLite is busy with other things.  I
don't want to postpone any longer, so I'm simply moving forward, tagging DrLite
if it is related to the other project.

Issues/PRs:

### Umbrella Issue: [Doc] Quality of C++ API documentation of package App is lacking

For the work in this month, I could define concrete issues and related PRs, but
in the next stage I will improve the documentation of various files.  For that
stage it does not make sense to create separate issues.  Because of this, I
created this umbrella issue to relate all those PRs.

- [Issue](https://github.com/FreeCAD/FreeCAD/issues/20503)

### Old version of Doxygen

The configuration uses an old Doxygen.  This required some discussion, but
since I'm currently the only one working on it, it makes sense to update
doxygen to my version.

- [Issue (closed)](https://github.com/FreeCAD/FreeCAD/issues/20365)
- [PR (merged)](https://github.com/FreeCAD/FreeCAD/pull/20474)

### Structural Doxygen warnings

These are warnings that are not about documentation but about incorrect
nesting, issues that prevent the documentatoin to render properly.

- [Issue (closed)](https://github.com/FreeCAD/FreeCAD/issues/20366)
- [PR (merged)](https://github.com/FreeCAD/FreeCAD/pull/20428)

### Restructure topics/modules for App

Topics or called modules in old versions (things that are created by the
`group` command) are highly inconsistent in general.  Solving it for all of the
documentation is out of scope for this project, but it was solved for the `App`
namespace.

- [Issue (still open for anything other than `App`](https://github.com/FreeCAD/FreeCAD/issues/20438)
- [PR (merged)](https://github.com/FreeCAD/FreeCAD/pull/20484)

### CMake issues for generating documentation

Regenerating the documentation has issues that need to be solved.  The issue
and PR need a bit of discussion but there are no real blockers for merging.

- [issue](https://github.com/FreeCAD/FreeCAD/issues/20478)
- [pr](https://github.com/FreeCAD/FreeCAD/pull/20479)


## Summary of Activities - Improve C++ API Documentation - April 2025

### CMake issues for generating documentation

Last month, I created the PR below which was still open.  This has been merged
now and needed some fixing as well.

- [#20479 (merged)](https://github.com/FreeCAD/FreeCAD/pull/20479)
- [#20709 (merged)](https://github.com/FreeCAD/FreeCAD/pull/20709)

### Fixing unassociated doc strings

Some doc strings were not associated with a specific piece of code and would
appear randomly:

- [#20737 (merged)](https://github.com/FreeCAD/FreeCAD/pull/20737)

### PropertyContainer

The documentation of PropertyContainer was improved.  Based on community
feedback on the forum, I changed the assignment of this project slightly.  I
defined the project as having the scope by just fixing the doc comments of
classes, functions, etc.  However, it was clear that the community wanted to
have improved overview texts as well, that would provide developers context.
So, I decided that I will not document all of the App package, but just the
most important things but I will add overview texts as well.  For this work, I
created such an overview text for the Property Framework where the most
important object is PropertyContainer.  This came in two PRs:

- [#20781 (merged)](https://github.com/FreeCAD/FreeCAD/pull/20781)
- [#21065 (merged)](https://github.com/FreeCAD/FreeCAD/pull/21065)

### Discussion on how to document

Based on the above PR, a [discussion on
Discord](https://discord.com/channels/870877411049357352/1354091480393842799)
was started to establish how documentation can be done in FreeCAD.  This can
eventually lead to guidelines in the developer guide.

### Property

I've started working on improving the documentation of Property but this is not
yet finished.

### ObjectIdentifier

The same is true for ObjectIdentifier.





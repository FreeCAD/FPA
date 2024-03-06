## Activity Report 3

### Week 1

This week I worked on tasks related to flushElementMap and resetElementMap.

Most of the time was used to write tests, check differences between RT fork and main both within the codebase and the outputs generated.

Work completed included:

* [#12471](https://github.com/FreeCAD/FreeCAD/pull/12471) Part/Toponaming: Tests for flushElementMap and resetElementMap *in progress*
* [#12595](https://github.com/FreeCAD/FreeCAD/pull/12535) Part/Toponaming: Transfer WireJoiner *opened*

Next week I will focus on completing this tasks and then move back to the transfer of WireJoiner.

### Week 2

This week I worked on finishing the tasks related to flushElementMap and resetElementMap, then continued the transfer of WireJoiner and its dependencies.

During the transfer of WireJoiner I found a method of Part::Feature, create(), that needed to be transfered and led to the opening of a new PR.

Work completed included:

* [#12471](https://github.com/FreeCAD/FreeCAD/pull/12471) Part/Toponaming: Tests for flushElementMap and resetElementMap *merged*
* [#12595](https://github.com/FreeCAD/FreeCAD/pull/12535) Part/Toponaming: Transfer WireJoiner *in progress*
* [#12694](https://github.com/FreeCAD/FreeCAD/pull/12694) Part/Toponaming: Transfer Part::Feature::create() *opened*

Next week I will continue the transfer of WireJoiner and other Toponaming code, as well as applying modifications for Part::Feature::create() if needed.

## Activity Report 2

### Week 1

This week I worked mostly on finishing the transfer of makeElementWires.

It's tests are still work in progress because during their implementation I found various missing tests that caused the opening of other PRs.

For those PRs I needed to learn several OCCT concepts (History management, Shape Healing process) and this took me the second part of the week. 

Work completed included:

* [#12098](https://github.com/FreeCAD/FreeCAD/pull/12189) Toponaming: makeElementWires *merged*

Next week will focus on the remaining tests/dependencies for makeElementWires.

### Week 2

This week I worked mostly on finishing the tests for MapperHistory.

After that I started importing the logics for flushElementMap and resetElementMap and related tests, still work in progress as there are other methods that need to be aligned to the equivalents of RT branch  

Also, during these developments I found another class, WireJoiner, that needs to be transfered and will lead to a new PR.

Work completed included:

* [#12402](https://github.com/FreeCAD/FreeCAD/pull/12402) Toponaming: tests for MapperHistory *merged*
* [#12471](https://github.com/FreeCAD/FreeCAD/pull/12471) Toponaming: Transfer flushElementMap and resetElementMap *opened*

Next week is about finishing the tests for flushElementMap and makeElementWires, importing WireJoiner and other Toponaming methods.

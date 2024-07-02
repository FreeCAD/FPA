# Creation of furniture and parametric components

FPA Grant to Francisco Rosa

## Report 1, 2024/07/02

This first report covers three subjects: procedures acquired, problems not yet resolved and next steps.

## 1. Purchased procedures

For the development of the first components, doors and windows, it was decided to create a single file that covered most types, instead of several individual ones. This made it a little difficult to start the work due to the need for greater planning to foresee all the necessary elements and how they would be articulated and parameterized together. However, the effort and work required produced positive results, as knowledge was acquired and some procedures were developed that will help and facilitate the development of other intended future components. These gains were then recorded and transformed into scripts, forming part of the final file created.

To obtain faster and more efficient parameterization, we tried to use formulas based on the relationships between the dimensions of the parts. Displacements of the profiles, sketches or bases of the objects were avoided, always keeping them at the origin of the coordinate system, only adjusting the resulting objects as necessary. The use of sketches based on or designed from others was also avoided, that is, any necessary changes to one of them will not result in chain changes and edits to others in the worked file..

Finally, we avoided as much as possible that possible changes in dimensions during parameterization would compromise the geometric stability of the sketches, for this reason we chose to use pre-established profiles whenever possible or applicable. This strategy also expanded the possibilities for including new external profiles whenever necessary.

It will be necessary to carry out even more usage tests, but apparently the parameterizations are proceeding smoothly without major problems or destruction of the bases (sketches) of the constructive elements of the desired final set.

Another point to highlight was the use of hierarchical visualization through the application of combined formulas of boolean properties, using multiplications of the visualization options in the content of the object expressions.

## 2. Problems not yet resolved

It was not possible to use an automation mechanism for 2D projections (sections, plans, and views). It would be necessary to achieve a link between the visualization options and the generation of projections, so when configuring the elements visualized in 3D, their corresponding 2D projections also would be produced.

Concerning the quantitative memorial and other information, it would be interesting for the text to update the materials and dimensions of the parts automatically and parametrically, as their data changes, as occurs when using isolated cells in the spreadsheet. I leave this question: would it be possible to combine formulas and strings in the same cell?

For improving the properties' elaboration, and thinking about translations and constant modifications of object characteristics, it would be good to expand its capabilities with the inclusion of independent strings to include other languages, as well as creating the possibility of editing them at any time.

## 3. Next steps

With the learning acquired and once the procedures for creating files for parametric components for FreeCAD have been established, greater ease and speed in creating the other intended elements is expected. For example, to create the next component, “Windows”, many parts of the “Doors” file created will certainly be reused. I would like to take this opportunity to note that the spreadsheet with the quantities and memorial of the file delivered is partially prepared and must be completed in the final phase scheduled for a general review of the work prepared.

# Creation of furniture and parametric components

FPA Grant to Francisco Rosa

## Report 2, 08/06/2024

In this second report on the development of parametric components, we present a summary of the work carried out, a brief description of the procedures adopted, the next steps and some comments.

## 1. Work carried out

We continued the development of the unified file for doors and windows, complementing the latter, including the configuration of materials among the properties of the components.

The objective was to cover the most common types of windows, such as those with sliding panels, sashes, conventionals, tiltings, among others, as well as panels with shutters.

Some rendered images and videos demonstrating the use of the developed configurations were posted at https://github.com/Francisco-Rosa/Recently-created-FCStd-models.

Next, we began reviewing some components developed years ago in the HVAC area, specifically, air conditioning ducts, so that they meet the parametric prerogatives of this work.

So, in addition to the parametric 3D elements of the component, each file contains a spreadsheet (with a brief report and the main data of the component) and a sheet with pre-established drawings, both with their respective updateable and editable data. These three elements provided, 3D CAD, spreadsheet and technical drawings, cannot be seen as final documents, but rather a base that can be adapted parametrically according to the needs of the project to be developed.

As a small additional improvement, we have included expressions in the report that allow it to be updated automatically, as intended.

The revised types were organized into seven groups according to their shapes, circular, oval, rectangular, as well as the combination between them, circular-oval, rectangular-circular and rectangular-oval, these in turn subdivided into two, linear, curved and finally flexible, constituting 13 components.

The application of these components in projects made through the FreeCAD library was maintained (there are videos that show this).

The files created were posted in a branch of the main FreeCAD library (https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/HVAC/Ducts), awaiting any necessary revisions, after which they can be merged into the main library. The posts are accompanied by three videos demonstrating the application of the components in an example of a duct network.

We believe that including tutorial videos in the library will encourage users to adopt the components available there, although these videos can and should be improved.

## 2. Procedures adopted

The four main procedural elements were:

• Implementation of property windows to manage the parameterization;

• Arrangement of expressions to control the geometry of the created components;

• Use of Attachment of the object properties, allowing any subsequent adjustments to the positions, angles, and dimensions of objects;

• Parametric objects structured by their axes.

Unlike the strategy previously adopted to create the file for doors and windows, a single file for several derived types, the conventional strategy was adopted for HVAC components, that is, one file per each type. We believe that in this case, it is more suited to the characteristics of this field of design.

Therefore, we sought to reproduce the process of preparing ducts network designs that are structured primarily around the creation of distribution of its axes throughout buildings. So, the parameterization of each element, in this case each duct, should follow this same reasoning and begin with its respective axes. For this, we used the resources offered by the FreeCAD object properties *Attachment*, in addition to the expressions and formulas already used.

In this way, interchangeable axes support the duct profiles. The process is carried out by mapping these profiles using the *InertialCS* or *NormalToEdge* options. Basically, this allows the constructed component to automatically adapt to the new designated axis, relative to the position, rotation and length variables, leaving only the adjustments of some of its dimensions (diameters, widths, and heights).

The use of these resources even allowed the mirroring of parts, something that is widely used and useful, without the need to specify planes or axes for this, simply including a boolean property for this (fantastic!).

## 3. Comments and next steps

We cannot fail to highlight the great resources offered by the application of expressions in FreeCAD, generating expressive results using only what is available to users.

Without a doubt, the search for solutions took a significant amount of time, sometimes longer than the time it took to create the files themselves.

We should also point that the subtraction of solids (boolean operation *Cut*) was used to create thickness in the parts instead of the *Part_Thickness* or *PartDesign_Thickness* tools that are more suitable for this. Unfortunately they were unable to remain stable during the changes made to the ducts.

As next steps, we plan to develop components for kitchens and bedrooms, such as parametric kitchen cabinet and wardrobes, initially using the strategy of single parametric files.

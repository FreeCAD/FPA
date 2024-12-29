# Creation of furniture and parametric components
## FPA Grant to Francisco Rosa
## Report 5, 12/28/2024

In this fifth report on the development of parametric components, we present a summary of the work carried out and the results obtained.

## 1. Work carried out

As planned, a final general review of the components developed was done. This basically consisted of the following tasks:

* Replacing the application of properties based on *Part::Feature* for the new *App::VarSet*;
* Replacing the materials based on the Render Workbench with those present in the internal body of FreeCAD;
* Modifying the expressions in the application of the *PathArray* tool, inserting compensatory values ​​for *End Offset*. This should have supposedly eliminated the message *“End Offset too large for path length minus Start Offset. Using zero instead.”*, however, it continues to appear when using a repetition in the tool, and we are still waiting for a correction by its developers according to a post on the FC Forum (https://forum.freecad.org/viewtopic.php?t=91517&hilit=PathArray);
* Because of this, when reviewing the Doors and Windows file, it was decided to maintain the adoption of the *Draft_Array* tool, which required finding a solution to anchor this tool to the base Sketch, obtained through another Sketch, this time in the XY plane;
* Attachment of the *Arch_SectionPlanes* to the basic Sketches of the components through the use of the *Part_EditAttachment* tool, through which they move and rotate with the other elements;
* Necessary updates to the component guides and their macros;
* Implementation of two new macros, one to obtain the component configurations previously saved in a spreadsheet and another to insert the new ones.

Without a doubt, the most work was focused on reworking the complex Doors and Windows component, which included the following new features:

* Redesign of object dependencies so that the main parts of the component are based on flat profiles, which can also be parameterized. However, the possibility of using fixed standard profiles was maintained;
* The broad application of *PropertyEnumeration* was introduced for selecting materials, profiles, or even sets of objects that are part of a larger structure, such as the internal panels of doors and windows or even the choice of hardware;
* As mentioned, macros were created to manage the various models derived from this complex file. The use of these macros can be extended to other components, through adjustments to their properties, similar to those made in the Doors and Windows component;
* As expected, this component was completely restructured to be anchored to a base Sketch like the others, but in this case it was challenging and laborious. Therefore, doors and windows can be inserted directly into projects in their final positions if necessary or desired, and it is no longer mandatory to create links, clones or copies for this purpose.
* A very useful feature when inserting doors and windows into their respective host walls is the constant need to rotate them 180° or invert their positions in the wall voids. To allow this, the aforementioned anchoring to a base Sketch has become essential.

As described in previous reports, each file contains: sets of its configurable properties; a base for moving and rotating the component; previously established sections that allow the generation of the main projections; the elements that compose them; a spreadsheet (with a brief report and main data of the component); instructions on how to create a new component and how to configure the existing one; some models saved through macros or spreadsheets and some materials previously configured for application.

The revised files have been updated in a branch of the main FreeCAD library, which can be merged into the main one. Their locations are:

* Bathroom_cabinet_sink.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Bathroom

* Bedroom_closet.FCStd
* Beds.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Bedroom

* Doors_windows_module_01.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Doors_Windows

* Kitchen_cabinet_base.FCStd
* Kitchen_cabinet_sink.FCStd
* Kitchen_cabinet_superior.FCStd
* Kitchen_cabinet_vertical.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Kitchen

* Chair.FCStd	
* Living_room_cabinet.FCStd
* Rectangular_center_table.FCStd
* Rectangular_tables.FCStd	
* Sideboard.FCStd
* Sofa_Armchair.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Living%20room

* Duct_curved_circular_complete.FCStd
* Duct_linear_circular_complete.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/HVAC/Ducts/Circular

* Duct_curved_circular_oval_complete.FCStd
* Duct_linear_circular_oval_complete.FCStd	
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/HVAC/Ducts/Circular_oval	

* Duct_flex_complete.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/HVAC/Ducts/Flex

* Duct_curved_oval_complete.FCStd
* Duct_linear_oval_complete.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/HVAC/Ducts/Oval

* Duct_curved_rectangular_complete.FCStd
* Duct_linear_rectangular_complete.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/HVAC/Ducts/Rectangular

* Duct_curved_rectangular_circular_complete.FCStd
* Duct_linear_rectangular_circular_complete.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/HVAC/Ducts/Rectangular_circular

* Duct_curved_rectangular_oval_complete.FCStd
* Duct_linear_rectangular_oval_complete.FCStd
* * https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/HVAC/Ducts/Rectangular_oval


## 2. Results obtained

First, it is important to review the points that we plan to resolve in this final stage, in which most of the solutions were achieved, leaving a few for future approximation:

* *ShapeColor*: the change in the adopted materials allows the automatic update of their basic colors, however, we noticed that this internal resource is not yet fully functional in  FreeCAD;

* *Translations*: unfortunately, there was no time to implement this resource. The idea of using a macro for this still seems feasible, in which the translated strings would be collected, creating a new set of properties for the selected language, which in turn would control the original of the component;

* *Macros*: The new ones were created to adapt to the changing of the names as the component is inserted into the project. As a method, and similar to the previous point, a spreadsheet was used to store the properties of the components, allowing them to be saved and retrieved when necessary. However, for the simpler components, the previous macros based on simple text containing the list of properties were also maintained.

* *PropertyEnumeration*: although it initially seemed very basic, the implementation of this property required a lot of work, including the creation of new sets of properties for its use, to avoid the numerous and constant *"Cyclic references to..."*. In addition, it required the prior existence of two properties for its application (*PropertyLink* and *PropertyLinkList*), that is, it caused an increase in the number of properties. Because of this, it was decided to restrict its application to the Doors and Windows component.

As planned, the fifth stage involved the necessary general review of the components, mainly the one related to the doors and windows. We have also prepared macros so that the "Doors_windows_module_01.FCStd" file can generate parametric models, capable of creating at least 20 different types, not counting their numerous derivations.

However, as important as the number of components is the method and the way in which these components were constructed. They allow their use and improvement for the widespread creation of new parametric elements in the various areas of architecture, engineering, design, carpentry, education, among many others.

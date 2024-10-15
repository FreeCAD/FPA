# Creation of furniture and parametric components

## FPA Grant to Francisco Rosa

## Report 4, 10/15/2024

In this fourth report on the development of parametric components, we once again present a summary of the work carried out, a brief description of the procedures adopted and the next steps.

## 1. Work carried out

We continued the development of individualized files for kitchen, living room and bedroom cabinets. Components for tables, chairs, beds, sofas, and armchairs were also created and we began the general review of windows with the redesign of the conventional type.

This review consisted of restructuring the *Attachments* to be based on a vertical sketch with the dimensions of the opening. With this, it is possible to move and rotate (on the three axes) the component so that it can be inserted into the project wall, whatever the position. It was also possible to include the possibility of leaving the window panels open at any specified angle. Finally, to facilitate its adaptation to the final positioning in the project, it is also possible to mirror the entire window on the wall, a very useful and necessary feature, without a doubt.

Another widely included feature was the possibility of configuring the profiles of all the parts that make up the window. The profiles can also be parameterized, in addition to the option of adopting “fixed” standard profiles.

Therefore, window insertions, through the FreeCAD library in projects, can be carried out directly, without the need to create clones, copies or links, but leaving them as valid options.

Once again, some rendered images were posted demonstrating the results of the configurations created.

At this stage, it was possible to extend the possibility of creating macros that automate the generation of the different options, with this the user can quickly obtain a specific configuration of the component, without the need to adjust the properties one by one, in addition to being able to save the ones that will be used most in their projects.

As previously done, each file contains: a set of its main configurable properties; a base for moving and rotating the component; previously established sections that allow the generation of the main projections; the elements that compose them; a spreadsheet (with a brief report and main data of the component); scripts on how to create a new component and how to configure the existing one; and some materials previously configured for application.

The files created were posted in a branch of the main FreeCAD library, which can be merged into the main library of said library:
https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Bedroom :

. Bedroom_closet.FCStd

. Beds.FCStd

https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Bedroom/Images :

. Bed_single_image_01.jpg

. Bedroom_closet_model_01_image_01.jpg

. Bedroom_closet_model_02_image_01.jpg

. Bedroom_closet_model_03_image_01.jpg

. Bedroom_closet_model_03_image_02.jpg

https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Kitchen :

. Kitchen_cabinet_vertical.FCStd

https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Kitchen/Images :

. Kitchen_cabinet_vertical_model_02_image_01.jpg

https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Living%20room :

. Chair.FCStd

. Living_room_cabinet.FCStd

. Rectangular_tables.FCStd

. Sofa_Armchair.FCStd

https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Living%20room/Images ;

. Armchair_model_03_image_01.jpg

. Bedside_table_image_01.jpg

. Chair_image_01.jpg

. Living_room_cabinet_model_01_image_01.jpg

. Living_room_cabinet_model_01_image_02.jpg

. Living_room_cabinet_model_02_image_01.jpg

. Living_room_cabinet_model_04_image_01.jpg

. Sofa_armchair_imag_01.jpg

. Sofa_armchair_imag_02.jpg

. Sofa_model_01_image_01.jpg

. Sofa_model_02_image_01.jpg

. Table_image_01.jpg

. Table_image_02.jpg

https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Windows/Casement ;

. Window_casement_parametric.FCStd

https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/Architectural%20Parts/Windows/Casement/Images ;

. Window_casement_model_01_image_01.jpg

. Window_casement_model_01_image_02.jpg

. Window_casement_model_02_image_01.jpg

. Window_casement_model_03_image_01.jpg

. Window_casement_model_04_image_01.jpg

## 2. Procedures adopted

In general, the criterion of creating parametric components structured by basic sketches was adopted. Thus, with small adjustments to those already presented, the four main procedures were:

• Implementation of one or more sets of properties in the parameterization control;

• Arrangement of expressions structuring the geometry of the created components;

• Use of Attachment resources in the properties of the objects, allowing the coordination of adjustments of positions, angles, and dimensions of the objects simultaneously;

• Creation of macros of basic configurations of each component.


However, for windows and doors, the basic sketches will be changed to a vertical plane established in the XZ plane. This allows the component to automatically adapt to the new positioning (Placement), relative to the X, Y, Z and rotation variables. Further adjustments to dimensions, materials, display options and even mirroring of the component itself (in the case of doors and windows) can be made using the property sets created.

## 3. Next steps

As planned, the fifth and final stage will involve the necessary general review of the components, mainly regarding doors and windows, as already developed with the conventional window.

For this general review, we would like to take the opportunity to list some points that we would like to resolve in this final stage, for which we are not yet sure how to obtain a complete solution. Therefore, we need external help. They are:

• *ShapeColor*: include control over the adjustment of the colors of the component elements acting together with the configuration of the materials;

• Translations: create the possibility that the parts and properties of the components can be translated. If there is no ready-made solution for this, we are considering creating a spreadsheet of strings within each file, which can serve as a database for use in future translations. Using a macro, the translated strings would be collected, creating a new set of properties such as the selected language, which in turn would control the original set of properties of the file;

• Macros: in addition to what was already discussed in the previous report, the macros for configuring component models need to be further developed. They have be adapted as the component is inserted into the project, with the appropriate updating of the names of the properties, materials, and profiles adopted. As a method, and similar to the previous point, we are considering using a dictionary to manage the component properties, allowing them to be saved and updated when possible;

• *PropertyEnumeration*: although it should be quite basic, we have not yet managed to use the property to list the profile options available in the component configuration. The solution used, *PropertyLink*, although it works, requires a lot of attention and care when choosing the correct option. A list of the corresponding options would be much simpler and more appropriate.

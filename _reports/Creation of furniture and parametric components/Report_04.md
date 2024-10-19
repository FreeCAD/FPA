# Creation of furniture and parametric components

## FPA Grant to Francisco Rosa

## Report 4, 10/15/2024

In this fourth report on the development of parametric components, we once again present a summary of the work carried out, a brief description of the procedures adopted and the next steps.

## 1. Work carried out

We continued the development of individualized files for kitchen, living room and bedroom cabinets. Another new components such as tables, chairs, beds, sofas, armchairs were also created and we began the general review of windows with the redesign of the casement type.

This review consisted of restructuring the *Attachments* to be based on a vertical Sketch with the dimensions of the opening. With this, it is possible to move and rotate the component (on the three axes) so that it can be inserted into the project wall, whatever its final position. It was also possible to leave the window panels open at any specified angle. Finally, to facilitate its adaptation to the positioning in the project, we can mirror the entire window on the wall, a very useful and necessary feature, without a doubt.

Another included feature was the configuration of the profiles of each window part. These elements can also be parameterized, in addition to the option of adopting “fixed” standard profiles.

Therefore, window insertions in projects, through the FreeCAD library, can be carried out directly, it is not necessary to create clones, copies or links, but they are still valid options.

We extended the possibility of creating macros that automate the generation of the different options, with this the user can quickly obtain a specific pre-configuration of the component, or creating and saving the ones that will be used most in their projects.

As previously phases, each file contains: a set of its main configurable properties; a base for moving and rotating the component; previously established sections that allow the generation of the main projections; the elements that compose them; a spreadsheet (with a brief report and main data of the component); guidelines on how to create a new component and how to configure the existing one; and some materials previously configured for application.

Once again, some rendered images were posted demonstrating the results of the configurations created, as well as two videos relating to the insertion of windows and components in general.

The files created were posted in a branch of the main FreeCAD library, which can be merged into the main one. Their locations are:

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

In general, the criterion adopted was the creation of parametric components structured by basic sketches. Thus, with small adjustments to those already presented, the four main procedures were:

• Implementation of one or more sets of properties in the parameterization control;

• Arrangement of expressions structuring the geometry of the components;

• Use of *Attachment* resources in the properties of the objects, allowing the simultaneous coordination of adjustments of positions, angles, and dimensions of the objects;

• Creation of macros of basic configurations of each component.


However, for windows and doors, the basic sketches will be changed to a vertical plane established in the XZ plane. This allows the component to automatically adapt to the new *Placement*, relative to the X, Y, Z and rotation variables. Further adjustments to dimensions, materials, display options and even mirroring of the component itself (in the case of doors and windows) can be made using the property sets created.

## 3. Next steps

As planned, the fifth and final stage will involve the necessary general review of the components, mainly regarding doors and windows, as already developed with the casement window.

We will also prepare macros so that the "Doors_windows.FCStd" file can generate static models as suggested. We will try to review its general structure, but due to its enormous complexity, we do not know if it will be fully feasible.

For this general review, it is important to take the opportunity to list some points that we plan to resolve in this final stage, for which we are not yet sure how to obtain a complete solution. Therefore, we need external help. They are:

• *ShapeColor*: it is necessary to include control over the adjustment of the colors of the component parts, acting together with the configuration of materials;

• Translations: it would be good to create the possibility to translate the parts and properties of the components. If there is no ready-made solution for this, we are considering creating a spreadsheet of strings within each file, which can serve as a database for use in future translations. Using a macro, the translated strings would be collected, creating a new set of properties for the selected language, which in turn would control the original one of the file;

• Macros: in addition to what was already discussed in the previous report, the macros for configuring component models need to be further developed. They have to be adapted as the component is inserted into the project, with the appropriate updating of  the properties names, materials, and profiles adopted. As a method, and similar to the previous point, we are considering using a dictionary to manage the component properties, allowing them to be saved and updated when possible;

• *PropertyEnumeration*: although it should be quite basic, we have not managed to use this property. The solution used, *PropertyLink*, although it works, requires a lot of attention and care. A list of the corresponding options would be much simpler and more appropriate.

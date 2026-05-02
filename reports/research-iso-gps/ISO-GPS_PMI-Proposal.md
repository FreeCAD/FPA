# FreeCAD PMI Implementation Proposal for ISO GPS


#### Table of Contents  
1. [Summary](#1-Summary)  
2. [Scope](#2-Scope)  
3. [Referenced Standards](#3-Referenced-Standards)  
4. [Industry-aligned Workflow](#4-Industry-aligned-Workflow)  
5. [Objects, commands and possibilities](#5-Objects-commands-and-possibilities)  
   5.1. [Create and manage the PMI workbench](#51-Create-and-manage-the-PMI-workbench)  
   5.2. [Preferences for standards mode and behavior adaptation](#52-Preferences-for-standards-mode-and-behavior-adaptation)  
   5.3. [Create and manage the PMI container (Annotation Set)](#53-Create-and-manage-the-PMI-container-Annotation-Set)  
   5.4. [Create, activate, edit, duplicate, delete Views](#54-Create-activate-edit-duplicate-delete-Views)  
   5.4.1. [Clipping planes](#541-Clipping-planes)  
   5.5. [Create Datum annotations](#55-Create-Datum-annotations)  
   5.6. [Create Datum Reference Frame (Datum System) objects](#56-Create-Datum-Reference-Frame-Datum-System-objects)  
   5.7. [Create Dimensional specifications](#57-Create-Dimensional-specifications)  
   5.8. [Create Geometric Tolerance annotations (Feature Control Frames)](#58-Create-Geometric-Tolerance-annotations-Feature-Control-Frames)  
   5.9. [Selection logic and validity rules for geometric tolerances based on context (Tolerancing Advisor)](#59-Selection-logic-and-validity-rules-for-geometric-tolerances-based-on-context-Tolerancing-Advisor)  
   5.10. [Create Text, Note, and Leader annotations](#510-Create-Text-Note-and-Leader-annotations)  
   5.11. [Add Tables](#511-Add-Tables)  
   5.12. [Supplemental geometry (construction lines, center marks, axes)](#512-Supplemental-geometry-construction-lines-center-marks-axes)  
   5.13. [Surface texture specifications (later phase)](#513-Surface-texture-specifications-later-phase)  
   5.14. [Bind annotations to model geometry](#514-Bind-annotations-to-model-geometry)  
   5.15. [Repair broken references](#515-Repair-broken-references)  
   5.16. [Recompute behavior when geometry changes](#516-Recompute-behavior-when-geometry-changes)  
   5.17. [Edit and modify existing annotations](#517-Edit-and-modify-existing-annotations)  
   5.18. [Annotation stacking and attachment between annotations](#518-Annotation-stacking-and-attachment-between-annotations)  
   5.19. [Control which annotations belong to which views](#519-Control-which-annotations-belong-to-which-views)  
   5.20. [Validate Annotations](#520-Validate-Annotations)  
   5.21. [Query specifications for a selected feature](#521-Query-specifications-for-a-selected-feature)  
   5.22. [Derive TechDraw pages from PMI Views](#522-Derive-TechDraw-pages-from-PMI-Views)  
   5.23. [STEP AP242 Import](#523-STEP-AP242-Import)  
   5.24. [STEP AP242 Export](#524-STEP-AP242-Export)  
   5.24.1 [JT, PRC / 3D PDF and QIF export (later phase)](#5241-JT-PRC--3D-PDF-and-QIF-export-later-phase)
   5.25. [Semantic data access for other workbenches](#525-Semantic-data-access-for-other-workbenches)  
   5.26. [Undo/Redo and WB switching](#526-UndoRedo-and-WB-switching)  
6. [Proposed Document Object Model](#6-Proposed-Document-Object-Model)  
7. [Annotation Categories for ISO GPS Support](#7-Annotation-Categories-for-ISO-GPS-Support)  
   7.1. [Datums and Datum Systems per ISO 5459](#71-Datums-and-Datum-Systems-per-ISO-5459)  
   7.2. [Dimensional Specifications per ISO 14405-1, ISO 14405-3, ISO 129-1](#72-Dimensional-Specifications-per-ISO-14405-1-ISO-14405-3-ISO-129-1)  
   7.3. [Geometric Tolerances (Macrogeometrical Specifications) per ISO 1101](#73-Geometric-Tolerances-Macrogeometrical-Specifications-per-ISO-1101)  
   7.4. [Profile Tolerances per ISO 1660](#74-Profile-Tolerances-per-ISO-1660)  
   7.5. [Text Annotations](#75-Text-Annotations)  
   7.6. [Leaders](#76-Leaders)  
   7.7. [Surface Texture per ISO 21920 series](#77-Surface-Texture-per-ISO-21920-series)  
8. [Missing Symbols and Modifiers per ISO GPS](#8-Missing-Symbols-and-Modifiers-per-ISO-GPS)  
9. [Suggested Implementation Phases](#9-Suggested-Implementation-Phases)  
10. [Open Topics and Risks](#10-Open-Topics-and-Risks)  
11. [Appendix A: OCCT Enumeration Mapping Reference](#Appendix-A-OCCT-Enumeration-Mapping-Reference)  
 

## 1. Summary

FreeCAD has no native PMI (Product Manufacturing Information) capability. There is no way to attach semantic tolerancing data to a 3D model, no way to import or export GD&T via STEP AP242, and no dedicated 3D annotation infrastructure. TechDraw handles basic 2D dimensioning but has no feature control frame support. Third-party attempts ([FreeCAD-GDT WB](https://github.com/juanvanyo/FreeCAD-GDT)) are unmaintained and incompatible with current FreeCAD.

This proposal defines an overall basic PMI workflow for FreeCAD, focused on ISO GPS first. It covers major document objects, commands, dialogs, selection rules, and data exchange requirement needed to go from an unannotated model to a toleranced 3D product definition with derived 2D drawings and STEP AP242 support.

All annotations are semantic: they carry structured, typed data that other workbenches (CAM, Inspection, maybe future addons like tolerance analysis / stacking or DFM) can make use of. They are not display-only text overlays (though they will be displayed as well as such).

The proposal does not claim to be complete, but rather serves as a guideline for implementing the most important functions for an entire PMI workflow. It is organized as a functional specification acc. to the grant description for potential developers, a GSoC project or maintainers. It does not contain code implementations but rather assumptions on how this could be implemented, so the proposed property types should not be taken for granted. 



---

## 2. Scope 

**In scope (must-have and initial implementation):**
- Dimensional specifications (linear sizes, angular sizes, distances)
- Geometric tolerances (all 14 ISO 1101 types: form, orientation, location, runout, profile)
- Datums and datum systems (single datums, common datums, datum targets)
- 3D annotation views with camera state (incl. zoom), visibility, clipping, annotation plane
- Text annotations, leaders, flag notes
- TechDraw page derivation from PMI views (for classic 2D export)
- STEP AP242 import and export (semantic PMI; graphical PMI as plus)
- Some sort of semantic API for cross-workbench or addon usability

**In scope (not critical but later phase):**
- Surface texture specifications (ISO 21920 series, replacing ISO 1302/4287/4288)
- Welding symbols (ISO 2553)
- General tolerance notes per ISO 22081 (replacing withdrawn ISO 2768-2)
- Edge/transition specifications per ISO 13715 and ISO 21204
- JT import and export for lightweight 3D product definition exchange
- PRC / 3D PDF import and export for downstream viewing, review and documentation
- QIF export for quality workflows
- Surface texture specifications (ISO 21920 series, replacing ISO 1302/4287/4288)

**Out of scope:**
- Tolerance analysis / stack-up calculation (maybe as addon in the future)
- Automatic dimensioning (one click)
- Full ASME Y14.5 implementation (mentioned as preference extensibility only)
- Change of annotation to change the model (reverse approach)

**General Assumptions:**
- A new workbench named "PMI"
- A PMI container group in the document tree, per Document, Part or Assembly
- Under PMI, one or more View objects
- Under each View, annotation objects (similar to how TechDraw pages collect dimensions and annotations)
- Annotations reference model geometry maybe via PropertyLinkSub (using TNP-mapped element names)
- TechDraw pages could be derived from PMI views for classic/old 2D output format
- STEP AP242 remains the primary format target for semantic CAD + PMI exchange. JT, PRC / 3D PDF and QIF cover adjacent but different use cases but should not be ignored.

---

## 3. Referenced Standards

The standards used for this research are the following, with only ISO GPS in scope.

**Geometrical Product Specification (GPS):**

| Standard | Content |
|----------|----------------|
| ISO 8015:2011 | Fundamental tolerancing principles (independency principle) |
| ISO 1101:2017 | Geometrical tolerancing: form, orientation, location, runout |
| ISO 5459:2011 | Datums and datum systems |
| ISO 5458:2018 | Position tolerancing |
| ISO 14405-1:2016 | Dimensional tolerancing: linear sizes |
| ISO 14405-2:2018 | Dimensional tolerancing: other than linear/angular sizes |
| ISO 14405-3:2016 | Dimensional tolerancing: angular sizes |
| ISO 286-1:2010 | ISO tolerance system for linear sizes (fits) |
| ISO 2692:2021 | Maximum/Least material requirement, reciprocity |
| ISO 1660:2017 | Profile tolerancing |
| ISO 22081:2021 | General geometrical specifications (replaces ISO 2768-2) |
| ISO 14638:2015 | GPS matrix model |
| ISO 129-1:2018 | Indication of dimensions and tolerances |

**Technical Product Documentation:**

| Standard | Content |
|----------|----------------|
| ISO 16792:2021 | Digital product definition data practices (3D annotation rules) |

**Data Exchange:**

| Standard | Content |
|----------|----------------|
| ISO 10303-242 ed1-ed4 | STEP AP242: PMI semantic and graphical representation |
| ISO 14306:2017 | JT: lightweight 3D visualization incl. PMI |
| ISO 14739-1:2014 | PRC: Product Representation Compact for use in 3D PDF |
| ISO 23952:2020 | QIF: exchange format for quality planning and measurement workflows |

**Future extensibility for GD&T and similar JIS (preference system must accommodate):**

| Standard | Content |
|----------|----------------|
| ASME Y14.5-2018 | Dimensioning and Tolerancing |
| ASME Y14.41-2019 | Digital Product Definition Data Practices |
| JIS B 0021 | Geometrical tolerancing (Japanese) |

---

## 4. Industry-aligned Workflow

The intended user workflow, from an empty document to exported product definition:

1. User completes a Part, PartDesign Body, or Assembly model (alternatively an imported STEP file)
2. User switches to the PMI workbench
3. User creates a PMI container in the document tree
4. User creates one or more PMI Views (e.g. Front, Top, Section A-A) Standard ones offered
5. User activates a View (double click). This sets the camera, shows the annotation plane, applies clipping, and filters visible objects/annotations.
6. While a View is active, the user:
   - Defines datums on model faces/features (primary, secondary, tertiary)
   - Adds dimensions with tolerances to features
   - Adds geometric tolerances (feature control frames) referencing datums
   - Adds text annotations, notes, leaders or others (tables,...)
7. User switches between Views to annotate the model from different directions
8. User runs a validation check for standards compliance
9. User optionally derives TechDraw drawing pages from PMI Views for an old-school 2D export
10. User exports to STEP AP242 with semantic PMI data. Bonus with graphical conversion of annotations
11. Later phase / optional downstream outputs
   - JT for lightweight product definition exchange and visualization workflows
   - PRC / 3D PDF for review and documentation
   - QIF for quality planning and inspection preparation

This is aligned with the industry workflows in apps like SolidWorks, CATIA FTA or NX PMI.

---

## 5. Objects, commands and possibilities

### 5.1 Create and manage the PMI workbench

**User intent:** Access a dedicated workspace for 3D annotation and tolerancing.

**Proposed behavior:**
- The PMI workbench appears in the workbench selector alongside Part, Part Design, TechDraw, etc.
- It offers the creation of a PMI container if a document contains at least one Solid, Surface, Part, Body, or Assembly object
- Activating the workbench shows toolbars organized in sections: Views, Annotations, Visualization, Validation
- The workbench does not modify or interfere with the model geometry. All PMI objects are non-geometric metadata but can have a human-readable 3D representation (also for export).

**Toolbar / menu sections:**
- Views: Add Standard Views, Custom View, Activate View, Edit View, Clipping Plane (still needs to be implemented: [#12187](https://github.com/FreeCAD/FreeCAD/issues/16187))
- Annotations: Datum, Datum System, Dimension, Geometric Tolerance, Note, Leader, Optional: SVG, table (from Spreadsheet), follow up for Surface, Weld,...
- Validation: Query Element, Validate Annotations, Repair Broken References
- Visualization (optional): Toggle Annotations, Filter/Select by Type, Select Linked Geometry, Select Linked Annotations, Stack Frame
- TechDraw Workflow: Derive TechDraw page (not sure if this should be in the PMI WB or TechDraw)



---

### 5.2 Preferences for standards mode and behavior adaptation

**User intent:** Configure which tolerancing standard governs annotation behavior.

**Where:** Edit > Preferences > PMI

**Required preference settings:**

- **Governing standard** (Enumeration: ISO GPS, ASME GD&T)
  - ISO GPS (default): Independency principle per ISO 8015. Annotation planes default to coordinate system alignment per ISO 16792 (7.3.4) Tolerance display per ISO 129-1.
  - ASME GD&T: Envelope rule (Difference to ISO GPS) per ASME Y14.5. Annotation planes default to surface-relative alignment per ASME Y14.41. Tolerance display per ASME conventions.
  - Future: JIS option. Architecture must allow adding this in the future without structural changes.
  - Changing the standard affects all subsequently created annotations. Existing annotations are not retroactively changed (not possible to convert automatically). The validation command can flag standard inconsistencies.

- **Default tolerance method** (Enumeration: Plus/Minus, Limits, Fit Designation, None)
- **Decimal places** (Integer, default 2 for mm, 3 for inch). Should not use document decimal places automatically.
- **Font family and size** for annotation text
- **Arrow type** (Filled, Open, Dot, Tick) and size
- **Leader line style** (Solid, Dashed) and width
- **Annotation plane display** (Show/hide plane (like sketch), color, opacity)
- **Tolerancing advisor** (Bool: whether context-sensitive filtering is active)
- **Unit system** follows FreeCAD's global unit setting (mm/inch)

The defaults could be overwritten per individual annotation (similar as in TechDraw).

**Differences of the standards that the preference must control:**
- Default principle: ISO independency vs. ASME envelope (affects if form is controlled by size)
- Datum indicator style: ISO uses filled/open triangle, ASME uses filled triangle only
- Feature control frame notation: minor symbol differences exist between ISO 1101 and ASME Y14.5
- Annotation plane creation logic: ISO standard document coordinate-system-aligned vs. ASME surface-relative

**Open point:** Verify exact symbol differences between ISO 1101 and ASME Y14.5 for each tolerance type and modifier. Some symbols (e.g. concentricity, symmetry) have been deprecated or repositioned differently. This concept focusses on ISO GPS though.

---

### 5.3 Create and manage the PMI container (Annotation Set)

**User intent:** Organize all PMI data for a part or assembly in a dedicated tree container.

**Proposed document structure:**

```
Document
  Body1
    Pad
    Pocket
    ...
  Part1
    Body2
    ...
  PMI [AnnotationSet]
    View: Front
      Datum1
      Datum2
      Dimension1
      Flatness1
    View: Right
      Datum2
      Position1
    View: Section A-A
      Dimension2
```

**Properties of the PMI container:**
- Standard (Enumeration: ISO_GPS, ASME_GDT) = overrides global preference at document level
- Label (String) = Name or descriptive text
- Visibility (Boolean) = toggles all children on/off

**Behavior:**
- One PMI container per Part/Assembly (not in a PD Body) is the typical case. We can also do one per document.
- Multiple containers are allowed for multi-stage manufacturing or different specs
- The container is auto-created when the user first creates a view or annotation in the PMI workbench. Or the user can create it explicitly.
- On STEP AP242 import, one container is created per part, populated with imported PMI data

---

### 5.4 Create, activate, edit, duplicate, delete Views

**User intent:** Define named camera states that organize how PMI annotations are presented and consumed.

A PMI View is the fundamental organizational unit. It stores what the viewer sees when consuming the product definition. Equivalent to CATIA "Capture" or NX's "Model View".

**Properties:**
- ViewName (String) = user-visible name (e.g. "Front View", "Section A-A")
- CameraView = storing camera position, direction, up-vector, type (ortho/perspective), and zoom
- AnnotationPlane (Placement) = the 2D plane on which annotations are projected and placed on and can be moved on
- VisibleObjects (LinkList) = which document objects (models) are visible
- VisibleAnnotations (LinkList) = which annotations appear in this view
- ClippingPlanes (LinkList) = references to ClippingPlane objects active in this view
- CoordinateSystem (Link) = optional local coordinate system reference

**Commands:**

**PMI_CreateStandardViews:**
- Creates six orthographic views (Front, Back, Left, Right, Top, Bottom) plus one Isometric
- Camera positions calculated from the part's bounding box
- Each view gets an annotation plane parallel to the respective coordinate plane
- User can select which to create via checkboxes in a dialog (similar to TechDraw ProjGroup or CATIA "Principal Views" panel)


**PMI_CreateCustomView:**
- Captures the current 3D camera state
- Creates a new View object with the current camera position, direction, zoom and visible objects and active clipping planes
- Annotation plane defaults to the plane perpendicular to the camera direction, passing through the model center

**PMI_ActivateView (also triggered by double-click on View in tree):**
- Restores camera to stored position/direction/zoom
- Shows only VisibleObjects
- Shows only VisibleAnnotations
- Activates listed ClippingPlanes of the view
- Displays the annotation plane as a semi-transparent overlay (if enabled in preferences)
- Sets this View as the "active object": any new annotation created is automatically added to this View's VisibleAnnotations list (similar to active Part)
- Similar UX pattern to double-clicking a PartDesign Body to activate it

**PMI_DeactivateView:**
- Returns to default or previous 3D state (before entering a view, fallback: all objects visible, no clipping, no annotation filter).
- No View is active. Creating annotations without an active view is allowed but they are "unassigned" until moved to a view.

**PMI_EditView:**
- Opens a task panel to modify:
  - View name
  - Camera parameters (can recapture from current viewport) or standard views
  - Annotation plane position/orientation (can align to face, datum plane, or coordinate plane), also via attachment
  - Object visibility checkboxes (list of all objects)
  - Clipping plane selection
- Changes apply immediately (live preview)

**PMI_DuplicateView:**
- Creates a copy of the selected View with all properties
- Annotations are shared (referenced, not copied). The duplicate shows the same annotations but can be modified independently (e.g. different camera angle, different annotation visibility).

**Editing behavior:**
- Double-click a View: activates it
- Right-click a View: context menu with Activate, Edit, Duplicate, Delete, Rename
- Drag annotations between Views in the tree to move them

**Relationship between Views and annotations:**
- An annotation is NOT "owned" by a View. It is referenced / linked (e.g. a datum could be visible in multiple views).
- An annotation can appear in multiple Views (e.g. Datum A visible in both Front and Right views)
- An annotation has its own AnnotationPlane property, independent of the View. But when created inside an active View, it inherits the View's annotation plane by default.
- Deleting a View does not delete its annotations. The annotations remain in the PMI container.

**Related gaps in FreeCAD:**
- FreeCAD has no persistent named view objects in the document (Std_FreezeViews is session-only, Draft WorkingPlaneProxy is the most similar but lacks annotation filtering and clipping). The PMI View is a new object type.
- Related GitHub issues: [#16187](https://github.com/FreeCAD/FreeCAD/issues/16187) (persistent clipping planes), [#19795](https://github.com/FreeCAD/FreeCAD/issues/19795) (STEP AP242 views). The RT fork has saved views already implemented, and similar properties are stored in Draft WPs.

---

#### 5.4.1 Clipping planes

FreeCADs current clipping (Std_ToggleClipPlane) has no document persistence. A PMI View needs reusable, saveable clipping planes.
*Ideally this is fixed with [#16187](https://github.com/FreeCAD/FreeCAD/issues/16187).*

**User intent:** Create persistent clipping planes that can be associated with views.

**Properties of PMI_ClippingPlane:**
- PlaneNormal (Vector) = plane origin and normal direction
- Flipped (Bool) = flips the direction of the plane
- IncludedObjects (LinkList) = which objects are clipped (empty = all visible). If persistent clipping planes are implemented, it could store these instead. Default is empty, if empty, all objects are clipped.
- ExcludedObjects (LinkList) = which objects are NOT clipped.
- IsActive (Bool)
- ShowCapping (Bool) = show solid cross-section faces at the cut
- ShowPlane (Bool) = display as semi-transparent rectangle (similar as the ShowPlane of Sketches)
- HorizontalSize and VerticalSize (optional) = store a size of the plane to define how far it clips the document. Infinite if none (default)

**Command: PMI_AddClippingPlane**
- User selects a face (plane aligns to face normal), a datum plane, or specifies position/direction manually
- It can be attached to objects in the document or interactively dragged in the 3D view
- The plane appears in the tree under the PMI container
- It can be assigned to one or more Views
- Interactive dragging in 3D is supported (like FEM clipping planes)

**Task dialog contents:**
- Reference selection field (face, datum plane, or coordinate plane) or the attachment dialog
- Manual offset input (distance along normal)
- Included objects list (optional, defaults to all)
- Excluded objects list
- Flip direction button
- Preview toggle

The Clipping Plane is only visual. It does NOT compute BRep booleans (unlike Part_SectionCut, which does but also is very slow).
Existing clipping planes of the document could be used and dragged into a view.

**Related issues:** [#16187](https://github.com/FreeCAD/FreeCAD/issues/16187), [#16190](https://github.com/FreeCAD/FreeCAD/issues/16190), [#11169](https://github.com/FreeCAD/FreeCAD/issues/11169), [#11173](https://github.com/FreeCAD/FreeCAD/issues/11173), [#18877](https://github.com/FreeCAD/FreeCAD/issues/18877)

---
 

### 5.5 Create Datum annotations

**User intent:** Identify reference features on the model that serve as the basis for orientation and location specifications. Per ISO 5459.

**What this object represents:**
A datum is a theoretically exact geometric element (point, line, or plane) derived from a real (imperfect) feature on the part. Datums establish the coordinate framework for all orientation and location tolerances.

**Properties:**
- DatumLabel (String) = uppercase letter A-Z, auto-assigned in sequence (per PMI object)
- DatumType (Enumeration):
  - SimpleDatum = attached to a complete feature surface
  - DatumTarget_Point, DatumTarget_Line, DatumTarget_Rectangle, DatumTarget_Circle, DatumTarget_Area per ISO 5459 datum target definitions
- LinkedGeometry (LinkSub) = reference to face, edge, or vertex
- TargetNumber (Integer) = for datum targets: e.g. A1, A2, A3
- TargetShape / TargetDimensions for area targets: boundary shape and size
- Modifiers (StringList) per ISO 5459:
  - [CF] contacting feature
  - [PL] situation element is a plane
  - [SL] situation element is a straight line
  - [PT] situation element is a point
  - Material condition modifiers (M, L) for features of size
- AnnotationPlane (Placement) = referencing the view
- LeaderPoints (VectorList), or maybe via placement the points to reference the geometry (should move with the model)
- AttachedToDimension (Link) = optionally, renders the datum indicator on this dimension line instead of directly on geometry

**Command: PMI_AddDatum**

**Preconditions:** Model geometry must exist. PMI workbench active. Ideally, a view should be active.

**What the user selects first:** A face, edge, or vertex on the model. Should work with preselection or selected in the task dialog

**Task dialog contents:**
- Selected reference element
- Datum letter (auto-assigned, editable)
- Datum type (auto-detected from selection. User can override to datum target)
- If datum target: target number, target type (point/line/rectangle/circle/area), size fields
- Modifiers dropdown (available options filtered by selection type)
- Annotation plane selector (defaults to active view plane)
- Preview of datum indicator symbol on the model in the 3D view

**Selection-based logic:**
- Planar face selected: SimpleDatum, triangle indicator placed on face with leader
- Cylindrical face selected: SimpleDatum, indicator attached to derived axis. The datum references the axis, not the surface
- Two parallel faces selected: Common datum offered (e.g. A-B), center plane is the datum
- Edge selected: SimpleDatum on the edge (center line or derived element)
- Vertex selected: SimpleDatum (point datum, unusual but valid)
- No geometry selected: Datum target creation mode (user selects target manually)

**Datum letter assignment logic:**
- Letters are assigned in the order A, B, C,...
- The system tracks which letters are used and offers the next available letter
- User can override (e.g. skip to D)
- Reassigning an existing letter is blocked with a warning

**Rendering:**
- SimpleDatum: filled triangle (ISO) or open triangle with letter in a rectangular frame, connected to the feature by a leader line.
- DatumTarget: circle divided horizontally, target number above the line, datum letter and sequence below. Per ISO 5459.

**Error handling:**
- If the linked geometry is deleted or renamed (TNP breaks), the datum is flagged as "broken" (red overlay icon).
- A datum that is referenced by geometric tolerances cannot be deleted without confirmation ("Datum A is referenced by 3 annotations. Delete anyway?").

**Import/export:**
- Maps directly to OCCT XCAFDoc_Datum with XCAFDimTolObjects_DatumObject
- DatumLabel maps to datum identification name
- DatumType maps to XCAFDimTolObjects_DatumTargetType
- Modifiers map to XCAFDimTolObjects_DatumSingleModif (22 values covering DOF constraints, material conditions, geometric modifiers)

---

### 5.6 Create Datum Reference Frame (Datum System) objects

**User intent:** Combine datums into a prioritized reference system for geometric tolerances. Per ISO 5459.

**What this object represents:**
A datum reference frame establishes up to three mutually perpendicular reference planes from which location and orientation are measured. The primary datum constrains the most degrees of freedom.

**Properties:**
- PrimaryDatum (Link) = reference to a PMI Datum object
- PrimaryModifiers (StringList)
- SecondaryDatum (Link) = optional
- SecondaryModifiers (StringList)
- TertiaryDatum (Link) = optional
- TertiaryModifiers (StringList)

**Behavior:**
- Usually created implicitly when the user specifies datum references in a geometric tolerance
- Can also be created explicitly if the user wants to reuse the same datum system across multiple tolerances
- The 3-2-1 rule: primary constrains 3 DOF (plane), secondary constrains 2 (line), tertiary constrains 1 (point). The system should warn but not block if the constraint count is geometrically inconsistent.

**Validation:**
- A plane datum as primary: valid (constrains translation along normal + two rotations = 3 DOF)
- A cylindrical datum as primary: constrains 4 DOF (two translations + two rotations). Only one more datum needed.
- If the user specifies datums that constrain the same degrees of freedom (e. g. three parallel planes all constraining the same direction), warn that the datum system is redundant and does not form a proper coordinate system.

**Open point:** The exact DOF logic depends on the geometric type of each datum feature. Full validation requires understanding the association between datum indicator position and the derived ideal element. ISO 5459 Annex B has guidance on DOF counting.

---

### 5.7 Create Dimensional specifications

**User intent:** Specify size, distance, and angle dimensions on model features. Per ISO 14405-1 (linear sizes), ISO 14405-3 (angular sizes), ISO 129-1 (indication).

**Properties:**
- DimensionType (Enumeration) = mapped to OCCT XCAFDimTolObjects_DimensionType (31 values):
  - Size types: Diameter, Radius, SphericalDiameter, SphericalRadius, CurveLength, Thickness, Angular
  - Location types: LinearDistance (with inner/outer/center variants), CurvedDistance, Angular
- LinkedGeometry (LinkSubList) = one sub-element for sizes, two for distances
- NominalValue (Float) = auto-calculated from geometry, editable
- UpperTolerance (Float)
- LowerTolerance (Float)
- ToleranceType (Enumeration): PlusMinus, Limits, FitDesignation, Symmetrical, None
- FitClass (String) = e.g. "H7", "g6", looked up from ISO 286-1
- FitGrade (Enumeration) = IT01 through IT18
- SpecificationModifiers (StringList) = per ISO 14405-1:
  - LP (two-point size), GG (Gauss), GX (max inscribed), GN (min circumscribed), GC (Chebyshev)
  - E (envelope requirement)
  - SX, SN, SA, SM, SR, SD (statistical modifiers)
  - CT (common tolerance), ACS (any cross section), SCS (specific cross section)
  - CC (circumference diameter), CA (area diameter), CV (volume diameter)
- IsBasic (Bool) = TED (theoretically exact dimension), displayed dimensional value in rectangular frame per ISO 1101
- Qualifier (Enumeration): None, Min, Max, Avg
- ShowDiameterSymbol (Bool)
- ShowRadiusSymbol (Bool)
- AnnotationPlane (Placement)
- DimensionLineLayout (various vectors for line geometry, extension lines, arrows, to attach to the model and place the annotation)
- TextPosition (Vector)
- TextOverride (String) = optional manual text
- FeatureCount (Integer) = number of identical features sharing this dimension (displayed as "4x" prefix, e.g. "4x Diameter 6,5 H7"). Default 0 or 1 meaning no prefix shown.

**Command: PMI_AddDimension**

**What the user selects first:** One or two geometric subelements (faces, edges, vertices).

**Task dialog contents:**
- Detected dimension type (auto, can be overridden)
- Nominal value (auto-calculated, editable)
- Tolerance section:
  - Type dropdown: None, Plus/Minus, Limits, Fit Designation, Symmetrical
  - If Plus/Minus: upper and lower deviation fields
  - If Limits: max and min value fields (derived from nominal +/- deviations)
  - If Fit Designation: class dropdown (H7, g6, etc.) with auto-lookup of deviations from ISO 286-1 tables
  - If Symmetrical: single value applied as +/- equally
- Modifiers section: multi-select from ISO 14405-1 modifier list (filtered by dimension type)
- Basic/TED checkbox
- Qualifier dropdown (None, Min, Max, Avg)
- Diameter/Radius symbol checkbox
- Preview in 3D

**Selection-based auto-detection logic:**

| Selection | Detected Type |
|-----------|---------------|
| One cylindrical face | Size_Diameter |
| One spherical face | Size_SphericalDiameter |
| One circular edge | Size_Diameter or Size_Radius (user prompted) |
| Two parallel planar faces | Location_LinearDistance |
| Two non-parallel planar faces | Location_Angular |
| One conical face | Size_Angular (half-cone angle) |
| One edge on a cylindrical feature + nothing else | Size_Radius |
| One edge + one face | Location_LinearDistance (edge to face) |
| Two parallel edges | Location_LinearDistance |
| One face (planar, non-size) | Not a dimension candidate; suggest geometric tolerance instead |



**Dimension arrangement modes:**
Besides individual dimensions, the following arangement modes per ISO 129-1 should be supported:
- Chain dimensioning: sequential dimensions between adjacent features, each measured from the previous one
- Baseline / parallel dimensioning: all dimensions measured from a common datum feature, arranged as parallel dimension lines
- Ordinate / cumulated dimensioning: all dimensions measured from a common origin, shown as cumulated values along a coordinate axis
- Stacked dimensioning: multiple dimensions sharing one reference point, stacked vertically

These are not separate object types but arrangement modes that affect how dimension lines are placed. The task dialog could offer these as a layout option when multiple dimensions reference the same baseline or origin.

**Modifier availability logic per ISO 14405-1:**
- LP, GG, GX, GN, GC: available for linear size dimensions only (features of size)
- E (envelope requirement): available for linear size dimensions only
- CC, CA, CV: available for diameter-type sizes only
- SX, SN, SA, SM, SR, SD: available for any dimension type
- ACS, SCS: available for size dimensions on rotation-symmetric features
- CT: available when multiple identical features share the same tolerance

**TED/Basic dimension logic:**
- When a dimension is referenced by a position tolerance (ISO 5458) or profile tolerance with datums (ISO 1660), it MUST be theoretically exact (TED/basic)
- The system should suggest setting IsBasic=true when the user creates a position tolerance that needs TED dimensions. Alternatively, warn if position tolerance references are made but dimensions are not marked as basic.

**Thread dimensions:**
Threaded holes and shafts need thread callout notation (e.g. M8x1.25, M10, 1/4-20 UNC) per ISO 6410 and ISO 129-1. If the geometry was created with a Part Design Hole feature that has thread parameters, it should read the thread specification automatically and offer it as a dimension type. Otherwise the user enters it manually as a text-based dimension. This is a common dimension type in practice and should not require workarounds with text notes.

**Error handling:**
- If the user selects geometry that cannot produce a valid dimension (e.g. a single vertex), the command stays in selection mode with a status bar hint or message
- If nominal value cannot be computed (e.g. linked geometry is a B-spline surface), the nominal field is blank and the user must enter it manually (=overwrite)

**Import/export:**
- Maps to OCCT XCAFDoc_Dimension / XCAFDimTolObjects_DimensionObject
- DimensionType, nominal value, upper/lower bounds, modifiers, qualifier, fit variance and grade all have direct OCCT enum mappings

---


### 5.8 Create Geometric Tolerance annotations (Feature Control Frames)

**User intent:** Specify form, orientation, location, runout, and profile requirements on model features. Per ISO 1101.

**Properties:**
- ToleranceType (Enumeration) = 16 types per ISO 1101, mapped to OCCT XCAFDimTolObjects_GeomToleranceType:
  - Form: Straightness, Flatness, Circularity, Cylindricity (+ Profiles can define form)
  - Orientation: Parallelism, Perpendicularity, Angularity
  - Location: Position, Concentricity, Coaxiality, Symmetry
  - Runout: CircularRunout, TotalRunout
  - Profile: ProfileOfLine, ProfileOfSurface
- ToleranceValue (Float) = tolerance zone width
- DiameterZone (Bool) = cylindrical tolerance zone (show diameter symbol)
- MaterialConditionRequirement (Enumeration): None, MMR (M), LMR (L)
- ReciprocityRequirement (Bool) = indicates the reciprocity requirement (R), only possible with MaterialConditionRequirement = MMR or LMR (not standalone)
- ZoneModifiers (StringList):
  - CZ (combined zone), SZ (separate zones)
  - UZ + offset value (unequally disposed zone)
  - OZ (offset zone)
  - ACS (any cross section), ALS (any longitudinal section)
  - UF (united feature)
- FeatureCount (Integer) = number of features sharing this tolerance (displayed as "8x" prefix before the FCF). Used together with CZ or SZ when a pattern of features shares the same positional tolerance.
- ProjectedToleranceZone (Bool) + ProjectedLength (Float) = P modifier
- FreeStateCondition (Bool) = F modifier per ISO 10579
- StatisticalTolerance (Bool) = ST modifier
- TangentPlane (Bool) = T modifier
- ContinuousFeature (Bool) = continuous, non-closed toleranced feature indicator (double arrow symbol <-->)
- RestrictedLength (Float, optional) = tolerance zone restriction in the form (t/...) = Limits the specification to a restricted length of the selected feature.
- EvaluationPlaneIndicator (Enumeration):
  - None
  - OrientationPlane
  - IntersectionPlane
  - CollectionPlane
- EvaluationPlaneReference (Link, optional) = datum plane, derived plane, coordinate plane, or other plane reference used by the selected indicator
- PrimaryDatum (Link) + PrimaryDatumModifiers (StringList)
- SecondaryDatum (Link) + SecondaryDatumModifiers (StringList)
- TertiaryDatum (Link) + TertiaryDatumModifiers (StringList)
- LinkedGeometry (LinkSub) = toleranced feature (face, edge, derived element)
- CompositeFrames (List of sub-frame data) = for composite tolerances per ISO 5458
- AnnotationPlane (Placement)
- LeaderPoints (VectorList)
- TextAbove (String), TextBelow (String) = optional above/below text
- AttachedToDimension (Link) = optional, renders the FCF below this dimension instead of using its own leader
- StackedWith (Link) = optional, another annotation on the same feature to stack with

**Command: PMI_AddGeometricTolerance**

**What the user selects first:** A face, edge, or vertex on the model. Optionally, also preselect datum objects. Sould work without preselection too.

**Task dialog contents:**

Section 1: References
- Geometry elements, optionally taken from preselection

Section 2: Tolerance Type
- Grid of 14 tolerance type icons, organized in rows by category (Form, Orientation, Location, Runout, Profile)
- Icons that are invalid for the current selection are greyed out / disabled or not shown (contextual logic: only present types that make sense)
- Clicking an icon selects the type

Section 3: Tolerance Value
- Numeric input for tolerance value
- Diameter zone checkbox (enabled only for applicable types)
- Material condition modifier dropdown (enabled only for features of size + applicable categories)


Section 4: Zone Modifiers
- Multi-select checkboxes for CZ, SZ, UZ (with value field), OZ, ACS, ALS, UF
- Projected zone checkbox + length field
- Free state, Statistical, Tangent plane checkboxes
- Continuous feature checkbox (double arrow symbol), shown only where a continuous non-closed toleranced feature is meaningful
- Zone restriction length field (activated when restricted tolerance is selected)
- Evaluation plane indicator selector: None, orientation plane, intersection plane, collection plane
- Evaluation plane reference field, enabled when an evaluation plane indicator is selected


Section 5: Datum References
- Three slots (Primary, Secondary, Tertiary)
- Each slot: dropdown to select from existing datum objects (or type letter)
- Each slot: modifier dropdown per datum reference
- For form tolerances: this entire section is hidden (no datums allowed)
- For orientation tolerances: at least primary required, others optional
- For location tolerances: at least primary required, typically all three
- For runout tolerances: at least one datum (typically one, defining the rotation axis)
- For profile tolerances: datums optional

Section 6: Composite (default collapsed)
- Button "Add Composite Row" (for multi-row feature control frames)
- Each row has its own tolerance value + datum references

Section 7: Preview
- Live rendering of the feature control frame symbol in the task dialog
- Preview of the annotation on the model

---

### 5.9 Selection logic and validity rules for geometric tolerances based on context (Tolerancing Advisor)

**User intent:** FreeCAD should propose valid geometrical specifications based on the selected 3D elements.

This is the contextual logic. When the user selects geometry, only standards-compliant tolerance types should be offered. Invalid types are greyed out in the dialog.

**Single planar face:**
- Valid form: Flatness, Straightness (requires direction element)
- Valid profile: ProfileOfSurface, ProfileOfLine
- If datums exist = valid orientation: Parallelism, Perpendicularity, Angularity
- If datums exist = valid location: Position (requires TEDs)
- NOT valid: Circularity, Cylindricity, Concentricity, CircularRunout, TotalRunout, Symmetry

**Single cylindrical face (feature of size):**
- Valid form: Cylindricity, Circularity, Straightness (surface line elements or axis)
- Valid profile: ProfileOfSurface, ProfileOfLine
- If datums exist = valid orientation: Parallelism, Perpendicularity, Angularity (axis vs. datum)
- If datums exist = valid location: Position (axis, requires TEDs), Concentricity/Coaxiality (same symbol), CircularRunout, TotalRunout
- Straightness on axis: allows diameter zone modifier and material condition modifier

**Single conical face:**
- Valid form: Circularity, Straightness (surface elements)
- Valid profile: ProfileOfSurface, ProfileOfLine
- If datums exist: Angularity, CircularRunout, TotalRunout

**Two parallel faces (tab/slot, feature of size):**
- Valid form: Flatness (individual faces), Straightness (center plane)
- If datums exist: Parallelism, Perpendicularity, Position, Symmetry (center plane)
- Straightness on center plane: allows material condition modifiers

**Single spherical face:**
- Valid form: Circularity (in any cross section)
- If datums exist: Position (center point, requires TEDs)

**Pattern of features (e.g. multiple holes selected):**
- If datums exist: Position (composite or single)
- CZ modifier auto-suggested for combined tolerance zone
- SZ suggested as alternative for separate zones

**Modifier availability rules (per ISO 2692 and ISO 1101):**

| Modifier | Availability |
|----------|-------------|
| Material condition (M, L) | ONLY for linear features of size (cylinders or two parallel opposite planes). ONLY for orientation, location, and runout tolerances. NEVER for form tolerances. |
| Reciprocity requirement `(R)` | ONLY together with M or L. NEVER standalone. ONLY for features of size (cylindrical features of size or features defined by two parallel opposite planes) |
| Projected zone `(P)` | Available for holes or similar features where mating parts extend beyond the surface |
| Free state `(F)` | Available when the part is declared non-rigid |
| Statistical `(ST)` | Available where statistical tolerancing is explicitly intended |
| Tangent plane `(T)` | Available for flatness and orientation of planar features |
| Diameter zone | Available when the tolerance zone is cylindrical |
| CZ / SZ | Available when multiple features share the same tolerance |
| OZ / UZ + value | Available for profile tolerances and other cases where offset or unequal disposition is defined |
| Continuous feature (double arrow) | Available for continuous, non-closed toleranced features |
| Restricted length `t/...` | Available when the tolerance applies only to a restricted part of the feature |
| Intersection plane indicator | Available for line profile in a specified direction and similar cases where the tolerance zone is evaluated in an identified plane |
| Orientation plane indicator | Available when the orientation of the evaluation plane must be explicitly defined |
| Collection plane indicator | Available when a set of features is interpreted collectively in a specified plane, especially in profile-related cases |

All around and all over are not zone modifiers inside the feature control frame. They are supplementary indications attached at the leader / feature indication level.

For profile specifications that apply to more than one single feature, all around and all over should be used together with UF, CZ, or SZ to avoid ambiguity.

**Datum reference validation rules (per ISO 1101):**

| Tolerance Category | Datum required? |
|-------------------|-----------------|
| Form (straightness, flatness, circularity, cylindricity) | NO. Datums cannot be specified |
| Orientation (parallelism, perpendicularity, angularity) | YES. At least one datum required |
| Location (position, concentricity, symmetry) | YES. At least one datum required. Position typically needs full datum system (A, B, C) |
| Runout (circular runout, total runout) | YES. At least one datum required (defining the rotation axis). Common datums like A-B allowed for compound rotation axis. |
| Profile (profile of line, profile of surface) | OPTIONAL. Without datums = form control only. With datums = form + orientation + location |

**Invalid combinations that must be blocked:**
- Datum reference in a form tolerance
- Material condition modifier on a non-feature-of-size
- Material condition modifier on a form tolerance
- Cylindrical tolerance zone (diameter symbol) on a non-axial feature
- Concentricity/coaxiality applied to a non-cylindrical or non-spherical feature
- Symmetry applied to a non-feature-of-size (non tab/slot)

---

### 5.10 Create Text, Note, and Leader annotations

**User intent:** Add text, general notes, flag notes, and leaders to the model

**PMI_Note properties:**
- Text (StringList) = multi-line text
- Frame (Enumeration): None, Rectangle, Flag (numbered flag note)
- LinkedGeometry (LinkSub) = optional attachment point
- LeaderPoints (VectorList) = optional leader
- FlagNumber (Integer) = for flag notes, auto-assigned
- AnnotationPlane (Placement)
- TextPosition (Vector)


**Command: PMI_AddNote**
- Click a point in 3D or on the annotation plane
- Type text in a text editor field
- Select frame style, leader attachment
- For flag notes: number auto-assigned, referenced in a legend table

**PMI_Leader properties:**
- StartPoint (Vector) = arrowhead position on geometry
- EndPoint (Vector) = text attachment point
- MidPoints (VectorList) = optional bend points for multi-segment leaders
- LinkedGeometry (LinkSub) = what the arrow points at
- ArrowType (Enumeration): Filled, Open, Dot, None
- AllAround (Bool) = specification applies to a continuous, closed toleranced feature
- AllOver (Bool) = specification applies all over the workpiece or all relevant surfaces

**Command: PMI_AddLeader**
- Click geometry first (arrow target), then click text/annotation endpoint
- Multi-segment leaders: click intermediate points


These are supplementary indications attached at the leader elbow or feature indication level, not part of the tolerance value or datum compartments.

Selection logic:
- AllAround is only valid when the leader identifies a closed contour or a closed periphery in the relevant interpretation plane
- AllOver is only valid when the specification applies to the complete part or all relevant surfaces 
- For profile specifications spanning more than one single feature, AllAround and AllOver should only be offered together with UF, CZ or SZ

---

### 5.11 Add Tables

**User intent:** Add structured table data to the annotation view, such as hole callout tables, tolerance tables, or revision history. Can use/import spreadsheet tables.

**Properties:**
- Rows (Integer)
- Columns (Integer)
- CellData (List of Lists of String)
- ColumnHeaders (StringList)
- LinkedAnnotations (LinkList) = optional references to annotations that feed data into cells
- AnnotationPlane (Placement)
- Position (Vector)

**Command: PMI_AddTable**
- Click anywhere on the active view annotation plane to place a table

**Behavior:**
- Tables are manually created and populated
- Future: tables could be auto-populated from annotation data (e.g. list all datums, list all tolerances for a feature) or imported from spreadsheet objects
- Tables appear on the annotation plane in the active view

**Open point:** Table auto-generation from PMI data is a future goal. Implement the manual table first.

---

### 5.12 Supplemental geometry (construction lines, center marks, axes)

ISO 16792 defines supplemental geometry as elements that aid the reading of annotations but are not part of the product geometry. This includes centerlines, center marks, axis lines, symmetry lines, and intersection curves.

**User intend:** Attach a dimension to the center of a hole pattern if there is no visible geometry. Define a datum on an axis if the axis is not displayed. In 2D drawings (TechDraw), center lines and center marks are already available. In 3D PMI, similar construction geometry is needed.

**What is needed:**
- Center line display for cylindrical features (drawn along the axis)
- Center mark for circular features (cross at the center)
- Axis display for features of size
- Symmetry line between two parallel faces

**Proposed approach:**
These are display-only elements, not model geometry. They should be objects under the AnnotationSet (or auto-generated from feature detection). CATIA FTA has explicit "Construction Geometry Creation" commands for this. A simpler approach: automatically show center lines / axes when a datum or dimension references a cylindrical or circular feature. User can toggle visibility. It could reuse existing Core Datum objects for that, as children under the PMI container.

This is not critical for a basic OMI implementation, if datums and dimensions can reference derived elements (like an axis) internally without needing a visible construction line. It becomes important for readability and for proper PMI to 2D TechDraw page workflow, where center lines are expected on every hole.

**Open point:** Auto-generated construction geometry, user created or both. CATIA does both (auto for common cases, manual for elements like intersection curves).

---

### 5.13 Surface texture specifications (later phase) 

**User intent:** Specify surface roughness requirements per ISO 21920 series standards.

This is out of scope for the first implementation but the document object model must accommodate it.

**What the object would need:**
- A surface texture annotation type with properties for parameter (Ra, Rz,...), value, filter type, cut-off wavelength, lay direction, machining allowance, and manufacturing process
- Reference to one face (or all around / all over via modifier)
- Rendering of the standard surface texture symbol (checkmark with horizontal line and extensions)
- TechDraw already has a command covering some of this

**Open point:** ISO 21920-1, ISO 21920-2 and ISO 21920-3 have replaced the withdrawn ISO 1302, ISO 4287, ISO 4288. The symbol has changed recently and wrong one is used in TechDraw.

The future implementation could also include information for Welds (PMI_Weld command) and Edge Symbols (PMI_Edge command).


---

### 5.14 Bind annotations to model geometry

**User intent:** Annotations maintain a stable, traceable link to the geometry they reference.

**Primary binding mechanism:**
- All geometry references use PropertyLinkSub: object reference + subelement name (e.g. ["Pad", "Face6"])
- The linked subelement always points to BRep geometry on the final shape (e.g. the shape of the tip of the Body)

**Secondary binding (optional metadata):**
- Store the Part Design feature name that created the geometry as an informational property (SourceFeature, Link). This is not used for geometric calculation but aids recovery when the primary reference breaks.
- Store the geometric center point and normal vector of the referenced face at creation time. This might allow future proximity based autorepair suggestions.

**What should be selectable:** 
- Faces (primary target for most annotations)
- Edges (for some dimension types, datum on an edge, profile of a line)
- Vertices (for point to point dimensions or datum target points)
- Part Design features themselves should NOT be the primary reference. Always resolve to BRep subelements. But the feature should be stored as secondary metadata (e.g. in the case for Thread dimension from the Hole tool) for more robust models.

**BRep references vs feature references:**
- STEP AP242 operates on Brep shape_aspects, not parametric features. BRep references enable lossless STEP exchange
- A feature can produce multiple faces. The user must indicate which specific face the annotation applies to
- When importing from STEP, there are no Part Design features to reference, only BRep

---

### 5.15 Repair broken references

**User intent:** When model edits break annotation geometry links, provide a repair workflow.

**Command: PMI_RepairBrokenReferences**

**Behavior:**
- Scans all PMI annotations in the document
- Lists annotations where LinkedGeometry no longer resolves (subelement name not found on the shape)
- For each broken annotation shows:
  - The annotation name and type
  - The old subelement reference (e.g. "Face6")
  - The stored backup data: geometric center, normal vector, Part Design feature name
  - Suggested candidates: faces near the stored center point, or faces belonging to the stored PartDesign feature
- The user clicks the correct geometry to rebind
- After rebinding, the annotation recalculates position and value

**Visual indication of broken annotations:**
- Red warning icon on the annotation in the tree
- The annotation remains visible in 3D at its last known position, but with a dashed/red rendering to indicate it is unresolved

**Prevention:**
- Always store backup metadata at creation time (center, normal, feature name)
- When the model is recomputed and references survive (TNP works),  update stored backup metadata to match the new geometry in the background

---

### 5.16 Recompute behavior when geometry changes

**User intent:** When the model was changed the recompute should not break PMI and should update nominal values automatically. Manually entered tolerances do not change. Leaders follow the geometry.

What happens when the model is edited and recomputed but the geometry references survive (TNP mitigated):

**Nominal values update automatically:** They are derived from geometry, not user input. If a pad goes from 30mm to 35mm, the dimension shows 35. No confirmation, no dialog. This is what CATIA, NX and SolidWorks all do and anything else would be unusable on a model with many dimensions.

**Tolerances stay as entered:** They are design intent. The +0.1/-0.05 stays +0.1/-0.05 regardless of the new nominl value. Same for geometric tolerance values, datum labels, modifiers, everything the user typed in manually.

**Fit designations stay but deviations get recalculated:** H7 stays H7, but the absolute deviations depend on the nominal size range per ISO 286-1. If the nominal crosses a range boundary (e.g. from 18mm to 35mm, which are in different ranges), the deviations change. The system recalculates silently. Optional: A small visual indicator on that dimension would be useful so the user notices the actual tolerance zone changed even though they didnt touch it.

**Leaders and attachment points follow the geometry:** If a face moves, the arrow tip moves with it. Text position stays relative to the reference point (or adjusts if the annotation plane moved).

**Annotation planes follow geometry if they were derived from it:** If the plane was aligned and attached to a face and that face moved, the plane follows. If it was placed manually or aligned to a coordinate plane, it stays. 

**What should NOT update automatically:**
- Tolerance values (user intent and not derived)
- Modifier selections
- Datum letters and references
- Text overrides

**Optional: "changed since last edit" indicator:** After recompute, annotations where the nominal value actually changed could get a overlay icon in the tree (small refresh icon or dot). Not a blocker, just information. Clears when the user opens the annotation or acknowledges it. Not critical for first implementation but a nice to have.

**Validation note:** The validation command could optionally flag dimensions where the tolerance to nominal ratio changed drastically after recompute (eg. a 0,01mm tolerance on what was a 10mm feature but is now 200mm). The system cannot judge design intent, but it can point out things that look suspicious.

---

### 5.17 Edit and modify existing annotations

**User intent:** Change any annotation after creation.

**Editing methods:**
- **Double click** an annotation in the tree or 3D view: opens the same task dialog used for creation, filled with current values
- **Property view**: shows all properties for direct editing
- **Drag** on the annotation plane in 3D view: repositions the annotation text and adjusts the leader line. It should never move the reference point.
- **Right click context menu:** Edit, Move to View, Add to View, Remove from View, Delete, Show Linked Geometry, Properties

**Rules:**
- Editing a datum letter that is referenced by geometric tolerances: prompt whether to update all referencing annotations automatically
- Changing linked geometry on a dimension: triggers recalculation of nominal value
- Changing a tolerance type on a geometric tolerance: revalidates all modifiers and datum references. Invalid ones are flagged or cleared with a warning.
- Deleting a datum that is referenced: confirmation dialog listing all affected annotations. If confirmed, datum references in those annotations are removed (shown as empty/missing).

***Open points:** 
- Copy annotation to feature: Applying the same tolerance specification to multiple similar features without recreating it each time. Select an existing annotation, pick target features, get copies with the same values but new geometry references. Useful for hole patterns or symmetric features.

---

### 5.18 Annotation stacking and attachment between annotations

**User intent:** Multiple annotations on the same feature are not floating independently. They are visually connected and stacked and moved as group.

**Stacked feature control frames:**
When multiple geometric tolerances apply to the same geometry, they stack vertically and share one leader. For example a hole might have cylindricity and position tolerances, shown as two FCF boxes on top of each other with one arrow pointing to the hole. Per ISO 1101 this is standard notation. Implementation: the GeometricTolerance object could have a StackedWith (Link) property pointing to another GeometricTolerance on the same feature, or the system auto-stacks when it detects multiple tolerances referencing the same geometry.

**Feature control frame attached to a dimension:**
Instead of its own leader a FCF can be placed directly below a dimension line. This means the tolerance applies to the feature that the dimension measures. E.g diameter dimension for a hole with position tolerance underneath. Implementation: the GeometricTolerance should have an AttachedToDimension (Link) property. Then the FCF renders below that dimension instead of getting its own leader. The geometry reference is inherited from the dimension.

**Datum indicator on a dimension line:**
When a datum triangle is placed on a dimension line (instead of directly on the surface), it means the dimensioned feature is the datum. This is the standard way to indicate datum features of size per ISO 5459. A datum on a diameter dimension means the datum is the axis. A datum on a distance dimension between two faces means the datum is the center plane. Implementation: the Datum object could have an AttachedToDimension (Link) property. When set, the triangle renders on the dimension line.

**Combined annotation block:**
A feature might end up with datum indicator + dimension + multiple tolerances as one visual unit. The rendering system needs to handle this as a stack: datum triangle on the dimension line, dimension value, then FCFs underneath, all connected by one leader. 

**Open point:** Decide between explicit attachment (user manually attaches FCF to dimension) vs. automatic stacking (system auto-groups annotations on the same geometry). CATIA does explicit attachment through the creation dialog. NX does a mix of both. Automatic stacking based on shared geometry reference is simpler to implement and covers most cases, but explicit attachment gives more control.

---

### 5.19 Control which annotations belong to which views

**User intent:** Manage which annotations are visible in each view.
 
**Mechanism:**
- When a View is active and the user creates an annotation, it is automatically added to that View's VisibleAnnotations
- The user can drag annotations between views in the tree
- If an Annotation is moved to another view, the reference point should move to the intersection of that view with the 3D model
- Right-click an annotation > "Manage View Membership": opens a dialog showing all views with checkboxes to include/exclude the annotation
- The same annotation can appear in multiple views (it is referenced, not owned)
- An annotation not in any view is "unassigned" and appears under the PMI container root, visible when no view is active


---

### 5.20 Validate Annotations

**User intent:** Validate and check all annotations in the active PMI Container against the governing standard and reports problems.

**PMI_ValidateAnnotations:**
WHat it checks:
ISO Standards compliance:
- Geometric tolerances with missing required datum references (eg parallelism without a datum)
- Datum references in form tolerances
- Material condition modifiers on non features of size or on form tolerances
- Diameter zone symbol on non-axial features
- Concentricity on non-cylindrical geometry
- Symmetry on non features of size
- Position or profile tolerance referencing dimensions that are not marked as basic/TED
- Incomplete datum systems for position tolerances (only primary where primary + secondary + tertiary would be expected for full constraint)
- Runout tolerance without a datum defining the rotation axis
- Evaluation plane indicator used without a valid plane reference
- Orientation / intersection / collection plane indicator used on an incompatible tolerance type
- Continuous feature indicator used on a closed toleranced feature where all around or all over would be required instead
- Restricted length t/... used with zero or negative value

Completeness: 
- Dimensions without tolerance but non-TED (warning, not error, sometimes intended)
- Datums that are defined but never referenced by any geometric tolerance
- Geometric tolerances where the tolerance value is zero or negative
- Annotations with broken geometry links
- Annotations referencing deleted datums
- Annotations not assigned to any view

After recompute:
- Dimensions where the nominal changed significantly since the tolerance was last edited (large ratio change)
- Fit designations where the nominal crossed an ISO 286-1 size range boundary (deviations recalculated, user may not have noticed)

**Output:**
A report dialog (in the task panel) with one row per issue. Each row shows: severity (error/warning/info), annotation name, issue description, and a clickable link that selects and zooms to the annotation in the 3D view.

Errors are things that violate the standard (eg datum in a form tolerance). Warnings are things that look wrong but might be intentional (eg. dimension without tolerance). Info is just helpful (datum defined but unused).

**Open point:** The exact set of checks will grow over time. Important are: invalid combinations and broken references. The completeness checks are nice to have.

---

### 5.21 Query specifications for a selected feature

**User intent:** Select a face, edge, vertex, or feature and see all PMI specifications that apply to it or depend on it.

This is the reverse direction of the contextual selection logic when adding specifications to answers what is already defined on the current selection.

**PMI_QueryFeatureSpecifications**

**What the user selects first:** One or more geometric elements on the model, typically:
- a face
- an edge
- a vertex
- multiple faces representing one feature of size

**Behavior:**
- The command collects and lists all annotations that are directly or indirectly associated with the selected geometry
- The result is shown in a task panel
- Selecting one result in the list highlights the corresponding annotation in 3D view and in the tree
- This command should work even if no PMI View is active

**What should be listed in the result:**
- Dimensions that reference the selected geometry
- Geometric tolerances that apply to the selected geometry
- Basic dimensions that are related to those geometric tolerances
- Datum features attached to the selected geometry
- Datum systems that include these datums
- Notes and leaders attached to the selected geometry
- Annotations that are attached indirectly through a referenced dimension
- The Views in which each annotation is visible
- Validation state of each annotation, if invalid or broken

**Direct and indirect relationship logic:**
- Direct means the selected geometry is explicitly referenced by the annotation e.g. a:
  - diameter dimension linked to the cylindrical face of a hole
  - datum feature attached to a planar face 
  - position tolerance whose toleranced feature is the selected hole
- Indirect means the annotation is functionally related through another semantic object, e.g. a:
  - hole face, show the position tolerance, the basic dimensions used to locate it, and the datum features referenced by that tolerance
  - planar datum feature face, show all geometric tolerances that reference datum A
  - diameter dimension, show the feature control frame attached below it
- The command should clearly distinguish direct and indirect results in the UI

**Task panel contents:**
- Selection summary
  - selected object name
  - selected subelement name
  - detected feature type if recognized
- Result groups:
  - Directly applied specifications
  - Related basic dimensions
  - Referenced datums and datum systems
  - Indirectly related specifications
  - Notes and supplemental annotations
  - Visible in views
- For each result:
  - annotation name
  - annotation type
  - short value summary
  - linked view count
  - validation state
- Actions:
  - Show only these annotations (isolate)
  - Select linked geometry
  - Go to annotation
  - Open annotation for editing
  - Export result as report, later phase

---

### 5.22 Derive TechDraw pages from PMI Views

**User intent:** Generate 2D technical drawings from 3D PMI annotations for human readability / export

**Command: PMI_DeriveTechDrawPage**

**What the user selects:** One or more PMI Views

**Behavior:**
- A new TechDraw Page is created.
- For each selected PMI View, a TechDraw view is added:
  - Projection direction from View's CameraDirection
  - Scale auto-calculated or user-specified
  - Visible objects from View's VisibleObjects
  - Clipping planes applied as section cuts
- PMI annotations are propagated to the TechDraw view

**Open Points**
- Import views as individual pages with one view per page
- Use imports as static objects (like a SVG)

**Parametric link:**
- TechDraw objects maintain a link back to the PMI annotation
- If the PMI annotation value changes, the TechDraw representation updates
- Direction: one-way, PMI > TechDraw. Changes in TechDraw do not change back to PMI


---

### 5.23 STEP AP242 Import

**User intent:** Open STEP AP242 files from other CAD systems and see their PMI annotations in FreeCAD.

**Technical approach (discussion with Dimitrii):**
- FreeCAD's Import module already uses OCCT's STEPCAFControl_Reader. Currently, GDT mode is not enabled. Change: call reader.SetGDTMode(true) before transfer
- After geometry transfer, traverse the XDE label tree via XCAFDoc_DimTolTool:
  - GetDimensionLabels() > create PMI_Dimension objects
  - GetGeomToleranceLabels() > create PMI_GeometricTolerance objects
  - GetDatumLabels() > create PMI_Datum objects
- Map each OCCT data object's properties to FreeCAD PMI object properties using the enum mappings listed in the appendix
- Resolve STEP shape_aspect references to FreeCAD BRep sub-element names
- Read draughting_model entities to create PMI_View objects with camera parameters and annotation assignments
- Read graphical PMI (tessellated_annotation_occurrence) as fallback visualization when semantic data is incomplete
- Create a PMI AnnotationSet to hold all imported data

**Challenges:**
- Different CAD systems export different PMI completeness levels. Some write only graphical PMI (polylines), some only semantic, some both. The importer must handle all cases.
- Geometry reference resolution: STEP shape_aspects must map to specific TopoDS_Shape sub-elements, then to FreeCAD subelement names. OCCT's XDE label tree provides this mapping.
- View reconstruction: STEP saved views store camera + annotation references, but the camera model may differ from FreeCAD (eg Z-up convention). Translation may not be exact.

**Testing:**
- [NIST](https://www.mbx-if.org/home/cax/resources/) provides public PMI test models for STEP AP242 PMI validation


---

### 5.24 STEP AP242 Export

**User intent:** Export the annotated model to STEP AP242 with machine-readable PMI data.

**Technical approach (discussion with Dimitrii):**
- Set STEP schema to AP242DIS on STEPCAFControl_Writer
- Enable tolerance writing: writer.SetDimTolMode(true)
- For each PMI object, populate the corresponding OCCT XDE label:
  - PMI_Dimension > XCAFDoc_Dimension with XCAFDimTolObjects_DimensionObject
  - PMI_GeometricTolerance > XCAFDoc_GeomTolerance with XCAFDimTolObjects_GeomToleranceObject
  - PMI_Datum > XCAFDoc_Datum with XCAFDimTolObjects_DatumObject
- Map FreeCAD sub-element references back to STEP shape_aspects
- Write saved views as draughting_model entities
- Write annotation planes

**Graphical PMI generation:**
- OCCT commercial PMI Visualization Component can generate graphical PMI
- The open source path requires generating tessellated polyline representations of annotation symbols manually. This could be a lot of effort.
- Acceptable initial approach: semantic-only export. Graphical PMI as a later phase.
- Both semantic and graphical are recommended by CAx-IF for interoperability

**Workflow requirement and testing:**
- Import a STEP AP242 file, make no changes, export. All PMI data should survive identically
- Import, modify one annotation, export. Unmodified annotations should survive, modified one should reflect changes

---

#### 5.24.1 JT, PRC / 3D PDF and QIF export (later phase)

STEP AP242 should remain the primary format for semantic (and graphical) CAD + PMI exchange. Besides STEP AP242 other standardized exchange formats could be supported later as follow-up:

- JT is relevant as a lightweight 3D format and can also carry PMI which makes it useful for review, supplier and large assembly workflows where a lighter exchange format is preferred
- PRC / 3D PDF is relevant as a publishing and documentation format. It is useful for sharing annotated 3D models for review, communication and downstream consumption without requiring a CAD system. It could reuse defined PMI views as named PDF views or create individual pages per PMI view (needs more specification)
- QIF overlaps with PMI and is used to handover data into quality, inspection and metrology workflows (not general CAD model exchange)

---

### 5.25 Semantic data access for other workbenches

**User intent:** Other FreeCAD workbenches and addons can read PMI data to make informed decisions.

**Examples of other workbench use:**
- CAM: Read tolerance value on a hole to select appropriate tool, feeds and strategy. Like for example a 0.01 mm position tolerance requires different toolpaths than 0.1 mm.
- Future tolerance analysis addon: Read all dimensions and tolerances for stack-up calculations in an assembly

**Required Python API (to be documented):**
Not from a coder but what would make sense:
- Get all annotations, filtered by type
- Get annotations for a feature
- Get datum info (label, linked geometry)
- Get dimension info (nominal, tolerance, modifiers,...)
- Get tolerance info (type, value, references, modifiers,...)
- Properties also accessible via standard access like obj.PropertyName

---

### 5.26 Undo/Redo and WB switching

**Undo/redo:** All PMI operations (create, edit, delete, move between views, rebind geometry) must be registered in the transaction system. Undoing a datum creation that a geometric tolerance already references should undo both, at least leave the tolerance in a state where the missing datum is flagged.

**Workbench switching:** When the user switches away from the PMI workbench, annotations should stay visible in the 3D view. If a PMI View was active, it gets deactivated on workbench switch (camera and clipping revert to normal). The user can toggle PMI visibility globally via View menu regardless of active workbench.


---

## 6. Proposed Document Object Model

| Object Type | Parent | Purpose |
|-------------|--------|---------|
| PMI_AnnotationSet | Document root (sibling to Body/Part but also possible as child of Part or Assembly) | Container for all PMI data |
| PMI_View | AnnotationSet | Named camera + annotation filter + clipping |
| PMI_ClippingPlane | AnnotationSet | Persistent visual clipping plane |
| PMI_Datum | AnnotationSet (referenced by Views) | Datum feature indicator |
| PMI_DatumReferenceFrame | AnnotationSet | Datum system (A, B, C combination)  |
| PMI_Dimension | AnnotationSet (referenced by Views) | Size, distance, or angle specification |
| PMI_GeometricTolerance | AnnotationSet (referenced by Views) | Feature control frame |
| PMI_Note | AnnotationSet (referenced by Views) | Text, flag note |
| PMI_Leader | AnnotationSet (referenced by Views) | Leader line connecting to geometry |
| PMI_Table | AnnotationSet (referenced by Views) | Tabular data |
| PMI_ConstructionGeometry | AnnotationSet | Center lines, axes, center marks (display-only) |
| PMI_SurfaceTexture | AnnotationSet (referenced by Views, later phase) | Surface roughness/waviness |
| PMI_Weld | AnnotationSet (referenced by Views, later phase) | Welding information |
| PMI_Edge | AnnotationSet (referenced by Views, later phase) | Edge symbols |

Annotations are stored under the AnnotationSet and referenced (appear as children) by Views. They are not "owned" by Views. This allows sharing annotations across multiple views (e.g. display a Datum in multiple views).

---

## 7. Annotation Categories for ISO GPS Support

### 7.1 Datums and Datum Systems per ISO 5459
- Simple datums (A, B, C, ...) on faces, edges, vertices
- Common datums (A-B) from multiple features
- Datum targets (point, line, rectangle, circle, area) with individual numbering
- Datum reference frames (hierarchical datum systems)

### 7.2 Dimensional Specifications per ISO 14405-1, ISO 14405-3, ISO 129-1
- Linear sizes (diameter, radius, thickness, curve length)
- Location distances (linear, angular, curved)
- ISO 286-1 fit designations (H7, g6,...)
- 24 specification modifiers per ISO 14405-1
- Theoretically exact dimensions (basic/TED)

### 7.3 Geometric Tolerances (Macrogeometrical Specifications) per ISO 1101
- 14 tolerance symbols across 5 categories
- Material condition modifiers per ISO 2692
- Zone modifiers (CZ, SZ, UZ, OZ, ACS, ALS, UF)
- Projected tolerance zone, free state, statistical, tangent plane
- Composite tolerances per ISO 5458
- Supplementary indications for continuous and restricted toleranced features
- Evaluation plane indicators: orientation plane, intersection plane, collection plane
- Full feature control frame rendering

### 7.4 Profile Tolerances per ISO 1660
- Profile of a line, profile of a surface
- Unilateral (inward, outward) and unequally bilateral zones
- With and without datum references
- Line profile in a specified direction using an intersection plane indicator
- Profile specifications using collection plane indication
- All around / all over indications together with UF, CZ, or SZ where the specification spans more than one single feature

### 7.5 Text Annotations
- Free text notes
- Table notes
- Flag notes (numbered, with legend)
- General tolerance declarations per ISO 22081
- Title block annotations

### 7.6 Leaders
- Single and multi-segment leader lines
- Arrow types (filled, open, dot, none)
- Connecting annotations to geometry

### 7.7 Surface Texture per ISO 21920 series
- Parameter, value, filter, cut-off, lay direction, process
- Surface texture symbol rendering

---

## 8. Missing Symbols and Modifiers per ISO GPS

The following symbols must be created (SVG for TechDraw, geometry for 3D or render the filled SVG or used from a Font). Existing TechDraw symbols cover some but not all.


**Geometric characteristic symbols (ISO 1101):**
All 14 standard symbols are already in TechDraw

**Modifier symbols that must be added, most from ISO 1101**
- All ISO 14405-1 specification modifier circles: LP, GG, GX, GN, GC, CC, CA, CV, SX, SN, SA, SM, SR, SD, SQ (Text with dynamic frame)
- UZ (unequally disposed zone)
- OZ (offset zone)
- UF (united feature)
- All around symbol (circle on leader elbow)
- All over symbol (two circles on leader elbow)
- Between symbol (double arrow between indicators)
- Intersection plane indicator
- Orientation plane indicator
- Collection plane indicator
- Direction feature indicator
- Continuous feature indicator (double arrow symbol)
- Restricted length indication t/... (text only)

**Datum symbols:**
- Filled triangle with leader (ISO 5459). TechDraw implementation is OK
- Datum letter in rectangular frame. TechDraw implementation is bad
- Datum target indicator (divided circle, per ISO 5459)
- Movable datum target symbol (per ISO 5459)

**Dimension notation:**
- Basic/TED frame (rectangle around value), per ISO 1101. Also here the frame in TechDraw is bad
- Countersink, counterbore, depth symbols, per ISO 129-1. Some already in TechDraw
- ISO fit designation rendering (e.g. 30 H7), per ISO 286-1. This is text only
- Altered default (AD in circle) per ISO 8015

**Additional symbols for future expansion**
- Welding symbols
- Surface finish
- Edge symbols




---

## 9. Suggested Implementation Phases

**Phase 1: Basics**
- PMI workbench  (menus, toolbar)
- Preferences page (standard selection, display settings)
- PMI_AnnotationSet container object
- PMI_View object with camera restore and visibility filter
- PMI_ClippingPlane object (or use of implemented saved views/clipping planes)
- View activation/deactivation UX

**Phase 2: Datums and Dimensions**
- PMI_Datum object with creation dialog and rendering
- PMI_Dimension object with auto-detection from geometry
- Tolerance input (plus/minus, limits, fit designation)
- ISO 14405-1 modifier support
- Basic/TED dimensions
- Symbol library (core set per ISO)
- Leader objects

**Phase 3: Geometric Tolerances**
- PMI_GeometricTolerance object
- Tolerancing advisor logic (contextual / type filtering)
- All 14 tolerance types
- Modifier support (material conditions, zone modifiers)
- Composite tolerances
- Datum reference validation
- Validation command

**Phase 4: STEP AP242 Import**
- Enable GDT mode in STEP reader
- Import dimensions, geometric tolerances, datums
- Import saved views
- NIST test model validation

**Phase 5: STEP AP242 Export**
- Semantic PMI export to AP242
- Round-trip testing (import test model and export without changes)
- Graphical PMI generation (future goal)

**Phase 6: TechDraw Integration**
- PMI View to TechDraw page derivation
- Parametric update from 3D to 2D

**Phase 7: Polish and Extensions**
- Broken reference repair tool 
- Query element tool
- General tolerance notes (ISO 22081)
- Surface texture specifications (ISO 21920)
- Table annotations
- Further annotations (weld, joints, ...)
- Further file format support: JT import/export (code should be already in [main](https://github.com/FreeCAD/FreeCAD/tree/main/src/Mod/JtReader/App)), PRC / 3D PDF, QIF export

---

## 10. Open Topics and Risks

- **TNP:** PMI annotations depend on stable geometry references. TMP mitigation  improves stability but edge cases remain. PMI must be tested against model edit scenarios. Risk: annotations break silently after parametric edits.

- **Graphical PMI generation:** OCCT commercial PMI Visualization Component generates compliant graphical presentation. The open-source alternative requires manual polyline tessellation of all annotation symbols. This is a significant effort with high standards compliance risk. Risk: semantic-only export limits interoperability with viewers that support only graphical PMI.

- **OCCT version dependency:** AP242 PMI support requires minimum OCCT 7.6. The export of Views for AP242 is not supported in 8.0 (import is). Dimitrii plans to add it in the next version.

- **Annotation placement algorithm:** Automatic layout to avoid overlaps (in both 3D and TechDraw derivation) seems to be non trivial. Initial implementation should allow manual placement with dragging. Auto-layout is a future goal.

- **Composite tolerance rendering:** Multi-row feature control frames have complex layout rules (not relevant for semantic use)

- **Assembly PMI:** ISO 16792 support PMI at the assembly level (tolerances across multiple parts). This proposal focuses on part-level PMI. Assembly PMI can be a future extension.



---

## Appendix A: OCCT Enumeration Mapping Reference

For STEP AP242 FreeCAD PMI object properties must map to OCCT XCAFDimTolObjects enumerations, based on chat with Dimitrii:

| OCCT Enumeration | Values | Maps to |
|------------------|--------|---------|
| DimensionType | 31 values | PMI_Dimension.DimensionType |
| GeomToleranceType | 16 values (14 standard symbols) | PMI_GeometricTolerance.ToleranceType |
| DatumTargetType | 5 values | PMI_Datum.DatumType |
| DimensionModif | 24 values | PMI_Dimension.SpecificationModifiers |
| GeomToleranceModif | 16 values | PMI_GeometricTolerance.ZoneModifiers |
| GeomToleranceMatReqModif | 3 values (None, Maximum, Least) | PMI_GeometricTolerance.MaterialConditionModifier |
| DimensionQualifier | 4 values (None, Min, Max, Avg) | PMI_Dimension.Qualifier |
| DimensionFormVariance | 28 values (A-ZC) | PMI_Dimension.FitClass |
| DimensionGrade | 20 values (IT01-IT18) | PMI_Dimension.FitGrade |
| DatumSingleModif | 22 values | PMI_Datum.Modifiers |
| DatumModifWithValue | 5 values | PMI_Datum modifier with associated value |

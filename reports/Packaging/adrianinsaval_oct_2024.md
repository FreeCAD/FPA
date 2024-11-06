* published FreeCAD 1.0RC2 on flathub-beta along with other improvements to the package https://github.com/flathub/org.freecad.FreeCAD/pull/2
* triggered migration from org.freecadweb.FreeCAD to org.freecad.FreeCAD for flathub-bet package https://github.com/flathub/org.freecadweb.FreeCAD/pull/137
* upgraded qt to 5.15.15 on conda-forge, and backported a potential fix for the crash reported at https://github.com/FreeCAD/FreeCAD/issues/17308: https://github.com/conda-forge/qt-main-feedstock/pull/236 https://github.com/conda-forge/qt-webengine-feedstock/pull/69 https://github.com/conda-forge/qt-wayland-feedstock/pull/31 https://github.com/conda-forge/pyside2-feedstock/pull/250
* rebuild other related conda packages needed for freecad bundles
* upgraded weekly builds to occt 7.8.1 and qt 5.15.15
* upgraded appimagetool version being used for creating appimage bundles, resulting in better compression and dropping requirement of libfuse2 on the user's system.
* correspondingly updated download page about this change https://github.com/FreeCAD/FreeCAD-Homepage/pull/202
* tracking https://github.com/AppImage/type2-runtime/pull/37 to implement on our builds if not merged in time for release. This affects users of some systems where fuermount is not in /usr/bin but just in /bin
* fixed graphviz not working by default on some platforms https://github.com/FreeCAD/FreeCAD/pull/17121
* fixed release blocker issue #16687
* fixed failing openscad test failing on flatpak by default https://github.com/FreeCAD/FreeCAD/pull/17540, investigating how to improve compatibility in flatpak.
* updated ci lint action for ubuntu 24.04 https://github.com/FreeCAD/FreeCAD/pull/17171
* help on identifying root cause of https://github.com/flathub/org.freecad.FreeCAD/issues/4 and https://github.com/flathub/org.freecad.FreeCAD/issues/5, fixes incoming
* https://github.com/FreeCAD/FreeCAD-snap/pull/131
* attempted adding wayland support to appimages, but it seems coin3d is not yet fully ready for wayland despite working on some systems. Reverted until this is fixed in coin.
* cleaned issues on FreeCAD-Bundle repo
* cleaned packages in freecad conda repo

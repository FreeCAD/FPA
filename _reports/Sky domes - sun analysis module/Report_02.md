# Sky domes, sun radiations analysis module

FPA Grant to Francisco Rosa

## Report 2, 2025/12/03

This second report on the development of sun radiations analysis by sky domes in FreeCAD is described in two subjects: procedures acquired, and results.

Continuing the work of the Solar Workbench, which focuses on applying the resources available in the Python ladybug library, we have completed the second part dedicated to developing an application of colored sky domes as diagrams for recording and analyzing solar radiation from a specific geographic location over a given period of time.

## 1. Procedures acquired

Our main work procedures consisted of the following steps:

  • Improving the application of ladybug code resources for producing solar analysis domes, specially the modules: ladybug.legend, ladybug_radiance.skymatrix, and ladybug_radiance.visualize.skydome. We decided to create a separate Solar module, the Lbcomponents for this propose. In this manner, it will be possible to use those ladybug function in more than one Solar tools.
    
  • Creating the functions to modify the SkyDomes in every possible configurations.
    
  • Developing the dialog window for configuration of the creation and modification of SkyDomes. 
    
So, the code for the sky domes was consisted in four documents with three modules and an XML file for the configuration window.

The first of these, containing the dome classes and the main set of functions, is the  Skydomes.py,  the second and third are the SkyDomesDialog.py  and Skydomes.ui, and the last is a common one, the LBComponents.py, as we commented.

## 2. Results

Now, it is possible with the SkyDomes tools to create, configured and modify extensively and completely through its dialog window the following properties:

  • Diagrams of solar radiation of a specific location over a given period, distributed as total, direct, and diffuse values ​​in kWh/m².
    
  • Diagrams of solar irradiance of a specific location over a given period, distributed as total, direct, and diffuse values ​​in W/m².
    
  • The domes can be presented in two models: Tregenza with 144 patches (low resolution), and Reinhart (high resolution) with 576 patches.
    
  • We got a two new features with the ladybug.legend. Now, we can apply no one, but 32 sets of color for a legend and we can configure the number of its colors.
    
It is important to note that the sky domes is fundamental for the understanding and use of future modules of sun analysis. The resulting data of their patch vectors are used to calculate the solar radiation and irradiation over a site, for example.

The Solar Workbench with the new features can be downloaded at: https://github.com/Francisco-Rosa/Solar/tree/updates

#Notes on converting gnuCash Html to Github Markdown

gnuCash produces reports that look nice on paper or on the screen, but merging them into a Github markdown document is troublesome

gnuCash will send reports to paper, Pdf or Html. When gnuCash produces reports as Html, it makes extensive use of nested tables.  Github
markdown (as used in the FPA Handbook) has only rudimentary support for tables. 

To make the conversion, 2-3 tools are required:
- an Html editor such as SeaMonkey to remove table nesting
- LibreOffice Writer to align table cells and produce a MediaWiki document
- a online conversion service such as https://alldocs.app/convert-mediawiki-markup-to-markdown to convert from MediaWiki to Github markdown.

This process will require a number of iterations to get everything lined up.

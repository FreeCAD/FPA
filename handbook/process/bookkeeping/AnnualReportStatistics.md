# Annual Report Statistics and Financial Reports

## Manditory Financial Reports
The FPA is required to produce two financial reports each year.  These are specified in 
("Annexe 8 : Schéma des comptes annuels des associations et fondations qui tiennent une comptabilité
simplifiée.") [https://www.cnc-cbn.be/fr/node/2247].

The numbers for these two reports can be generated using the saved gnuCash reports 
"L'Etat Du Patrimoine" (a modified balance sheet) and "Etat des recettes et dépenses" (a modified
income statement).


#Annual Report Statistics
Statistical exhibit creation follows a simple process:
* export the relevant transactions from gnuCash to a csv file
* massage the exported transactions with python scripts
* run R scripts to generate the charts

An example - create a pie chart of revenue sources
* extract transactions from the Recettes accounts
  * producing donsetlegs2023.csv
* we want more detail on revenue sources, so we add collection platform information
  * python3 ./gcExportAddPlatform.py donsetlegs2023.csv txExportWithPlatform.csv
* run gnuCashTxExportToCommonFormat.py to convert the exported "splits" into single line transactions.
  * python3 ./gnuCashTxExportToCommonFormat.py txExportWithPlatform.csv commonDataOut.csv
* we also want to know about corporate donors, so we add this information
  * python3 ./commonAddCorporate.py commonDataOut.csv outputCommonWithCorp.csv
* insert CommonDataHeader.csv at the top of outputCommonWithCorp.csv so R will know the column names
  * producing inputForR2023Dons.csv
* now we run DonationsByPlatform.r in RStudio to generate our chart.
    


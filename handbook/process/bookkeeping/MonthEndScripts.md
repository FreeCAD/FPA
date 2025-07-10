# Month End Scripts

We do our "cash basis" accounting at the end of each month using a number of python scripts.

![Month End OverView](./MonthEndProcessingOverView.svg)

First, we need to get transaction files for the month from each of PayPal, OpenCollective and BNP Paribas.

Next, we need to use python scripts to turn the data files into double entry "split" files which will be imported into
GnuCash.

[OpenCollective tx file](./OpenCollectiveTransactionProcessing.md)
python3 splitmaker_OC.py OCMay2025.csv OCImport.csv

[PayPal tx file](./PayPalTransactionProcessing.md)
python3 streamsplitter_PP.py PPMay2025.csv PPDonationStream.csv PPTransferStream.csv PPManualStream.csv
python3 splitmaker_PPDonation.py PPDonationStream.csv PPDonationImport.csv

[BNP tx file](./BNPTransactionProcessing.md)
python3 streamsplitter_BNP.py BNPMay2025.csv BNPDonationStream.csv BNPTransferStream.csv BNPWithdrawalStream.csv
python3 splitmaker_BNPDon.py BNPDonationStream.csv BNPDonationImport.csv
python3 splitmaker_BNPFee.py BNPWithdrawalStream.csv BNPFeeImport.csv

[Weekly Transfers](./WeeklyTransferProcessing.md)
python3 splitmaker_WeeklyTransfers.py weeklyTransfers.csv weeklyTransfersImport.csv

[Regular monthly payments](./MonthlyPaymentProcessing.md)
python3 splitmaker_MonthlyDepenses.py monthlyWorksheet.csv monthlyDepensesImport.csv

Next, we import the xxxxxImport.csv files into [gnuCash](https://gnucash.org/docs/v5/C/gnucash-manual/trans-import.html).

The scripts are available in the [FPA Github repo](https://github.com/FreeCAD/FPA/tree/main/code/bookkeepingScripts)



# Process for posting transactions on OpenCollective to the FPA accounts.

![OpenCollective Processing](./OpenCollectiveTransactionProcessing.svg)

## To obtain a csv file of transactions on the FPA Open Collective account, 
* log in to your Open Collective account
* click on you account icon in the upper right
* select the FreeCAD organization
* select "Budget" and "Transactions"
* select "Transactions" from the drop-down menu
* select a date range and click "Download CSV"
* the csv file will be downloaded as "freecad-transactions.csv"

## To build the double entry transactions for PayPal to be imported into gnuCash, use a splitmaker script:
    python3 splitmaker_OC.py freecad-transactions.csv OC_TXIMPORT.csv

### Sample Output

    splitmaker_OC input file: freecad-transactions_OC.csv
    splitmaker_OC output file: OC_TXIMPORT.csv
    splitmaker_OC records in: 9
    splitmaker_OC records out: 24


The splitmaker scripts produce multiple line items for each transaction input.  Each line represents a change to a
single account (Open Collective balance, fees expense, currency conversion, etc).  These lines are called "splits" by gnuCash.


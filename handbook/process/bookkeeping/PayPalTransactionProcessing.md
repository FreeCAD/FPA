# Process for posting transactions on the PayPal account to the FPA accounts.

![OpenCollective Processing](./PayPalTransactionProcessing.svg)

## To obtain a csv file of transactions on the FPA PayPal account:
* log in to the FPA PayPal account
* click "All Reports" at the top of the page
* click "Activity Report" on the left side menu
* select a date range and click "Create Report"
* a notice will be sent to your fpa.org email
* log in to the FPA PayPal account
* click "All Reports"
* select the csv file from the list of available downloads

## To build the double entry transactions for PayPal to be imported into gnuCash

### First, use the streamsplitter script:
    python3 streamsplitter_PP.py PayPal.csv PayPal_Constributions.csv PayPal_Transfers.csv  PayPal_Manuals.csv

This will produce three csv files from the input:
* contribution (donation) transactions,
* transfer transactions, and,
* transactions requiring manual intervention, which may include: 
    * disputed items
    * reversals
    * anything else that the streamsplitter can not categorize.

### Second, use the splitmaker scripts:
    python3 splitmaker_PPContrib.py PayPal_Constributions.csv PayPal_ContributionSplits.csv
    python3 splitmaker_PPTransfer.py PayPal_Transfers.csv PayPal_TransferSplits.csv

The splitmaker scripts produce multiple line items for each transaction input.  Each line represents a change to a
single account (PayPal balance, fees expense, currency conversion, etc).  These lines are called "splits" by gnuCash.

The output from the splitmakers can be imported into gnuCash.

### Third, handle the exceptions:
The streamsplitter will report on any transactions that can not be identified as a contribution or a transfer.  These 
must be handled on a case by case basis.

The splitmakers will report on any input that can not be handled.  These transactions must be 
addressed on a case by case basis.


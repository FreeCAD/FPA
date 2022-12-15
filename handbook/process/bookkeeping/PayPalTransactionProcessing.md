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

## To build the double entry transactions for PayPal to be imported into gnuCash, use a splitmaker script:
    python3 splitmaker_PP.py PayPal.csv PayPal_TXIMPORT.csv

### Sample Output
    splitmaker_PP input file: PP_test_transactions.csv
    splitmaker_PP output file: PayPal_TXIMPORT.csv
    splitmaker_PP records in: 10
    splitmaker_PP records out: 45


The splitmaker scripts produce multiple line items for each transaction input.  Each line represents a change to a
single account (PayPal balance, fees expense, currency conversion, etc).  These lines are called "splits" by gnuCash.


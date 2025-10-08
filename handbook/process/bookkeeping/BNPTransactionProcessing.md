# Process for posting transactions on the BNP bank account to the FPA accounts.

![BNP Processing](./BNPTransactionProcessing.svg)

## A csv file of transactions on the BNP account can be obtained from [Yorik] on request.  This file must be split into various types of transactions for posting:
* donations in (direct and via Github), 
* weekly transfers in from PayPal, and,
* withdrawals out. These are split into:
    * bank fee transactions that can be imported automatically, and, 
    * other withdrawals that need to be handled manually, such as grant payouts or infrastructure  bills.
	    


## To separate BNP csv into donations in (direct and Github) and withdrawals out, use the streamsplitter script:
    python3 streamsplitter_PP.py PPAug2025.csv PPDonationStream.csv PPTransferStream.csv PPManualStream.csv

### Sample output:
    streamsplitter_BNP input file: BNPAug2025.csv
	streamsplitter_BNP non-paypal deposit output file: BNPDonationStream.csv
	streamsplitter_BNP paypal transfer output file: BNPTransferStream.csv
	streamsplitter_BNP withdrawal output file: BNPWithdrawalStream.csv
	streamsplitter_BNP records in: 57
	streamsplitter_BNP donation records out: 44
	streamsplitter_BNP transfer records out: 4
	streamsplitter_BNP withdrawal records out: 8

Note that the transfer file is no longer used for month end processing.

### The streamsplitter script produces intermediate transaction files with this layout:
    Data, Description, Amount, Type, TransactionNumber

## To build the double entry transactions for bank fees to be imported into gnuCash and identify withdrawals that need manual handling, use a splitmaker script:
    python3 splitmaker_BNPFee.py BNPWithdrawalStream.csv BNPFeeImport.csv

### Sample output:
    splitmaker_BNPFee input file: BNPWithdrawalStream.csv
	splitmaker_BNPFee output file: BNPFeeImport.csv
	splitmaker_BNPFee - record: 0 date: 2025-08-21 needs manual handling - amount: -1,00 desc: Altan type: Domiciliation
	etc
	etc
	splitmaker_BNPFee - record: 7 date: 2025-08-13 needs manual handling - amount: -0,01 desc:  type: Paiement par carte de crédit
	splitmaker_BNPFee records in: 8
	splitmaker_BNPFee records out: 0


## To build the double entry transactions for donations to be imported into gnuCash, use a splitmaker script:
    python3 splitmaker_BNPDon.py BNPDonationStream.csv BNPDonationImport.csv

### Sample output:
    splitmaker_BNPDon input file: BNPDonationStream.csv
	splitmaker_BNPDon output file: BNPDonationImport.csv
	splitmaker_BNPDon records in: 44
	splitmaker_BNPDon records out: 88


The splitmaker scripts produce multiple line items for each intermediate transaction input.  Each line represents a change to a single account.  These lines are called "splits" by gnuCash.



#!/usr/bin/python3

# input csv of PayPal transactions and output csv of contribution (donation) tx
#                                             csv of transfer related tx and
#                                             csv of tx requiring further manual intervention 
# usage: python3 streamsplitter_PP.py inputTransactions.csv payments.csv transfers.csv manuals.csv

import csv
import sys
import random


#convert values from ',' decimal separator to '.'.
def commaToPoint(inValue):
    outValue = inValue
    outValue = outValue.replace(",", ".")          # replace all ',' by ','
    outValue = outValue.replace(".", "", outValue.count(".") -1)  # remove all but last '.'
    return outValue

iDate = 0
iDesc = 3
iType = 4
iCurrency = 6
iGross = 7
iFee = 8
iNet = 9

inputFileName = "PPManualTx.csv"
paymentFileName = "PPTestPaymentTx.csv"
transferFileName = "PPTestTransferTx.csv"
manualFileName = "PPTestManual.csv"

if len(sys.argv) < 5:
    print("streamsplitter_PP: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    paymentFileName = sys.argv[2]
    transferFileName = sys.argv[3]
    manualFileName = sys.argv[4]
    print("streamsplitter_PP input file: {0}".format(inputFileName))
    print("streamsplitter_PP payment file: {0}".format(paymentFileName))
    print("streamsplitter_PP transfer file: {0}".format(transferFileName))
    print("streamsplitter_PP manual file: {0}".format(manualFileName))

recordsIn = 0
paymentsOut = 0
transfersOut = 0
manualsOut = 0

transferToken = "General Withdrawal"
conversionToken = "General Currency Conversion"
paymentToken = "Payment"
refundToken = "Refund"

paymentOut = open(paymentFileName, 'w', newline='')
paymentWriter = csv.writer(paymentOut, delimiter=',')
transferOut = open(transferFileName, 'w', newline='')
transferWriter = csv.writer(transferOut, delimiter=',')
manualOut = open(manualFileName, 'w', newline='')
manualWriter = csv.writer(manualOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if recordsIn == 0:
            #header line
            recordsIn += 1
            continue

        recordsIn += 1
        grossValue = float(commaToPoint(line[iGross]))
        # payments
        if paymentToken in line[iType] and refundToken not in line[iType]:
            if grossValue < 0:
                # probably a "General Payment" to another PayPal account
                manualWriter.writerow(line)
                manualsOut += 1
                continue
            paymentWriter.writerow(line)
            paymentsOut += 1
            continue

        # transfers
        if transferToken in line[iType]:
            transferWriter.writerow(line)
            transfersOut += 1
            continue

        # conversions  (normally? related to transfers
        if conversionToken in line[iType]:
            transferWriter.writerow(line)
            transfersOut += 1
            continue

        # must be a manual
        manualWriter.writerow(line)
        manualsOut += 1

print("streamsplitter_PP records in: {0}".format(recordsIn))
print("streamsplitter_PP payments out: {0}".format(paymentsOut))
print("streamsplitter_PP transfers out: {0}".format(transfersOut))
print("streamsplitter_PP manuals out: {0}".format(manualsOut))

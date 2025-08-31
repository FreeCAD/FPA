#!/usr/bin/python3

# input csv of PayPal transactions and output csv of donation tx
#                                             csv of tx requiring further manual intervention 
# usage: python3 streamsplitter_PP.py PPMonthlyTransactions.csv donations.csv manuals.csv

# change: transfer records are no longer produced as they must be handled manually to get the 
# exchange rates right.

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
donationFileName = "PPTestPaymentTx.csv"
#transferFileName = "PPTestTransferTx.csv"
manualFileName = "PPTestManual.csv"

if len(sys.argv) < 4:
    print("streamsplitter_PP: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    donationFileName = sys.argv[2]
#    transferFileName = sys.argv[3]
    manualFileName = sys.argv[3]
    print("streamsplitter_PP input file: {0}".format(inputFileName))
    print("streamsplitter_PP donation file: {0}".format(donationFileName))
#    print("streamsplitter_PP transfer file: {0}".format(transferFileName))
    print("streamsplitter_PP manual file: {0}".format(manualFileName))

recordsIn = 0
donationsOut = 0
transfersOut = 0
manualsOut = 0

transferToken = "General Withdrawal"
# file seems to have changed as of June 2023 records.  Conversions are now tagged 
# as "User Initiated Currency Conversion" and the order of records has changed
# with the conversion records coming before the withdrawal record.
#conversionToken = "General Currency Conversion"
conversionToken = "Currency Conversion"
donationToken = "Payment"
refundToken = "Refund"
AcceptedCurrencies = ["EUR", "USD"]

donationOut = open(donationFileName, 'w', newline='')
donationWriter = csv.writer(donationOut, delimiter=',')
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

        # oddball currencies
        if not line[iCurrency] in AcceptedCurrencies:
            print("Non-standard currency near input record: {0} date: {1} amount: {2}".format(recordsIn, line[iDate], grossValue))
            manualWriter.writerow(line)
            manualsOut += 1
            continue
            
        # donations
        if donationToken in line[iType] and refundToken not in line[iType]:
            if grossValue < 0:
                # probably a "General Payment" to another PayPal account
                print("Probable pay out near input record: {0} date: {1} amount: {2}".format(recordsIn, line[iDate], grossValue))
                print("    desc: {0}  currency: {1}".format(line[iDesc], line[iCurrency]))
                manualWriter.writerow(line)
                manualsOut += 1
                continue
            donationWriter.writerow(line)
            donationsOut += 1
            continue

        # transfers
        if transferToken in line[iType]:
            print("Bank transfer out near input record: {0} date: {1} amount: {2}".format(recordsIn, line[iDate], grossValue))
            manualWriter.writerow(line)
            transfersOut += 1
            continue

        # conversions  (normally? related to transfers)
        if conversionToken in line[iType]:
            print("Currency conversion near input record: {0} date: {1} amount: {2}".format(recordsIn, line[iDate], grossValue))
            manualWriter.writerow(line)
            transfersOut += 1
            continue

        # must be a manual
        print("Mystery record encountered near input record: {0} date: {1} amount: {2}".format(recordsIn, line[iDate], grossValue))
        print("    desc: {0}  currency: {1}".format(line[iDesc], line[iCurrency]))
        manualWriter.writerow(line)
        manualsOut += 1

print("streamsplitter_PP records in: {0}".format(recordsIn))
print("streamsplitter_PP donations out: {0}".format(donationsOut))
print("streamsplitter_PP transfers out: {0}".format(transfersOut))
print("streamsplitter_PP manual handling records transfers: {0} other: {1}".format(transfersOut, manualsOut))

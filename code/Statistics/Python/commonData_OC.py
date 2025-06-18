#!/usr/bin/python3

# input downloaded csv of OpenCollective primary transactions and output csv in common donation format
# NOTE: OpenCollective tx are completely in USD
# usage: python3 commonData_OC.py inputFile.csv outputFile.csv

import csv
import sys
import random

iDate = 0
iDesc = 3
iType = 4   # CREDIT/DEBIT
iKind = 5   # CONTRIBUTION/HOST_FEE/EXPENSE
iValue = 10
iFee1 = 11

inputFileName = "inTXOC.csv"
outputFileName = "outTxOC.csv"

if len(sys.argv) < 3:
    print("commonData_OC: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("commonData_OC input file: {0}".format(inputFileName))
    print("commonData_OC output file: {0}".format(outputFileName))

recordsIn = 0
recordsOut = 0

inAccount = "Recettes:Dons et legs:Donations In USD"
offsetAccount = "Avoirs:Valeurs disponibles:OpenCollective"
tradingInAccount = "Trading:CURRENCY:USD"
tradingOutAccount = "Trading:CURRENCY:EUR"
feeAccount = "Depenses:Autres dépenses:Fees and Commissions:OpenCollective Commission"
commodityStringUSD = "CURRENCY::USD"
commodityStringEUR = "CURRENCY::EUR"
contributionToken = "CONTRIBUTION"
hostfeeToken = "HOST_FEE"
expenseToken = "EXPENSE"
creditToken = "CREDIT"
debitToken = "DEBIT"
platformToken = "OC"
conversionRate = 0.921    # this has to match the USD price in gnuCash Price db
serviceRate = 0.248        # this is an approximation for when the input doesn't include fees
reverseValue = -1.0
txCounterStart = random.randint(7000, 8000)

csvOut = open(outputFileName, 'w', newline='')
csvWriter = csv.writer(csvOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if recordsIn == 0:
            #header line
            recordsIn += 1
            continue
        recordsIn += 1
        baseValue = float(line[iValue]) * conversionRate
        reversedValue = baseValue * reverseValue
        dateString = line[iDate] [0:10]     # 2022-12-05 06:18:02 to 2022-12-05
        transactionId = txCounterStart + recordsIn
        if creditToken in line[iType]:
            row = [dateString] + [commodityStringEUR] + [line[iDesc]]+ [offsetAccount] + [baseValue] + [transactionId] + [platformToken]
            csvWriter.writerow(row)
            recordsOut += 1

print("commonData_OC records in: {0}".format(recordsIn))
print("commonData_OC records out: {0}".format(recordsOut))


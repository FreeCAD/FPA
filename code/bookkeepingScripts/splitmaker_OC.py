#!/usr/bin/python3

# input downloaded csv of OpenCollective primary transactions and output csv of full split transactions
# NOTE: OpenCollective tx are completely in USD
# usage: python3 splitmaker_OC.py inputFile.csv outputFile.csv
#python3 splitmaker_OC.py OC_Dec2022_testTXIN.csv OC_Dec2022_testTXOUT.csv

import csv
import sys
import random

iDate = 1
iDesc = 7
iValue = 4
iFee1 = 11
iFee2 = 12

inputFileName = "inTXOC.csv"
outputFileName = "outTxOC.csv"

if len(sys.argv) < 3:
    print("splitmaker_OC: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("splitmaker_OC input file: {0}".format(inputFileName))
    print("splitmaker_OC output file: {0}".format(outputFileName))

recordsIn = 0
recordsOut = 0
splitsPerTx = 3

inAccount = "Recettes:Dons et legs:Donations In USD"
offsetAccount = "Avoirs:Valeurs disponibles:OpenCollective"
tradingInAccount = "Trading:CURRENCY:USD"
tradingOutAccount = "Trading:CURRENCY:EUR"
feeAccount = "Depenses:Autres dépenses:Fees and Commissions:OpenCollective Commission"
commodityString = "CURRENCY::USD"
conversionRate = 0.9665    # this has to match the USD price in gnuCash Price db
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

        #line 1 - basic transaction USD
        baseValue = float(line[iValue])
        reversedValue = baseValue * reverseValue
        dateString = line[iDate] [0:10]     # 2022-12-05 06:18:02 to 2022-12-05
        row = [dateString] + [commodityString] + [line[iDesc]]+ [inAccount] + [reversedValue] + [txCounterStart + recordsIn]
        csvWriter.writerow(row)

        #line 2 - fee deduction USD & net amount USD
        feeAmount = baseValue * serviceRate   #USD
        if len(line) > iFee1:
            feeAmount = abs(float(line[iFee1]))
        if len(line) > iFee2:
            feeAmount += abs(float(line[iFee2]))
        netValue = baseValue - feeAmount      #USD
        row = [""] + [""] + [""] + [feeAccount] + [feeAmount] + [txCounterStart + recordsIn] #USD
        csvWriter.writerow(row)
        
        #line 3 - net to offset account (OpenCollective Balance) USD
        offsetValue = netValue
        row = [""] + [""] + [""] + [offsetAccount] + [offsetValue] + [txCounterStart + recordsIn]
        csvWriter.writerow(row)

        recordsIn += 1
        recordsOut += splitsPerTx
 
print("splitmaker_OC records in: {0}".format(recordsIn))
print("splitmaker_OC records out: {0}".format(recordsOut))


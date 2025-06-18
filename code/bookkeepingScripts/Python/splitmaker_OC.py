#!/usr/bin/python3

# input downloaded csv of OpenCollective primary transactions and output csv of full split transactions
# NOTE: OpenCollective tx are completely in USD
# usage: python3 splitmaker_OC.py inputFile.csv outputFile.csv

import csv
import sys
import random

#iDate = 0
#iDesc = 3
#iType = 4   # CREDIT/DEBIT
#iKind = 5   # CONTRIBUTION/HOST_FEE/EXPENSE
#iValue = 10
#iFee1 = 11

# a different OC format as of 2025?
# 1 line for donation, separate lines for fees
iDate = 0
iDesc = 2
iType = 3   # CREDIT/DEBIT
iKind = 4   # CONTRIBUTION/HOST_FEE/EXPENSE
iValue = 6
iFee1 = 11

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
contributionToken = "CONTRIBUTION"
hostfeeToken = "HOST_FEE"
expenseToken = "EXPENSE"
processorToken = "PAYMENT_PROCESSOR_FEE"

serviceRate = 0.06        # this is an approximation host fee for when the input doesn't include fees
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
        baseValue = float(line[iValue])
        reversedValue = baseValue * reverseValue
        dateString = line[iDate] [0:10]     # 2022-12-05 06:18:02 to 2022-12-05
        transactionId = txCounterStart + recordsIn
        if contributionToken in line[iKind]:
            #line 1 - basic transaction USD
            row = [dateString] + [commodityString] + [line[iDesc]]+ [inAccount] + [reversedValue] + [transactionId]
            csvWriter.writerow(row)

# line 2 only applies to the original data format.
#            #line 2 - fee deduction USD
#            feeAmount = baseValue * serviceRate   #USD
#            if len(line) > iFee1:
#                feeAmount = abs(float(line[iFee1]))
#            netValue = baseValue - feeAmount      #USD
#            row = [""] + [""] + [""] + [feeAccount] + [feeAmount] + [transactionId] #USD
#            csvWriter.writerow(row)
            feeAmount = 0
            netValue = baseValue
            
            #line 3 - net to offset account (OpenCollective Balance) USD
            offsetValue = netValue
            row = [""] + [""] + [""] + [offsetAccount] + [offsetValue] + [transactionId]
            csvWriter.writerow(row)

            recordsOut += splitsPerTx
            continue;
        if hostfeeToken in line[iKind]:
            #line 1 - charge to OC Fees
            row = [dateString] + [commodityString] + [line[iDesc]]+ [feeAccount] + [reversedValue] + [transactionId]
            csvWriter.writerow(row)
            #line 2 - reduce balance
            row = [""] + [""] + [""] + [offsetAccount] + [baseValue] + [transactionId]
            csvWriter.writerow(row)
            recordsOut += 2
            continue
            
        if processorToken in line[iKind]:
            #line 1 - charge to OC Fees
            row = [dateString] + [commodityString] + [line[iDesc]]+ [feeAccount] + [reversedValue] + [transactionId]
            csvWriter.writerow(row)
            #line 2 - reduce balance
            row = [""] + [""] + [""] + [offsetAccount] + [baseValue] + [transactionId]
            csvWriter.writerow(row)
            recordsOut += 2
            continue
        
        if expenseToken in line[iKind]:
            print("splitmaker_OC - record: {0} date: {1} amount: {2} fee: {3} desc: {4} - expense record".format(recordsIn, dateString, line[iValue], line[iFee1], line[iDesc]))

print("splitmaker_OC records in: {0}".format(recordsIn))
print("splitmaker_OC records out: {0}".format(recordsOut))


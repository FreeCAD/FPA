#!/usr/bin/python3

# input csv of exported gnuCash transactions and output csv in common format
# usage: python3 gnuCashTxExportToCommonFormat.py inputTransactions.csv commonDataOut.csv

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
iCurrency = 5
iAccount = 9
iAmount = 12
iPlatform = 16

inputFileName = "exportTx.csv"
outputFileName = "commonData.csv"

if len(sys.argv) < 3:
    print("gnuCashTxExportToCommonFormat: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("gnuCashTxExportToCommonFormat input file: {0}".format(inputFileName))
    print("gnuCashTxExportToCommonFormat output file: {0}".format(outputFileName))

recordsIn = 0
paymentsOut = 0

commodityStringUSD = "CURRENCY::USD"
commodityStringEUR = "CURRENCY::EUR"

OCAccountToken = "Avoirs:Valeurs disponibles:OpenCollective"
BNPAccountToken = "Avoirs:Valeurs disponibles:BNP"
PPAccountToken = "Avoirs:Valeurs disponibles:PayPal"

corporateToken = "corp"

conversionRate = 0.921    # this should match the price in gnuCash Price db
serviceRate = 0.10        # this is an approximation for when the input doesn't include fees
reverseValue = -1.0
txCounterStart = random.randint(15000, 16000)

paymentOut = open(outputFileName, 'w', newline='')
paymentWriter = csv.writer(paymentOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if recordsIn == 0:
            #header line
            recordsIn += 1
            continue

        recordsIn += 1
        if line[iDesc] == "":
            continue        # offset half of transaction - not interesting
            
        grossValue = float(commaToPoint(line[iAmount])) * reverseValue

        if line[iCurrency] == commodityStringUSD:
            grossValue = grossValue * conversionRate        # to EUR
        transactionId = txCounterStart + recordsIn
#        if recordsIn % 100 == 0:
#            print("gnuCashTxExportToCommonFormat - recordsIn: {0}".format(recordsIn))

        # date,currency,description,account,value,id,platform,corporate
        row = [line[iDate]] + [line[iCurrency]] + [line[iDesc]]+ [line[iAccount]] + [grossValue] + [transactionId] + [line[iPlatform]] + [corporateToken]

        paymentWriter.writerow(row)
        paymentsOut += 1


print("gnuCashTxExportToCommonFormat records in: {0}".format(recordsIn))
print("gnuCashTxExportToCommonFormat payments out: {0}".format(paymentsOut))


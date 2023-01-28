#!/usr/bin/python3

# input csv of PayPal withdrawal and output csv of full split transactions including conversion
# we expect each withdrawal to consist of 3 records
#           a General Withdrawal record in EUR (-)for the amount withdrawn
#           a Currency Conversion record in USD (+) for the amount withdrawn, and,
#           an offsetting Currency Conversion record in EUR (-)
# we can build our splits from the first 2 records 
# usage: python3 splitmaker_PPTransfer.py inputPairs.csv splits.csv

import csv
import sys
import random

#convert dates from PP format of dd/mm/yyyy to standard yyyy-mm-dd
def convertDate(inDate):
    if len(inDate) < 10:
        today = date.today()
        return today.strftime("%Y-%m-%d")
    year = inDate[6 : 10]
    month = inDate[3 : 5]
    day = inDate[0 : 2]
    newDate = year + '-' + month + '-' + day
    return newDate

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

inputFileName = "inPairsPP.csv"
splitFileName = "splitsPP.csv"

if len(sys.argv) < 3:
    print("splitmaker_PPTransfer: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    splitFileName = sys.argv[2]
    print("splitmaker_PPTransfer input file: {0}".format(inputFileName))
    print("splitmaker_PPTransfer split file: {0}".format(splitFileName))

recordsIn = 0
splitsOut = 0

fromAccount = "Avoirs:Valeurs disponibles:PayPal"
toAccount = "Avoirs:Valeurs disponibles:BNP"
tradingAccountUSD = "Trading:CURRENCY:USD"
tradingAccountEUR = "Trading:CURRENCY:EUR"
commodityStringUSD = "CURRENCY::USD"
commodityStringEUR = "CURRENCY::EUR"
withdrawalToken = "Withdrawal"
conversionToken = "Conversion"
EURToken = "EUR"
USDToken = "USD"

conversionRate = 0.921    # this has to match the price in gnuCash Price db
serviceRate = 0.094        # this is an approximation for when the input doesn't include fees
reverseValue = -1.0
txCounterStart = random.randint(17000, 18000)

splitOut = open(splitFileName, 'w', newline='')
splitWriter = csv.writer(splitOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    cacheLine = None
    for line in csvReader:
        recordsIn += 1
        transactionId = txCounterStart + recordsIn
        date = convertDate(line[iDate])
        desc = "Transfer"

        # skip along until we hit a withdrawal record
        if not withdrawalToken in line[iType]:
            continue

        conversion1 = next(csvReader)  # usually the USD record
        if not conversionToken in conversion1[iType]:
            print("records out of sequence (1) near: {0}".format(recordsIn))
            sys.exit()
        conversion2 = next(csvReader)  # usually the EUR record
        if not conversionToken in conversion2[iType]:
            print("records out of sequence (2) near: {0}".format(recordsIn))
            sys.exit()
        
        valueUSD = float(commaToPoint(conversion1[iGross]))
        if USDToken not in conversion1[iCurrency]:
            valueUSD = float(commaToPoint(conversion2[iGross]))
        valueEUR = float(commaToPoint(conversion2[iGross]))
        if EURToken not in conversion2[iCurrency]:
            valueEUR = float(commaToPoint(conversion1[iGross]))       
        recordsIn += 2

        #line 1 out - withdraw from PayPal in USD
        row = [date] + [commodityStringUSD] + [desc] + [fromAccount] + [valueUSD] + [transactionId]
        splitWriter.writerow(row)
        splitsOut += 1

        #line 2 - deposit to BNP in EUR
        row = [""] + [""] + [desc] + [toAccount] + [valueEUR] + [transactionId]
        splitWriter.writerow(row)
        splitsOut += 1

        #line 3 - currency conversion USD
        row = [""] + [""] + [desc] + [tradingAccountUSD] + [valueUSD * -1.0] + [transactionId]
        splitWriter.writerow(row)
        splitsOut += 1

        #line 4 - currency conversion EUR
        row = [""] + [""] + [desc] + [tradingAccountEUR] + [valueEUR * -1.0] + [transactionId]
        splitWriter.writerow(row)
        splitsOut += 1

print("splitmaker_PPTransfer records in: {0}".format(recordsIn))
print("splitmaker_PPTransfer splits out: {0}".format(splitsOut))

            

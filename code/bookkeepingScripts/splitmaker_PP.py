#!/usr/bin/python3

# input csv of PayPal primary transactions and output csv of full split transactions
# NOTE: PayPal tx are completely in mixeed currency
# usage: python3 splitmaker_PP.py inputFile.csv outputFile.csv
#        python3 splitmaker_PP.py PP_Dec2022_testTXIN.csv PP_Dec2022_testTXOUT.csv
import csv
import sys
import random

#convert dates from BNP format of dd/mm/yyyy to standard yyyy-mm-dd
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
def convertValue(inValue):
    outValue = inValue
    outValue = outValue.replace(",", ".")          # replace all ',' by ','
    outValue = outValue.replace(".", "", outValue.count(".") -1)  # remove all but last '.'
    return outValue

iDate = 0
iDesc = 3
iValue = 7
iFee = 8

inputFileName = "inTxPP.csv"
outputFileName = "outTxPP.csv"

if len(sys.argv) < 3:
    print("splitmaker_PP: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("splitmaker_PP input file: {0}".format(inputFileName))
    print("splitmaker_PP output file: {0}".format(outputFileName))

recordsIn = 0
recordsOut = 0
splitsPerTx = 5

inAccount = "Recettes:Dons et legs:Donations In USD"
offsetAccount = "Avoirs:Valeurs disponibles:PayPal"
tradingInAccount = "Trading:CURRENCY:USD"
tradingOutAccount = "Trading:CURRENCY:EUR"
feeAccount = "Depenses:Autres dépenses:Fees and Commissions:PayPal Cashout"
commodityString = "CURRENCY::USD"
conversionRate = 0.9665    # this has to match the price in gnuCash Price db
serviceRate = 0.094        # this is an approximation for when the input doesn't include fees
reverseValue = -1.0
txCounterStart = random.randint(9000, 10000)

csvOut = open(outputFileName, 'w', newline='')
csvWriter = csv.writer(csvOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if recordsIn == 0:
            #header line
            recordsIn += 1
            continue

        date = convertDate(line[iDate])
        baseAmount = float(convertValue(line[iValue]))
        if baseAmount < 0:
            # withdrawals require manual handling to avoid duplication with BNP transactions
            print("record: {0} amount: (1} requires manual handling".format(recordsIn, baseAmount))
            recordsIn += 1
            continue
        
        #line 1 - basic transaction USD
        reversedValue = baseAmount * reverseValue
        row = [date] + [commodityString] + [line[iDesc]]+ [inAccount] + [reversedValue] + [txCounterStart + recordsIn]
        csvWriter.writerow(row)

        #line 2 - fee deduction USD & net amount USD
        feeAmount = baseAmount * serviceRate   #USD
        if len(line) > iFee:
            feeAmount = abs(float(convertValue(line[iFee])))
        feeExchanged = feeAmount * conversionRate      #EUR
        netValue = baseAmount - feeAmount      #USD
        row = [""] + [""] + [""] + [feeAccount] + [feeExchanged] + [txCounterStart + recordsIn] #EUR
        csvWriter.writerow(row)
        
        #line 3 - net to offset account (PayPal Balance) EUR
        offsetValue = netValue * conversionRate
        row = [""] + [""] + [""] + [offsetAccount] + [offsetValue]  + [txCounterStart + recordsIn]
        csvWriter.writerow(row)

        #line 4 - currency conversion in
        tradingInValue = reversedValue * -1.0
        row = [""] + [""] + [""] + [tradingInAccount] + [tradingInValue] + [txCounterStart + recordsIn]
        csvWriter.writerow(row)

        #line 5 - currency conversion out
        tradingOutValue = (offsetValue + feeExchanged) * -1.0 
        row = [""] + [""] + [""] + [tradingOutAccount] + [tradingOutValue] + [txCounterStart + recordsIn]
        csvWriter.writerow(row)

        recordsIn += 1
        recordsOut += splitsPerTx

print("splitmaker_PP records in: {0}".format(recordsIn))
print("splitmaker_PP records out: {0}".format(recordsOut))

            

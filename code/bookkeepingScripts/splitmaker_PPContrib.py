#!/usr/bin/python3

# input csv of PayPal contribution transactions and output csv of full split transactions for ready for import
#                                           
# NOTE: PayPal tx are in various currencies
# usage: python3 splitmaker_PPContrib.py contributionTx.csv splits.csv

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

inputFileName = "PPTestContribTx.csv"
contribFileName = "PPTestContribImport.csv"

if len(sys.argv) < 3:
    print("splitmaker_PPContrib: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    contribFileName = sys.argv[2]
    print("splitmaker_PPContrib input file: {0}".format(inputFileName))
    print("splitmaker_PPContrib contrib file: {0}".format(contribFileName))

recordsIn = 0
contribsOut = 0
generalDropped = 0
splitsPerDeposit = 3

# donations to PayPal are reported in USD (but with ',' decimal point!)
inAccount = "Recettes:Dons et legs:Donations In USD"
offsetAccount = "Avoirs:Valeurs disponibles:PayPal"
bankAccount = "Avoirs:Valeurs disponibles:BNP"
tradingInAccount = "Trading:CURRENCY:USD"
tradingOutAccount = "Trading:CURRENCY:EUR"
feeAccount = "Depenses:Autres dépenses:Fees and Commissions:PayPal Transaction Fees"
commodityStringUSD = "CURRENCY::USD"
commodityStringEUR = "CURRENCY::EUR"
paymentToken = "Payment"
refundToken = "Refund"

conversionRate = 0.921    # this has to match the price in gnuCash Price db
serviceRate = 0.10        # this is an approximation for when the input doesn't include fees
reverseValue = -1.0
txCounterStart = random.randint(15000, 16000)

contribOut = open(contribFileName, 'w', newline='')
contribWriter = csv.writer(contribOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if recordsIn == 0:
            #header line
            recordsIn += 1
            continue

        recordsIn += 1
        date = convertDate(line[iDate])
        baseAmount = float(commaToPoint(line[iGross]))

        if paymentToken in line[iType] and refundToken not in line[iType]:
            # this is (probably) a normal contrib transaction
            #line 1 - basic donation transaction
            reversedValue = baseAmount * reverseValue
            row = [date] + [commodityStringUSD] + [line[iDesc]]+ [inAccount] + [reversedValue] + [txCounterStart + recordsIn]
            contribWriter.writerow(row)

            #line 2 - fee deduction USD
            feeAmount = baseAmount * serviceRate   #USD
            if len(line) > iFee:
                feeAmount = abs(float(commaToPoint(line[iFee])))
            row = [""] + [""] + [line[iDesc]] + [feeAccount] + [feeAmount] + [txCounterStart + recordsIn] #EUR
            contribWriter.writerow(row)
            
            #line 3 - net to offset account (PayPal Balance) USD
            netValue = commaToPoint(line[iNet])
            row = [""] + [""] + [line[iDesc]] + [offsetAccount] + [netValue]  + [txCounterStart + recordsIn]
            contribWriter.writerow(row)

            contribsOut += splitsPerDeposit

print("splitmaker_PPContrib records in: {0}".format(recordsIn))
print("splitmaker_PPContrib contribs out: {0}".format(contribsOut))

            

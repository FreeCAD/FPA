#!/usr/bin/python3

# input csv of PayPal transactions and output csv of donations in common format
# usage: python3 commonData_PP.py inputTransactions.csv commonData.csv

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

inputFileName = "PPTx.csv"
paymentFileName = "PPCommonData.csv"

if len(sys.argv) < 3:
    print("commonData_PP: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    paymentFileName = sys.argv[2]
    print("commonData_PP input file: {0}".format(inputFileName))
    print("commonData_PP payment file: {0}".format(paymentFileName))

recordsIn = 0
paymentsOut = 0

inAccount = "Recettes:Dons et legs:Donations In USD"
offsetAccount = "Avoirs:Valeurs disponibles:PayPal"
bankAccount = "Avoirs:Valeurs disponibles:BNP"
tradingInAccount = "Trading:CURRENCY:USD"
tradingOutAccount = "Trading:CURRENCY:EUR"
feeAccount = "Depenses:Autres dépenses:Fees and Commissions:PayPal Transaction Fees"
commodityStringUSD = "CURRENCY::USD"
commodityStringEUR = "CURRENCY::EUR"
transferToken = "General Withdrawal"
conversionToken = "General Currency Conversion"
paymentToken = "Payment"
refundToken = "Refund"
platformToken = "PP"

conversionRate = 0.921    # this has to match the price in gnuCash Price db
serviceRate = 0.10        # this is an approximation for when the input doesn't include fees
reverseValue = -1.0
txCounterStart = random.randint(15000, 16000)

paymentOut = open(paymentFileName, 'w', newline='')
paymentWriter = csv.writer(paymentOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if recordsIn == 0:
            #header line
            recordsIn += 1
            continue

        recordsIn += 1
        grossValue = float(commaToPoint(line[iGross])) * conversionRate
        dateString = convertDate(line[iDate])
        transactionId = txCounterStart + recordsIn
        if recordsIn % 100 == 0:
            print("commonData_PP - recordsIn: {0}".format(recordsIn))
        # payments
        if paymentToken in line[iType] and refundToken not in line[iType]:
            if grossValue < 0:
                # probably a "General Payment" to another PayPal account
                continue

            row = [dateString] + [commodityStringEUR] + [line[iDesc]]+ [offsetAccount] + [grossValue] + [transactionId] + [platformToken]
            paymentWriter.writerow(row)
            paymentsOut += 1


print("commonData_PP records in: {0}".format(recordsIn))
print("commonData_PP payments out: {0}".format(paymentsOut))


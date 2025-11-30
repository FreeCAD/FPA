#!/usr/bin/python3

# input csv of PayPal donation transactions and output csv of full split transactions for ready for import
#                                           
# NOTE: PayPal tx are in various currencies
# usage: python3 splitmaker_PPDonation.py PPDonationStream.csv PPDonationImport.csv

import csv
import sys
import random
import datetime

#convert dates from PP format of dd/mm/yyyy to standard yyyy-mm-dd
def convertDate(inDate):
    inDate = inDate.strip()

    if not inDate:
        today = datetime.date.today()
        return today.strftime("%Y-%m-%d")

    try:
        dt = datetime.datetime.strptime(inDate, "%d/%m/%Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        today = datetime.date.today()
        return today.strftime("%Y-%m-%d")

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

inputFileName = "PPTestDonatTx.csv"
donatFileName = "PPTestDonatImport.csv"

if len(sys.argv) < 3:
    print("splitmaker_PPDonat: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    donatFileName = sys.argv[2]
    print("splitmaker_PPDonat input file: {0}".format(inputFileName))
    print("splitmaker_PPDonat donat file: {0}".format(donatFileName))

recordsIn = 0
donatsOut = 0
generalDropped = 0
splitsPerDeposit = 3

# donations to PayPal are reported in USD (but with ',' decimal point!)
inAccount = "Recettes:Dons et legs:Donations In USD"
offsetAccount = "Avoirs:Valeurs disponibles:PayPal USD"
bankAccount = "Avoirs:Valeurs disponibles:BNP"
tradingInAccount = "Trading:CURRENCY:USD"
tradingOutAccount = "Trading:CURRENCY:EUR"
feeAccount = "Depenses:Autres dépenses:Fees and Commissions:PayPal Transaction Fees"
commodityStringUSD = "CURRENCY::USD"
commodityStringEUR = "CURRENCY::EUR"
paymentToken = "Payment"
refundToken = "Refund"

serviceRate = 0.10        # this is an approximation for when the input doesn't include fees
reverseValue = -1.0
txCounterStart = random.randint(15000, 16000)

donatOut = open(donatFileName, 'w', newline='', encoding='utf-8-sig')
donatWriter = csv.writer(donatOut, delimiter=',', quoting=csv.QUOTE_MINIMAL)

with open(inputFileName, encoding='utf-8-sig', newline='') as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        recordsIn += 1
        tx_date = convertDate(line[iDate])
        baseAmount = float(commaToPoint(line[iGross]))

        if paymentToken in line[iType] and refundToken not in line[iType]:
            # this is (probably) a normal donat transaction
            #line 1 - basic donation transaction
            reversedValue = baseAmount * reverseValue
            row = [tx_date] + [commodityStringUSD] + [line[iDesc]] + [inAccount] + [reversedValue] + [txCounterStart + recordsIn]
            donatWriter.writerow(row)

            #line 2 - fee deduction USD
            feeAmount = baseAmount * serviceRate   #USD
            if len(line) > iFee:
                feeAmount = abs(float(commaToPoint(line[iFee])))
            row = [""] + [""] + [line[iDesc]] + [feeAccount] + [feeAmount] + [txCounterStart + recordsIn] #EUR
            donatWriter.writerow(row)
            
            #line 3 - net to offset account (PayPal Balance) USD
            netValue = commaToPoint(line[iNet])
            row = [""] + [""] + [line[iDesc]] + [offsetAccount] + [netValue]  + [txCounterStart + recordsIn]
            donatWriter.writerow(row)

            donatsOut += splitsPerDeposit

print("splitmaker_PPDonat records in: {0}".format(recordsIn))
print("splitmaker_PPDonat donation splits out: {0}".format(donatsOut))

            
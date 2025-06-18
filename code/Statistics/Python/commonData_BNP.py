#!/usr/bin/python3

# input csv of BNP primary transactions and output csv of non-Paypal deposits in common format
# NOTE: BNP tx are completely in EUR
# usage: python3 commonData_BNP.py inputFile.csv deposits.csv 
import csv
import sys
import random
from datetime import date

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
    

iDate = 1
iDesc = 8  #Nom de la contrepartie
iValue = 3
iType = 6  #Type de transaction

offsetAccount = "Avoirs:Valeurs disponibles:BNP"
paypalTokenMixed = "PayPal"
paypalTokenCaps = "PAYPAL"
commodityStringEUR = "CURRENCY::EUR"
platformTokenBNP = "BNP"
platformTokenGitHub = "GitHub

txCounterStart = random.randint(1000, 5000)

inputFileName = "inTxBNP.csv"
outputDonationFileName = "BNPCommonData.csv"
outputPayPalTransferFileName = "BNPPayPalToSplit.csv"
outputWithdrawalFileName = "BNPManualToSplit.csv"

if len(sys.argv) < 3:
    print("commonData_bnp: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputDonationFileName = sys.argv[2]
    print("commonData_bnp input file: {0}".format(inputFileName))
    print("commonData_bnp non-paypal deposit output file: {0}".format(outputDonationFileName))

recordsIn = 0
recordsOutDeposit = 0

csvOutDeposit = open(outputDonationFileName, 'w', newline='')
csvWriterDeposit = csv.writer(csvOutDeposit, delimiter=',')

with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if recordsIn == 0:
            #header line
            recordsIn += 1
            continue

        grossValue = float(line[iValue])
        dateString = convertDate(line[iDate])
        txNumber = txCounterStart + recordsIn
        recordsIn += 1
        if grossValue >= 0.0 :
            # PayPal transactions are sometimes "PayPal" and sometimes "PAYPAL"
            if paypalTokenMixed in line[iDesc] or paypalTokenCaps in line[iDesc]:
                continue
            platformToken = platformTokenBNP
            if platformTokenGitHub in line[iDesc]:
                print("found github donation at record: {0}".format(recordsIn))
                platformToken = platformTokenGitHub
            row = [dateString] + [commodityStringEUR] + [line[iDesc]] + [offsetAccount] + [grossValue] + [txNumber] + [platformToken]
            csvWriterDeposit.writerow(row)
            recordsOutDeposit += 1

print("commonData_bnp records in: {0}".format(recordsIn))
print("commonData_bnp donation records out: {0}".format(recordsOutDeposit))

            

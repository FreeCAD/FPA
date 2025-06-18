#!/usr/bin/python3

# input csv of BNP primary transactions and output 
#             1) csv of non-Paypal deposits tx to feed splitmaker_BNPDon.py
#             2) csv of PayPal transfer tx to feed splitmaker_BNPPP.py
#                (but note that the transfers are normally applied from the 
#                 PayPal transaction stream and these records are only used as a
#                 cross check)
#             2) csv of withdrawal tx for manual handling
# NOTE: BNP tx are completely in EUR
# usage: python3 streamsplitter_BNP.py inputFile.csv deposits.csv pptransfers.csv withdrawals.csv

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
bankFeeString = "Coûts opérations diverses"
paypalTokenMixed = "PayPal"
paypalTokenCaps = "PAYPAL"
txCounterStart = random.randint(1000, 5000)

inputFileName = "inTxBNP.csv"
outputDonationFileName = "BNPDepositToSplit.csv"
outputPayPalTransferFileName = "BNPPayPalToSplit.csv"
outputWithdrawalFileName = "BNPManualToSplit.csv"

if len(sys.argv) < 5:
    print("streamsplitter_BNP: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputDonationFileName = sys.argv[2]
    outputPayPalTransferFileName = sys.argv[3]
    outputWithdrawalFileName = sys.argv[4]
    print("streamsplitter_BNP input file: {0}".format(inputFileName))
    print("streamsplitter_BNP non-paypal deposit output file: {0}".format(outputDonationFileName))
    print("streamsplitter_BNP paypal transfer output file: {0}".format(outputPayPalTransferFileName))
    print("streamsplitter_BNP withdrawal output file: {0}".format(outputWithdrawalFileName))

recordsIn = 0
recordsOutDeposit = 0
recordsOutTransfer = 0
recordsOutWithdrawal = 0

csvOutDeposit = open(outputDonationFileName, 'w', newline='')
csvOutTransfer = open(outputPayPalTransferFileName, 'w', newline='')
csvOutWithdrawal = open(outputWithdrawalFileName, 'w', newline='')
csvWriterDeposit = csv.writer(csvOutDeposit, delimiter=',')
csvWriterTransfer = csv.writer(csvOutTransfer, delimiter=',')
csvWriterWithdrawal = csv.writer(csvOutWithdrawal, delimiter=',')

with open(inputFileName) as csvIn:
# Note: November 2023 file from bnp uses ';' as separator instead of ','
#    csvReader = csv.reader(csvIn, delimiter=';')
# Note: January 2024 file from bnp is back to ',' as separator
# Note: May 2024 file from bnp is back to ';' as separator
# Note: June 2024 file from bnp is back to ',' as separator
# Note: July 2024 file is using ";"
# Note: August 2024 file is using ","
# Note: December 2024 is back to ";"
# Note: February is back to ","
# Note: March is back to ";"
# Note: April is ","
# Note: May is ";"   # does this flip on even/odd month number?!

#    csvReader = csv.reader(csvIn, delimiter=',')
    csvReader = csv.reader(csvIn, delimiter=';')
    for line in csvReader:
        if recordsIn == 0:
            # skip header line
            recordsIn += 1
            continue

#        print("streamsplitter_BNP at record {0} - {1} fields".format(recordsIn, len(line)))
#       print("streamsplitter_BNP - line: {0}".format(line))
        amount = float(line[iValue])
        formattedDate = convertDate(line[iDate])
        txNumber = txCounterStart + recordsIn
        if amount >= 0.0 :
            # PayPal transactions are sometimes "PayPal" and sometimes "PAYPAL"
            if paypalTokenMixed in line[iDesc] or paypalTokenCaps in line[iDesc]:
                row = [formattedDate] + [line[iDesc]] + [line[iValue]] + [line[iType]] + [txNumber]
                csvWriterTransfer.writerow(row)
                recordsOutTransfer += 1
            else:
                row = [formattedDate] + [line[iDesc]] + [line[iValue]] + [line[iType]] + [txNumber]
                csvWriterDeposit.writerow(row)
                recordsOutDeposit += 1
        else:
            row = [formattedDate] + [line[iDesc]] + [line[iValue]] + [line[iType]] + [txNumber]
            csvWriterWithdrawal.writerow(row)
            recordsOutWithdrawal += 1
        recordsIn += 1

print("streamsplitter_BNP records in: {0}".format(recordsIn))
print("streamsplitter_BNP donation records out: {0}".format(recordsOutDeposit))
print("streamsplitter_BNP transfer records out: {0}".format(recordsOutTransfer))
print("streamsplitter_BNP withdrawal records out: {0}".format(recordsOutWithdrawal))

            

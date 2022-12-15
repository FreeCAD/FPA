#!/usr/bin/python3

# input csv of BNP primary transactions and output 
#             1) csv of donation tx to feed splitmaker_BNPDon.py
#             2) csv of PayPal tx to feed splitmaker_BNPPP.py
#             2) csv of withdrawal tx for manual handling
# NOTE: BNP tx are completely in EUR
# usage: python3 streamsplitter_BNP.py inputFile.csv donationFile.csv transferFile.csv withdrawalFile.csv
#        python3 streamsplitter_BNP.py BNP_Misc_testTXIN.csv BNP_Misc_testDonationTXOUT.csv BNP_Misc_testTransferTXOUT.csv BNP_Misc_testWithdrawalTXOUT.csv
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
paypalToken = "PayPal"
txCounterStart = random.randint(1000, 5000)

inputFileName = "inTxBNP.csv"
outputDonationFileName = "outTxBNPDonation.csv"
outputPayPalTransferFileName = "outTxBNPPayPalTransfer.csv"
outputWithdrawalFileName = "outTxBNPWithdrawal.csv"

if len(sys.argv) < 5:
    print("streamsplitter_BNP: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputDonationFileName = sys.argv[2]
    outputPayPalTransferFileName = sys.argv[3]
    outputWithdrawalFileName = sys.argv[4]
    print("streamsplitter_BNP input file: {0}".format(inputFileName))
    print("streamsplitter_BNP donation output file: {0}".format(outputDonationFileName))
    print("streamsplitter_BNP transfer output file: {0}".format(outputPayPalTransferFileName))
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
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if recordsIn == 0:
            #header line
            recordsIn += 1
            continue

        amount = float(line[iValue])
        formattedDate = convertDate(line[iDate])
        txNumber = txCounterStart + recordsIn
        if amount >= 0.0 :
            if paypalToken in line[iDesc]:
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

            

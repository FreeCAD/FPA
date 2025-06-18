#!/usr/bin/python3

# input csv of BNP fee transactions and output csv of full split transactions
# NOTE: BNP tx are completely in EUR
# usage: python3 splitmaker_BNPFee.py inputFile.csv outputFile.csv
#        python3 splitmaker_BNPFee.py BNP_Dec2022_testTXIN.csv BNP_Dec2022_testTXOUT.csv
import csv
import sys

iDate = 0
iDesc = 1
iValue = 2
iType = 3
iTxNumber = 4

inputFileName = "inTxBNPFee.csv"
outputFileName = "outTxBNPFee.csv"

if len(sys.argv) < 3:
    print("splitmaker_BNPFee: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("splitmaker_BNPFee input file: {0}".format(inputFileName))
    print("splitmaker_BNPFee output file: {0}".format(outputFileName))

recordsIn = 0
recordsOut = 0
splitsPerTx = 2

bankFeeString = "Coûts opérations diverses"
creditCardFeeString = "Coûts sur opérations par carte"
outAccount = "Avoirs:Valeurs disponibles:BNP"
offsetAccount = "Depenses:Fees and Commissions:BNP Fees"
commodityString = "CURRENCY::EUR"
reverseValue = -1.0

csvOut = open(outputFileName, 'w', newline='')
csvWriter = csv.writer(csvOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if not (bankFeeString in line[iType] or creditCardFeeString in line[iType]):
            #not a fee transaction, needs manual handling
            print("splitmaker_BNPFee - record: {0} date: {1} needs manual handling - amount: {2}".format(recordsIn, line[iDate], line[iValue]))
            print("     desc: {0} type: {1}".format(line[iDesc], line[iType]))
            recordsIn += 1
            continue

        #line 1 - basic transaction EUR out
        baseValue = -float(line[iValue])   # withdrawal
        reversedValue = baseValue * reverseValue   # deposit-ish
        row = [line[iDate]] + [commodityString] + [line[iType]]+ [outAccount] + [baseValue] + [line[iTxNumber]]
        csvWriter.writerow(row)

        #line 2 - net to offset account (BNP Fees) EUR
        row = [""] + [""] + [""] + [offsetAccount] + [reversedValue] + [line[iTxNumber]]
        csvWriter.writerow(row)

        recordsIn += 1
        recordsOut += splitsPerTx

print("splitmaker_BNPFee records in: {0}".format(recordsIn))
print("splitmaker_BNPFee records out: {0}".format(recordsOut))

            

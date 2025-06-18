#!/usr/bin/python3

# input csv of BNP donation transactions and output csv of full split transactions
# NOTE: BNP tx are completely in EUR
# usage: python3 splitmaker_BNPPP.py inputFile.csv outputFile.csv
#        python3 splitmaker_BNPPP.py BNP_Dec2022_testTXIN.csv BNP_Dec2022_testTXOUT.csv
import csv
import sys

iDate = 0
iDesc = 1
iValue = 2
iType = 3
iTxNumber = 4

inputFileName = "inTxBNPPP.csv"
outputFileName = "outTxBNPPP.csv"

if len(sys.argv) < 3:
    print("splitmaker_BNPPP: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("splitmaker_BNPPP input file: {0}".format(inputFileName))
    print("splitmaker_BNPPP output file: {0}".format(outputFileName))

recordsIn = 0
recordsOut = 0
splitsPerTx = 2

inAccount = "Avoirs:Valeurs disponibles:BNP"
offsetAccount = "Avoirs:Valeurs disponibles:PayPal"
commodityString = "CURRENCY::EUR"
reverseValue = -1.0

csvOut = open(outputFileName, 'w', newline='')
csvWriter = csv.writer(csvOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        #line 1 - basic transaction EUR in to BNP
        baseAmount = float(line[iValue])
        reversedAmount = baseAmount * reverseValue
        row = [line[iDate]] + [commodityString] + [line[iDesc]]+ [inAccount] + [baseAmount] + [line[iTxNumber]]
        csvWriter.writerow(row)

        #line 2 - net to offset account (PayPal balance) EUR
        row = [""] + [""] + [""] + [offsetAccount] + [reversedAmount] + [line[iTxNumber]]
        csvWriter.writerow(row)
        print("date: {0} to: {1} amt: {2} from: {3} amt: {4}".format(line[iDate], inAccount, baseAmount, offsetAccount, reversedAmount))
        recordsIn += 1
        recordsOut += splitsPerTx

print("splitmaker_BNPPP records in: {0}".format(recordsIn))
print("splitmaker_BNPPP records out: {0}".format(recordsOut))

            

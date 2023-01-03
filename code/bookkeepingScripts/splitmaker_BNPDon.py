#!/usr/bin/python3

# input csv of BNP donation transactions and output csv of full split transactions
# NOTE: BNP tx are completely in EUR
# usage: python3 splitmaker_BNPDon.py inputFile.csv outputFile.csv
#        python3 splitmaker_BNPDon.py BNP_Dec2022_testTXIN.csv BNP_Dec2022_testTXOUT.csv
import csv
import sys

iDate = 0
iDesc = 1
iValue = 2
iType = 3
iTxNumber = 4

inputFileName = "inTxBNPDon.csv"
outputFileName = "outTxBNPDon.csv"

if len(sys.argv) < 3:
    print("splitmaker_BNPDon: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("splitmaker_BNPDon input file: {0}".format(inputFileName))
    print("splitmaker_BNPDon output file: {0}".format(outputFileName))

recordsIn = 0
recordsOut = 0
splitsPerTx = 2

inAccount = "Recettes:Dons et legs:Donations In EUR"
offsetAccount = "Avoirs:Valeurs disponibles:BNP"
commodityString = "CURRENCY::EUR"
reverseValue = -1.0

csvOut = open(outputFileName, 'w', newline='')
csvWriter = csv.writer(csvOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        #line 1 - basic transaction EUR in
        baseAmount = float(line[iValue])
        reversedValue = baseAmount * reverseValue
        print("record {0} line 1 base transaction value: {1}".format(recordsIn, reversedValue))
        row = [line[iDate]] + [commodityString] + [line[iDesc]]+ [inAccount] + [reversedValue] + [line[iTxNumber]]
        csvWriter.writerow(row)

        #line 2 - net to offset account (BNP Balance) EUR
        print("record {0} line 2 transfer: {1}".format(recordsIn, baseAmount))
        row = [""] + [""] + [""] + [offsetAccount] + [baseAmount] + [line[iTxNumber]]
        csvWriter.writerow(row)
        recordsIn += 1
        recordsOut += splitsPerTx

print("splitmaker_BNPDon records in: {0}".format(recordsIn))
print("splitmaker_BNPDon records out: {0}".format(recordsOut))

            

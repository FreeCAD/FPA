#!/usr/bin/python3

# input csv from weekly transfer worksheet and output csv of full split transactions for ready for import
#                                           
# usage: python3 splitmaker_WeeklyTransfers.py weeklyTransfers.csv weeklyTransfersImport.csv

import csv
import sys
import random

# remove thousands separator from text numbers
def stripComma(inValue):
    outValue = inValue
    outValue = outValue.replace(",", "")
    return outValue
    
iDate = 0
iFromUSDAmount = 1
iToEURAmount = 2
iToBNPAmount = 3
iRateEURUSD = 4
iRateUSDEUR = 5

commodityStringUSD = "CURRENCY::USD"
commodityStringEUR = "CURRENCY::EUR"

PPUSDAccount = "Avoirs:Valeurs disponibles:PayPal:PayPal USD"
PPEURAccount = "Avoirs:Valeurs disponibles:PayPal:PayPal EUR"
BNPAccount = "Avoirs:Valeurs disponibles:BNP"

transferDesc = "weekly transfer"

startLine = 4

inputFileName = "weeklyTransfers.csv"
outputFileName = "weeklyTransfersImport.csv"

if len(sys.argv) < 3:
    print("splitmaker_WeeklyTransfers: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("splitmaker_WeeklyTransfers input file: {0}".format(inputFileName))
    print("splitmaker_WeeklyTransfers output file: {0}".format(outputFileName))

recordsIn = 0
recordsOut = 0


txCounterStart = random.randint(41000, 45000)

splitsOut = open(outputFileName, 'w', newline='')
splitWriter = csv.writer(splitsOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if recordsIn < startLine:
            # skip the preamble
            recordsIn += 1
            continue
        if not line[iDate] or line[iDate] == "Date":
            #skip the blank lines
            recordsIn += 1
            continue
        
        recordsIn += 1
        
        fromUSDAmount = float(stripComma(line[iFromUSDAmount])) 
        toEURAmount = float(stripComma(line[iToEURAmount]))
        toBNPAmount = float(stripComma(line[iToBNPAmount]))
        
        txNumber = txCounterStart + recordsIn
        
        # note GC will get prissy if the primary transaction is "from" PP USD
        # basic split from PP USD to PP EUR
        
        row0 = [line[iDate]] + [commodityStringUSD] + [transferDesc] + [PPEURAccount] + [toEURAmount] + [0]  + [line[iRateUSDEUR]] + [txNumber]
        #row0 = [line[iDate]] + [commodityStringUSD] + [transferDesc] + [PPUSDAccount] + [-fromUSDAmount] + [0] + [1] + [txNumber]
        splitWriter.writerow(row0)
        recordsOut += 1

#        row1 = [""] + [""] + [transferDesc] + [PPEURAccount] + [toEURAmount] + [0]  + [line[iRateEURUSD]] + [txNumber]
        row1 = [""] + [""] + [transferDesc] + [PPUSDAccount] + [-fromUSDAmount] + [0] + [line[iRateEURUSD]] + [txNumber]
        splitWriter.writerow(row1)
        recordsOut += 1
    
        if toBNPAmount == 0:
            continue
            
        # basic split PPEUR to BNP
        row2 = [line[iDate]] + [commodityStringEUR] + [transferDesc] + [PPEURAccount] + [-toBNPAmount] + [0] + [1] + [txNumber]
        splitWriter.writerow(row2)
        recordsOut += 1

        row3 = [""] + [""] + [transferDesc] + [BNPAccount] + [toBNPAmount] + [0]  + [1] + [txNumber]
        splitWriter.writerow(row3)
        recordsOut += 1

print("splitmaker_WeeklyTransfers records in: {0}".format(recordsIn))
print("splitmaker_WeeklyTransfers splits out: {0}".format(recordsOut))

            

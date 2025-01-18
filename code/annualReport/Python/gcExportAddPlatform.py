#!/usr/bin/python3

# input csv of exported gnuCash tx and output with platform added.  the input is expected to be pairs
# of records - 1 for the debit to Don&Legs and one for the corresponding credit to an Avoirs disponsible
# account.  Sometimes there are more than 1 credit record
# usage: python3 gcExportAddPlatform.py inputCommon.csv outputCommon.csv

import csv
import sys

inputFileName = "inputCommon.csv"
outputFileName = "outputCommon.csv"

if len(sys.argv) < 3:
    print("gcExportAddPlatform: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("gcExportAddPlatform input file: {0}".format(inputFileName))
    print("gcExportAddPlatform ooutput file: {0}".format(outputFileName))

recordsIn = 0
recordsOut = 0

iDesc = 3
iAccount = 9

EOFToken = "end"
DirectToken = "BNP Direct"
PaypalToken = "PayPal"
StripeToken = "STRIPE"
GithubToken = "GitHub"
OCToken     = "OpenCollective"

OCAccount   = "Avoirs:Valeurs disponibles:OpenCollective"
PPAccount   = "Avoirs:Valeurs disponibles:PayPal"

fileOut = open(outputFileName, 'w', newline='')
outputWriter = csv.writer(fileOut, delimiter=',')

with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    while True:
        debitLine = next(csvReader, EOFToken)
        # uncomment this if input file has a header line
#        if recordsIn == 0:
#            #header line
#            recordsIn += 1
#            outputWriter.writerow(debitLine)
#            recordsOut += 1
#            continue

        if debitLine == EOFToken:       # no more records
            break
        if debitLine[iDesc] == "" :
            # this is an extra credit line and we should skip it.
            recordsIn += 1
            continue
        creditLine = next(csvReader, EOFToken)
        if creditLine == EOFToken:
            break
        
        recordsIn += 2
        platform = DirectToken
        #print("{0} : {1}".format(StripeToken, debitLine[iDesc]))
        if StripeToken in debitLine[iDesc]:
            platform = StripeToken
        if GithubToken in debitLine[iDesc]:
            platform = GithubToken

        if PaypalToken in creditLine[iAccount]:
            platform = PaypalToken
        if OCToken in creditLine[iAccount]:
            platform = OCToken
        row = debitLine + [platform]
        outputWriter.writerow(row)
        recordsOut += 1

print("gcExportAddPlatform records in: {0}".format(recordsIn))
print("gcExportAddPlatform records out: {0}".format(recordsOut))


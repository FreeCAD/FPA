#!/usr/bin/python3

# input csv of common data records and output same csv with corporate status added
# usage: python3 commonAddCorporate.py inputCommon.csv outputCommon.csv

import csv
import sys

# check donor name to see if it is a corporate donor
def isCorporateDonor(donorName):
    corporateTokens = ["co", "ltd", "cie", "ltee", "bv", "nv", "sa", "llc", "llp", "ltee", "ltda", "pty", "gmbh", "spa", "tech", "technology", "engineering", "partners", "inc", "usa", "design", "germany", "photography", "corporation", "enterprises", "construction", "&", "et", "l l c", "systems", "group", "com", "supply", "business", "electronics", "tool"]
    name = "  {0}  ".format(donorName.lower())
    name = name.replace(".", " ")
    name = name.replace(",", " ")
    name = name.replace(")", " ")
    name = name.replace("(",  " ")
    for token in corporateTokens:
        testableToken = " {0} ".format(token)
        tokenCount = name.count(testableToken)
        if tokenCount:
            return True
    return False


iDate = 0
iCurrency = 1
iDesc = 2
iAccount = 3
iValue = 4
iTransId = 5
iPlatform = 6

inputFileName = "inputCommon.csv"
outputFileName = "outputCommon.csv"

if len(sys.argv) < 3:
    print("commonAddCorporate: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("commonAddCorporate input file: {0}".format(inputFileName))
    print("commonAddCorporate payment file: {0}".format(outputFileName))

recordsIn = 0
recordsOut = 0

fileOut = open(outputFileName, 'w', newline='')
outputWriter = csv.writer(fileOut, delimiter=',')

with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
# uncomment this if input file has a header line
#        if recordsIn == 0:
#            #header line
#            recordsIn += 1
#            continue

        recordsIn += 1
        corporate = "{0}".format(isCorporateDonor(line[iDesc]))
        row = ( [line[iDate]] + [line[iCurrency]] + [line[iDesc]] + [line[iAccount]] + 
                [line[iValue]] + [line[iTransId]] + [line[iPlatform]] + [corporate] )
        outputWriter.writerow(row)
        recordsOut += 1

print("commonAddCorporate records in: {0}".format(recordsIn))
print("commonAddCorporate payments out: {0}".format(recordsOut))


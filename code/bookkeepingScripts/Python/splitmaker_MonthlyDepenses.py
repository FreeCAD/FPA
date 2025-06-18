#!/usr/bin/python3

# input csv from monthly payment worksheet and output csv of full split transactions for ready for import
#                                           
# usage: python3 splitmaker_MonthlyDepenses.py worksheet.csv monthlyDepensesImport.csv

import csv
import sys
import random

# remove thousands separator from text numbers
def stripComma(inValue):
    outValue = inValue
    outValue = outValue.replace(",", "")
    return outValue
    
iDate = 0
iIssue = 1
iDesc = 2
iAwardAmount = 3
iAwardCurrency = 4
iVATNo = 5
iRVAT = 6
iFromAccount = 7
iToAccount = 8
iToCurrency = 9
iAmountPaid = 10
iToAmount = 11
iBankFees = 12
iForeignFeesUSD = 13
iRate = 14
iVATAmount = 15
iCheck = 16

commodityStringUSD = "CURRENCY::USD"
commodityStringEUR = "CURRENCY::EUR"

BNPFeeAccount = "Depenses:Autres dépenses:Fees and Commissions:BNP Fees"
OtherBankFeesUSDAccount = "Depenses:Autres dépenses:Fees and Commissions:Other Bank Fees:Other Bank Fees USD"
VATControlAvoirsAccount = "Avoirs:VAT Control Avoirs"
RVATBalanceAccount = "Avoirs:Reverse VAT Balance"
VATControlDettesAccount  = "Dettes:VAT Control Dettes"

inputFileName = "monthlyWorksheet.csv"
outputFileName = "monthlyDepensesImport.csv"

if len(sys.argv) < 3:
    print("splitmaker_MonthlyDepenses: files not specified, using defaults")
else:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    print("splitmaker_MonthlyDepenses input file: {0}".format(inputFileName))
    print("splitmaker_MonthlyDepenses output file: {0}".format(outputFileName))

recordsIn = 0
recordsOut = 0
generalDropped = 0
splitsPerPayment = 3

txCounterStart = random.randint(33000, 35000)

splitsOut = open(outputFileName, 'w', newline='')
splitWriter = csv.writer(splitsOut, delimiter=',')
with open(inputFileName) as csvIn:
    csvReader = csv.reader(csvIn, delimiter=',')
    for line in csvReader:
        if recordsIn == 0:
            recordsIn += 1
            continue
        if not line[iDate]:
            recordsIn += 1
            continue
        
        recordsIn += 1
        
        description = line[iDesc] + " " + str(line[iIssue])
        
        creditAmount = float(stripComma(line[iToAmount]))
        debitAmount = float(stripComma(line[iAmountPaid])) * -1
        bankFee = float(stripComma(line[iBankFees]))
        foreignFee = float(stripComma(line[iForeignFeesUSD]))
        VATAmount = float (stripComma(line[iVATAmount]))
        rate = float(line[iRate])
        if line[iToCurrency] == commodityStringEUR:
            rate = 1
        txNumber = txCounterStart + recordsIn
        
        # basic debit split for from-account
        # always EUR from BNP right now
        row0 = [line[iDate]] + [commodityStringEUR] + [description] + [line[iFromAccount]] + [debitAmount] + [line[iVATNo]]  + [line[iRate]] + [txNumber]
        splitWriter.writerow(row0)
        recordsOut += 1
        
        # basic credit split for to-account
        # could be EUR or USD
        toRate = rate
        if line[iToCurrency] == commodityStringUSD:
            toRate = 1/toRate
        row1 = [""] + [""] + [description] + [line[iToAccount]] + [creditAmount] + [line[iVATNo]]  + [toRate] + [txNumber]
        splitWriter.writerow(row1)
        recordsOut += 1
        

        if bankFee != 0:
            # always EUR
            row2 = [""] + [""] + [description] + [BNPFeeAccount] + [bankFee] + [line[iVATNo]]  + [1] + [txNumber]
            splitWriter.writerow(row2)
            recordsOut += 1

        if foreignFee != 0:
            # always USD?
            row3 = [""] + [""] + [description] + [OtherBankFeesUSDAccount] + [foreignFee] + [line[iVATNo]]  + [toRate] + [txNumber]
            splitWriter.writerow(row3)
            recordsOut += 1

        if VATAmount != 0:
            # always EUR
            if line[iRVAT] == "FALSE":  
                # this is regular vat on purchase that we can claim against vat owing
                row4 = [""] + [""] + [description] + [VATControlAvoirsAccount] + [VATAmount] + [line[iVATNo]]  + [1]  + [txNumber]
                splitWriter.writerow(row4)
                recordsOut += 1
            if line[iRVAT] == "TRUE":
                # this is reverse VAT that we owe to taxation authority
                row5 = [""] + [""] + [description] + [VATControlDettesAccount] + [-VATAmount] + [line[iVATNo]]  + [1]  + [txNumber]
                splitWriter.writerow(row5)
                recordsOut += 1
                row6 = [""] + [""] + [description] + [RVATBalanceAccount] + [VATAmount] + [line[iVATNo]]  + [1]  + [txNumber]
                splitWriter.writerow(row6)
                recordsOut += 1


print("splitmaker_MonthlyDepenses records in: {0}".format(recordsIn))
print("splitmaker_MonthlyDepenses monthly splits out: {0}".format(recordsOut))

            

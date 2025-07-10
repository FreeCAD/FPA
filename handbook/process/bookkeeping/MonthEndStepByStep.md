---
title: Month-end Step by Step
description:
  The tasks required for end of month bookkeeping updates.
layout: default
---
# Month End Processing Step by Step

At the end of each month, the following tasks need to be performed:

* find out what the financial service providers think we have
    - get the month end balances from OpenCollective and PayPal, on the last day of the month if you can manage it. 
    - Neither seems to provide a "balance as of date" function.
    - BNP provides an actual statement as of the last of the month well as the data file

* retrieve svg data files from collection platforms
    - OpenCollective 
    - PayPal
    - BNP

* massage data files into common gnuCash import format
    - see monthly commands
    - reports list tx requiring manual handling
    - data formats change without notice, usually delimiters changed from last month
    - first time fails 
    
* update weekly transfer worksheet with data from 2)
    - import these (step x) into gnuCash first as they will establish currency conversion rates
    - a python script converts the csv spreadsheet into import format

* update monthly payment worksheet with data from 2) and/or github issues
    - a python script converts the csv spreadsheet into import format
    
* up to now we have not changed gnuCash, so this is a good time to make a backup of the .gnucash file.

* import massaged data
    - weekly transfers first
    - the order of the other imports is not significant, but often OpenCollective and PayPal data is
      available before the BNP data.
    - gnuCash has a feature that attempts to detect duplicate entries. Since we have a number of small
      recurring donations, we get a lot of false positives from this feature.  Good exercise for your
      clicking finger.

* handle any manual tx identify by the scripts
    - non-standard currency
    - on time payments

* balance the books
    - compare the month end balances gathered in 0) to the gnucash balances.
    - PayPal never, ever balances (multiple currencies and exchange rates?).
    - OpenCollective balances are closer (might be a fee not in our data file?)
    - BNP balances are typically very close. 
<!--- # the cummulative error will get bigger as the year progresses, so the raw balance comparison becomes
# less useful.  In this case, examining the error introduced in the current month is more helpful. --->

* mandatory reports
    - not really mandatory in any regulatory sense.
    - Balance sheet, income statement, monthly balance and monthly spending
    - results to FPA git hub _reports/monthlyfinancialstatus and _reports/2025.md
    
* proto-dashboard
    - update the revenue tracking and burn plan spreadsheets
    - graphs of the results to FPA weekly meeting agenda

* donation monitoring
    - export dons & legs transactions for the month from gnucash
    - run the R script to generate a graphic

* FPA Admin agenda item
    - amounts in, out. Net for the month and cash on hand.
    - graphs from dashboard and donation monitoring

* backups
    - create a zip archive of the gnucash file, the config file (.local/share/gnucash), the data files, reports etc
    - update the FPA repo at encrypted/gnuCashBackup

    

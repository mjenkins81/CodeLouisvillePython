# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:21:40 2022

@author: Michaela
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn')

import yfinance as yf

unh = yf.Ticker("UNH")
antm = yf.Ticker("ANTM")
cnc = yf.Ticker("CNC")
moh = yf.Ticker("MOH")
cvs = yf.Ticker("CVS")
hum = yf.Ticker("HUM") 
ci = yf.Ticker("CI")
clov = yf.Ticker("CLOV") 
bhg = yf.Ticker("BHG")


#financials are in a dataframe
# balance_sheet are in a dataframe
# info is a dictionary


# print(type(unh.financials))
# print(type(unh.balance_sheet))
# print(type(unh.info))

# unh.financials
# unh.balance_sheet
# unh.info

#create variable for info since it's a dictionary

po_info = antm.info

#display info line by line
for key,value in po_info.items():
    print(key, ":", value)


# antm.financials
# antm.balance_sheet
# antm.info

# cnc.financials
# cnc.balance_sheet
# cnc.info

# moh.financials
# moh.balance_sheet
# moh.info

# cvs.financials
# cvs.balance_sheet
# cvs.info

# hum.financials
# hum.balance_sheet
# hum.info

# ci.financials
# ci.balance_sheet
# ci.info

# clov.financials
# clov.balance_sheet
# clov.info

# bhg.financials
# bhg.balance_sheet
# bhg.info

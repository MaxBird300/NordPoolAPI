# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:52:27 2021

Documentation for API can be found here - https://marketdata.nordpoolgroup.com/docs/services/MarketData-UK-v2/operations/UkAreaPrices?

@author: maxbi
"""
from nord_pool_api_backend import NordPoolClass

startDate = '01/01/2020' # don't query more than one month at a time 
endDate = '01/02/2020'
   
nordPoolAPI = NordPoolClass() # initialise the API connection
df = nordPoolAPI.dayAheadData(startDate, endDate) # Timestamp in output dataframe relates to the start of the time period


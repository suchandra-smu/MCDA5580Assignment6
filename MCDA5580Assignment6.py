# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:03:44 2022

@author: Suchandra Ghosh
"""

import pandas as pd
import requests
import streamlit as st

API_URL = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'

st.title('Bitcoin Price Trend')

period = st.slider('Number of Days:',min_value=1, max_value=365, value=120)
currency=st.radio("Currency:",('CAD', 'USD', 'INR'))

params = {'vs_currency':currency,'days':period,'interval':'daily'}

ret = requests.get(API_URL, params=params)

if ret.status_code != 200:
    print("API Get request failed. Error Code:", ret.status_code)

else:
    api_data = ret.json()
    
    df = pd.DataFrame(api_data['prices'])
    
    df.columns=['date','price']
    df['date']=pd.to_datetime(df['date'], unit='ms')
    df = df.set_index('date')
    
    st.line_chart(df)
    st.write("Average price during this period was ", df['price'].mean(), " ", currency)
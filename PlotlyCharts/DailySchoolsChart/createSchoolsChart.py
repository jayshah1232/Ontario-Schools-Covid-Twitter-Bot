import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py
import urllib.request
import json
import config
import os
from datetime import datetime

print("Creating dataframe from Ontario data API...")

#creating a dataFrame
df = pd.read_json('https://data.ontario.ca/datastore/dump/8b6d22e2-7065-4b0f-966f-02640be366f2?format=json')

today = datetime.today().strftime('%Y-%m-%d')

dt_all = pd.date_range(start=df['reported_date'].iloc[0],end=df['reported_date'].iloc[-1]) #creating date range that only includes dates that have data (no weekends)
print(dt_all)

print("Logging in to Chart Studio...")
chart_studio.tools.set_credentials_file(username=config.plotlyUsername, api_key=config.plotlyAPIKey)
print("Logged in")

print("Creating Active Cases chart...")
x = df['']
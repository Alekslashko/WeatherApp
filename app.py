import streamlit as st
import requests
import pandas as pd
from datetime import datetime

API_KEY = "587022bce4b52fe8cff62c29e7c1d2bd"
LAT = 42.1354
LON = 24.7453
URL = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"

response = requests.get(URL)
data = response.json()

st.write({weather})

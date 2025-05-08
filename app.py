import streamlit as st
import requests
import pandas as pd
from datetime import datetime

API_KEY = "587022bce4b52fe8cff62c29e7c1d2bd"
CITY = "Plovdiv"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

response = requests.get(URL)
data = response.json()

st.write(data["weather"]["main"])

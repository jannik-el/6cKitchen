import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium, json

st.set_page_config(layout="wide")


"# UMEUS 6C Kitchen's Website"

st.write("Welcome to 6c's Website")

col1, col2, col3 = st.columns(3)

with col1:
  st.header("Shopping List")
  
  
with col2:
  st.header("Current Kitchen Captain, Shoppers and Weekend Cleaning")
  
  
with col3:
  st.header("Estimated Money?")
  
  




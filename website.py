import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium, json

st.set_page_config(layout="wide")


"# UMEUS 6C Kitchen's Website"

st.write("Welcome to 6c's Website!! 🎊")

col1, col2, col3 = st.columns(3)

with col1:
  st.header("Shopping List")
  
  test = st.checkbox('Buy sum cookies')

  if test:
      st.write('yasssss!')
  
with col2:
  st.header("Kitchen Captain, Shoppers and Weekend Cleaning")
  
  st.write("I'll automate this so you can check who is what and when")
  
  
with col3:
  st.header("Estimated Money?")
  
  st.write("~800kr")
  st.write("Please don't go crazy with the decorations budget")
  
  




import streamlit as st
import pandas as pd

kitchen_cap = "Caroline"
shoppers = "Marc & Jannik"
weekend_cleaning = "Caroline + Suheda"

st.set_page_config(layout="wide")

"# UMEUS 6C Kitchen's Website"
st.write("Welcome to 6c's Website!! 🎊")

with st.container():
  col1, col2, col3 = st.columns(3)

  with col1:
    st.header("Shopping List")
    
    test = st.checkbox('Buy sum cookies')

    if test:
        st.write('yasssss!')
    
  with col2:
    st.header("Kitchen Captain, Shoppers and Weekend Cleaning")

    st.write("""
    In future this will be automated with the actual dates.
    As of 21/02/2022 these roles are accurate. 
    """)

    st.write(f"Kitchen Captain: {0}".format(kitchen_cap))
    st.write(f"Shoppers: {0}".format(shoppers))
    st.write(f"Weekend Cleaning: {0}".format())

    with st.expander("See Kitchen Captain Chores Below:"):

      st.write("""
         Waiting on Neel to send me these   
      """)
    
    with st.expander("See Shopper roles below:"):

      st.write("TBD")

    with st.expander("See Weekend Cleaning Chores below:"):

      st.write("""
      Also waiting on Neel....
      """)
    
  with col3:
    st.header("Money")
    
    st.write("Currently at around ~800kr")
    st.write("Please don't go crazy with the decorations budget")
    st.write("[Last Updated: 21/02/2022]")
  
  



import streamlit as st
# import pandas as pd

kitchen_cap = "Caroline"
shoppers = "Marc & Jannik"
weekend_cleaning = "Caroline + Suheda"


@st.cache(allow_output_mutation=True) # this allows input data to be saved
class sl_list: #shopping list object

  def __init__(self, name):
    self.name = name

  def create_item(self):
    return

st.set_page_config(layout="wide")

"# UMEUS 6C Kitchen's Website"
st.write("Welcome to 6c's Website!! 🎊")

with st.container():
  col1, col2, col3 = st.columns(3)

  with col1: # Shopping List
    st.header("Shopping List")
    st.write("This will be a shopping list for the kitchen, doesn't work yet, need to spend some time coding it first :)")
    
    test = st.checkbox('Buy sum cookies')

    if test:
        st.write('Why though?')
    
  with col2: # Kitchen Captain and etc. 
    st.header("Kitchen Captain, Shoppers and Weekend Cleaning")

    st.write("""
    In future this will be automated with the actual dates.
    As of 21/02/2022 these roles are accurate. 
    """)

    st.write(f"Kitchen Captain: {kitchen_cap}")
    st.write(f"Shoppers: {shoppers}")
    st.write(f"Weekend Cleaning: {weekend_cleaning}")

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
    
  with col3: # Money and etc...
    st.header("Money")
    
    st.write("Currently at around ~800kr")
    st.write("Please don't go crazy with the decorations budget")
    st.write("[Last Updated: 21/02/2022]")


st.write("You scrolled this far down? Damn.")
st.write("Please sign the petition to rename 6C Kitchen to:")
vote = st.checkbox("SEXY KITCHEN")
vote2 = st.checkbox("SEX-C KITCHEN")

vote_no = 0
vote2_no = 0

if vote:
  st.write("wwooooop woooopppp 💃💃💃💃💃💃💃 its gettin hot in herrrrr")
  vote_no += 1

if vote2:
  st.write("wwooooop woooopppp 💃💃💃💃💃💃💃 its gettin hot in herrrrr")
  vote2_no += 1

st.write(f"Current Votes for option 1:", vote_no)
st.write(f"Current Votes for option 2:", vote2_no)





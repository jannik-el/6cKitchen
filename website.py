import streamlit as st
# import pandas as pd

kitchen_cap = "Caroline"
shoppers = "Marc & Jannik"
weekend_cleaning = "Caroline + Suheda"

# class SL_Class: #shopping list class
#   @st.cache(allow_output_mutation=True) # this allows input data to be saved
#   def __init__(self, s_list=[]): # create shopping list item
#     self.item = s_list
#     return

#   @st.cache(allow_output_mutation=True) # this allows input data to be saved
#   def create_item(self, item):
#     self.append(item)
#     return self

st.set_page_config(layout="wide")

"# UMEUS 6C Kitchen's Website"
st.write("Welcome to 6c's Website!! 🎊")

# shop_list = SL_Class()

with st.container():
  col1, col2, col3 = st.columns(3)

  with col1: # Shopping List
    st.header("Shopping List")
    st.write("This will be a shopping list for the kitchen, doesn't work yet, need to spend some time coding it first :)")
    
    @st.cache(allow_output_mutation=True) # this allows input data to be saved
    def shop_list():
      return []

    add_item = st.text_input("Add a shopping list item here:")
    if add_item:
      shop_list().append(add_item)
    
    for i in shop_list():
      st.checkbox(i)
      
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


################# testing ################


@st.cache(allow_output_mutation=True) # this allows input data to be saved
def return_vote():
  return []

@st.cache(allow_output_mutation=True) # this allows input data to be saved
def return_vote2():
  return []


st.write("Testing....")
st.write("Please sign the petition to rename 6C Kitchen to:")
vote = st.checkbox("SEXY KITCHEN")
vote2 = st.checkbox("SEX-C KITCHEN")


if vote:
  # st.write("wwooooop woooopppp 💃💃💃💃💃💃💃 its gettin hot in herrrrr")
  return_vote().append("x")

if vote2:
  # st.write("wwooooop woooopppp 💃💃💃💃💃💃💃 its gettin hot in herrrrr")
  return_vote2().append("x")

st.write(f"Current Votes for option 1:", len(return_vote()))
st.write(f"Current Votes for option 2:", len(return_vote2()))





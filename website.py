from pickle import TRUE
import streamlit as st
# import pandas as pd

kitchen_cap = "Caroline"
shoppers = "Marc & Jannik"
weekend_cleaning = "Caroline + Suheda"

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

    if st.button("Clear list"):
      shop_list()

    add_item = st.text_input("Add a shopping list item here:")
    if add_item:
      shop_list().append(add_item)
    
    radio_list = st.radio("", shop_list())

    if radio_list == [i for i in shop_list()]:
      shop_list().pop()
      
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
        General Info:
        -	You are captain for one week at a time
        -	We follow the list posted in the kitchen with dates on it
        -	If you for can´t be kitchen captain the week you are assigned to be, you can switch with somebody
        -	If you switch with somebody you write it on the list posted in the kitchen

        Duties:
        - Take out the trash when the trash cans are full
        -	Take out bio trash every day or every second day
        -	Remove anything from all the surfaces in the kitchen Thursday morning
        -	Put up chairs in the kitchen Thursday morning or Wednesday night 
        -	Empty the mailbox every day and put mail in the binder (remember to make sure the mailbox is locked)
        -	Check the filters in the dishwasher a couple of times during the week
        -	Remove the dirty cloths and dish towels every day if needed (and wash them if there is enough)
        -	Make sure that the kitchen looks fine before you go to bed
        -	Close the windows and turn the lights down
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





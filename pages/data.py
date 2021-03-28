import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

def data():
    st.header("Multiplier")

    # read actions csv
    actions_df = pd.read_csv("./data/actions.csv")
    actions = actions_df["Action"]
    selected_actions = st.multiselect("What will you do?", actions)

    st.markdown("You chose to do the following: ")

    total_co2 = 0
    for action in selected_actions:
        st.markdown("     **·** " + action)
        row = actions_df[actions_df['Action']==action]
        co2 = row.values[0][1]
        total_co2 += int(co2)
    
    st.subheader("Your Savings")
    st.markdown("You will prevent **" + str(total_co2) + "** lbs. of CO2 from entering the atmosphere each year!")

    st.subheader("Savings Multiplier")
    # get number of people
    num_people = st.slider("Number of People", min_value=1, max_value=1000000)
    multiplier = total_co2 * num_people

    if num_people > 1 and selected_actions:
        st.markdown("If **" + str(num_people) + "** people followed your footsteps, we would prevent **" + str(multiplier) + "** lbs. of CO2 from entering the atmosphere each year!")
        st.markdown("That's equivalent to the weight of **" + str(int(multiplier/900)) + "** concert grand pianos!")

    # # DATA
    # st.header("Data")

    # # get year
    # year = st.slider("Year", min_value=1990, max_value=2020)

    # # get all countries
    # countries = df['Country'].unique()
    # # select country
    # country = st.selectbox('Select a Country', countries)

    # # show row for selected year and country
    # row = df[ (df['Year']==year) & (df['Country']==country) ]
    # st.dataframe(row)

    # # extract value in emissions column
    # emissions = row.values[0][2]
    # st.markdown(country + "'s emissions is " + str(emissions))

    # # display map
    # st.header("World Map")
    # display_map()

def display_map():          
    st.markdown("**Add world map here**")
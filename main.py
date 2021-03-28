import streamlit as st
import pandas as pd

from pages.home import home
from pages.heros import heros
from pages.game import game

def main():
    st.sidebar.title("Enviro Hero")

    # show nav
    nav_options = ["Home", "Heroes", "Simulator"]
    selection = st.sidebar.selectbox("Navigation", nav_options)
    
    # handle nav
    if selection == "Home":
        home()
    elif selection == "Heroes":
        heros()
    else:
        game()

main()
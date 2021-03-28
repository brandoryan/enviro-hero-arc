import streamlit as st

def home():
    st.header("Home")
    st.image("./logo_pics/enviro-hero-logo.png")
    st.header("What we hope to achieve:")
    st.write("To inspire awareness of the imminent threat of global climate change and to communicate a tangible representation to the public of how their actions and positively and negatively impact the environment.")

    st.header("How to use the Simulator:")
    st.write("1) Choose the hero organization you would like to represent under Navigation \u2192 Heroes")
    st.write("2) Then Navigation \u2192 Simulator")
    st.write("3) Move the slider to pick how many people you will be making choices for (Note: this will increase or decrease your impact on the virtual map environment)")
    st.write("4) Choose options and see how they effect the CO2 and energy production levels on the map!")
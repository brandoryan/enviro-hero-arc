"""
Enviro Hero
"""

import streamlit as st
import time
from PIL import Image
import pandas as pd
import numpy as np

def display_choice_timer():
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

def heros():
    associations = [ 
        { 
        "name": "World Wildlife Fund",
        "logo": "logo_pics/wwf1.jpg",
        "desc": "For 60 years, WWF has worked to help people and nature thrive.\nAs the world’s leading conservation organization, WWF works in nearly 100 countries. At every level, we collaborate with people around the world to develop and deliver innovative solutions that protect communities, wildlife, and the places in which they live.",
        "page": "https://www.worldwildlife.org/"
        },
        {
        "name": "Green Peace",
        "logo": "logo_pics/greenpeace1.jpg",
        "desc": "We want to live on a healthy, peaceful planet. A planet where forests flourish, oceans are full of life and where once-threatened animals safely roam. Where our quality of life is measured in relationships, not things. Where our food is delicious, nutritious, and grown with love. Where the air we breathe is fresh and clear. Where our energy is as clean as a mountain stream. Where everyone has the security, dignity and joy we all deserve. It’s all possible. We can’t make it happen alone, but have no doubt: We can do it together.",
        "page": "https://www.greenpeace.org/international/"
        },
        {
        "name": "National Geographic Society",
        "logo": "logo_pics/ngs1.jpg",
        "desc": "Since 1888, the National Geographic Society has brought together extraordinary individuals from around the world. While our Explorers represent diverse backgrounds and pursue very different types of work, we think they share some traits in common. National Geographic Explorers: are leaders. are problem solvers. are informed, curious, and capable individuals who are committed to making the world a better place. have a sense of responsibility and respect for other people, cultures, and the natural world. are empowered to make a difference, pursue bold ideas, and persist in the face of challenges. observe, document, and engage with the world around them.  tell stories that inspire others. create and foster a global community committed to a sustainable future. are committed to supporting diversity, equity, and inclusion in their respective fields.",
        "page": "https://www.nationalgeographic.org/"
        },
        {
        "name": "Rainforest Action Network",
        "logo": "logo_pics/ran1.jpg",
        "desc": "Rainforest Action Network preserves forests, protects the climate and upholds human rights by challenging corporate power and systemic injustice through frontline partnerships and strategic campaigns. RAN works toward a world where the rights and dignity of all communities are respected and where healthy forests, a stable climate and wild biodiversity are protected and celebrated. We are committed to doing what is necessary, not only what is considered politically feasible, to preserve rainforests, protect the climate, and uphold human rights.",
        "page": "https://www.ran.org/"
        },
        {
        "name": "Friends of the Earth",
        "logo": "logo_pics/foe1.jpg",
        "desc": "Friends of the Earth strives for a more healthy and just world. We understand that the challenges facing our planet call for more than half measures, so we push for the reforms that are needed, not merely the ones that are politically easy. Sometimes, this involves speaking uncomfortable truths to power and demanding more than people think is possible. It’s hard work. But the pressures facing our planet and its people are too important for us to compromise. Friends of the Earth, as an outspoken leader in the environmental and progressive communities, seeks to change the perception of the public, media, and policymakers — and effect policy change — with hard-hitting, well-reasoned policy analysis and advocacy campaigns that describe what needs to be done, rather than what is seen as politically feasible or politically correct. This hard-hitting advocacy has been the key to our successful campaigns over our 47-year history.",
        "page": "https://foe.org/"
        }
    ]

    association_select = st.sidebar.selectbox("Select your Enviro Hero", [association["name"] for association in associations])

    d = next((d for d in associations if d.get("name") == association_select), None)
    st.image(d["logo"], width = 200)
    st.header(d["name"])
    st.write(d["desc"])
    st.markdown(d["page"])
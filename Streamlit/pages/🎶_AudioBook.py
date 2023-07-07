import streamlit as st
import streamlit.components.v1 as components
import random
import pandas as pd

# -------------- app config ---------------

st.set_page_config(page_title="Audio Book", page_icon="🎶")

password = st.text_input("Input Password", type="password")

if password == st.secrets["password"]:
    st.write("You're the chosen one.")
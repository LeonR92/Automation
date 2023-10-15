import pandas as pd
import streamlit as st
import pygwalker as pyg
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
 
# Add Title
st.title("Use Pygwalker In Streamlit")

df = pd.read_csv("dataset.csv")
walker = pyg.walk(df)

pyg_html = pyg.to_html(df)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
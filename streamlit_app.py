from bz2 import compress
import altair as alt
import pandas as pd
import streamlit as st
# from st_aggrid import AgGrid

'''
# The Guardian Analysis
#### What role do climate related news play on The Guardian?
'''

articles = pd.read_csv("data/clean/2022_clean.csv.zip", compression="zip")

st.write(articles)

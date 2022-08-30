from dataclasses import dataclass
import streamlit as st 
import pandas as pd 

class Opportunity:
    def __init__(self, info: dict) -> None:
        self.link: str = info['link']
        self.company: str = info['company']

df = pd.read_excel("data/opportunities.xlsx")
opportunities = [Opportunity(row) for _, row in df.iterrows()]
st.write("hello world!")
st.write(opportunities)
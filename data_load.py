import streamlit as st
import pandas as pd


st.title('Coffee sales Dashboard')
file=st.file_uploader("Upload csv file", type=["csv"])
if file :
  df=pd.read_csv(file)
  st.subheader("Data Preview")
  st.dataframe(df)

if file :
  st.subheader("Summary stats")
  st.write(df.describe())

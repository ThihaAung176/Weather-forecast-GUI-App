import streamlit as st
import plotly.express as px
st.title("Weather Forecast for the next days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1,max_value=5, help="Select the number of forecast days")
optioin = st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{optioin} for the next {days} in {place}")
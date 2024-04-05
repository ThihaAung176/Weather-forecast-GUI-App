import streamlit as st
import plotly.express as px
st.title("Weather Forecast for the next days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1,max_value=5, help="Select the number of forecast days")
optioin = st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{optioin} for the next {days} in {place}")

def get_date(days):
    dates = ["2024-10-4", "2024-11-4","2024-15-4"]
    temperatures = [11,13,15]
    temperatures = [days*i for i in temperatures]
    return dates, temperatures

d,t = get_date(days)

figure = px.line(x= d, y= t ,labels={"x":"Dates", "y":"Temperature (C)"})
st.plotly_chart(figure)
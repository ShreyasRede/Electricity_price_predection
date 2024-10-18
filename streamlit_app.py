import streamlit as st

st.title('⚡Electricity Price Prediction')

st.info('Suppose that your business relies on computing services where the power consumed by your machines varies throughout the day. You do not know the actual cost of the electricity consumed by the machines throughout the day, but the organization has provided you with historical data of the price of the electricity consumed by the machines.')

d = st.date_input("Select The Date", format="DD/MM/YYYY")
st.write(d)

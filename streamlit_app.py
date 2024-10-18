import streamlit as st

st.title('⚡Electricity Price Prediction')

st.info('Suppose that your business relies on computing services where the power consumed by your machines varies throughout the day. You do not know the actual cost of the electricity consumed by the machines throughout the day, but the organization has provided you with historical data of the price of the electricity consumed by the machines.')

Date =st.slider('Select a Date', min_value=1, max_value=31)
Month =st.slider('Select a Month', min_value=1, max_value=12)
st.info("you've selected date is",Date,"/",Month)
ForecastWindProduction =st.slider('Forecast Wind Production', min_value=10.00, max_value=100.00)
st.info(ForecastWindProduction)

import streamlit as st
import pandas as pd
import numpy as np
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/electricity.csv")

st.title('⚡Electricity Price Prediction')

st.info('Suppose that your business relies on computing services where the power consumed by your machines varies throughout the day. You do not know the actual cost of the electricity consumed by the machines throughout the day, but the organization has provided you with historical data of the price of the electricity consumed by the machines.')

Date =st.slider('Select a Date', min_value=1, max_value=31)
Month =st.slider('Select a Month', min_value=1, max_value=12)
st.write("you've selected date is",Date,"/",Month)
ForecastWindProduction =st.slider('Forecast Wind Production', min_value=10.00, max_value=100.00)
st.info(ForecastWindProduction)
SystemLoadEA= st.number_input("Enter a SystemLoadEA")
SMPEA= st.number_input("Enter a SMPEA")
ORKTemperature= st.number_input("Temperature")
ORKWindspeed= st.number_input("Windspeed")
CO2Intensity= st.number_input("CO2Intensity")
ActualWindProduction= st.number_input("ActualWindProduction")
SystemLoadEP2= st.number_input("SystemLoadEP2")
if st.button("submit"):
    data = {'Day':Date,
            'Month':Month,
            'ForecastWindProduction':ForecastWindProduction,
            'SystemLoadEA':SystemLoadEA,
            'SMPEA':SMPEA,
            'ORKTemperature':ORKTemperature,
            'ORKWindspeed':ORKWindspeed,
            'CO2Intensity':CO2Intensity,
            'ActualWindProduction':ActualWindProduction,
            'SystemLoadEP2':SystemLoadEP2}
    input_data=pd.Dataframe(data,index=[0])

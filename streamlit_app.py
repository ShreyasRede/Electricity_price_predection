import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/electricity.csv")
    return data.dropna()

data = load_data()

# Title and Introduction
st.title('⚡ Electricity Price Prediction')
st.info('Suppose your business relies on computing services where the power consumed by your machines varies throughout the day. '
        'You do not know the actual cost of the electricity consumed by the machines throughout the day, but the organization '
        'has provided you with historical data of the price of electricity consumed by the machines.')

# Prepare features and target
x = data[["Day", "Month", "ForecastWindProduction", "SystemLoadEA",
          "SMPEA", "ORKTemperature", "ORKWindspeed", "CO2Intensity",
          "ActualWindProduction", "SystemLoadEP2"]]
y = data["SMPEP2"]

# Train-test split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor()
model.fit(xtrain, ytrain)

# Function for prediction
def predict_price(Date, Month, ForecastWindProduction, SystemLoadEA, SMPEA, ORKTemperature,
                  ORKWindspeed, CO2Intensity, ActualWindProduction, SystemLoadEP2):
    input_data = np.array([[Date, Month, ForecastWindProduction, SystemLoadEA, SMPEA, ORKTemperature,
                            ORKWindspeed, CO2Intensity, ActualWindProduction, SystemLoadEP2]])
    return model.predict(input_data)

# Input features
st.header("Input Features")
Date = st.slider('Select a Date', min_value=1, max_value=31)
Month = st.slider('Select a Month', min_value=1, max_value=12)
ForecastWindProduction = st.slider('Forecast Wind Production (MW)', min_value=10.00, max_value=100.00)
SystemLoadEA = st.number_input("Enter SystemLoadEA (MW)", min_value=0.00, value=100.00)
SMPEA = st.number_input("Enter SMPEA", min_value=0.00, value=50.00)
ORKTemperature = st.number_input("Temperature (°C)", min_value=-10.0, value=15.0)
ORKWindspeed = st.number_input("Windspeed (m/s)", min_value=0.0, value=5.0)
CO2Intensity = st.number_input("CO2 Intensity (gCO2/kWh)", min_value=0.0, value=200.0)
ActualWindProduction = st.number_input("Actual Wind Production (MW)", min_value=0.0, value=50.0)
SystemLoadEP2 = st.number_input("SystemLoadEP2 (MW)", min_value=0.0, value=100.0)

# Prediction
if st.button("Submit"):
    try:
        prediction = predict_price(Date, Month, ForecastWindProduction, SystemLoadEA, SMPEA, ORKTemperature,
                                   ORKWindspeed, CO2Intensity, ActualWindProduction, SystemLoadEP2)
        st.success(f"The predicted electricity price (SMPEP2) is: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")


import streamlit as st
import numpy as np
import pickle

with open('california_housing_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("California Housing Price Prediction")

#8Widgets
medInc = st.number_input("Median Income", min_value = 0.0, max_value = 15.0, value = 3.0)
houseAge = st.number_input("House Age", min_value = 0, max_value = 52, value = 28)
aveRooms = st.number_input("Average Number of Rooms", min_value = 1, max_value = 10, value = 5)
aveBedrms = st.number_input("Average Number of Bedrooms", min_value = 1, max_value = 5, value = 2)
population = st.number_input("Population", min_value = 0, max_value = 40000, value = 1000)
aveOccup = st.number_input("Average Occupancy", min_value = 1, max_value = 10, value = 3)
latitude = st.number_input("Latitude", min_value = 32.0, max_value = 42.0, value = 36.0)
longitude = st.number_input("Longitude", min_value = -124.0, max_value = -114.0, value = -119.0)

#Prediction
if st.button("Predict"):
    input_data = np.array([[medInc, houseAge, aveRooms, aveBedrms, population, aveOccup, latitude, longitude]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Median House Value: ${prediction[0]*100000:.2f}")
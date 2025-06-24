import numpy as np
import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open("weather(logistic) (1).sva", 'rb'))

# Streamlit setup
st.set_page_config(page_title="Weather Predictor")
st.title("Weather Prediction App")
st.markdown("### Enter weather details below to predict the weather type:")

# Input Fields (no icons/emojis)
temperature = st.number_input("Temperature (°C)", -50.0, 60.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0)
wind_speed = st.number_input("Wind Speed (km/h)", 0.0, 150.0)
pressure = st.number_input("Pressure (hPa)", 800.0, 1100.0)
visibility = st.number_input("Visibility (km)", 0.0, 50.0)
dew_point = st.number_input("Dew Point (°C)", -20.0, 30.0)
cloud_cover = st.number_input("Cloud Cover (%)", 0.0, 100.0)
uv_index = st.number_input("UV Index", 0.0, 15.0)
precipitation = st.number_input("Precipitation (mm)", 0.0, 500.0)
solar_radiation = st.number_input("Solar Radiation (W/m²)", 0.0, 1500.0)

# Prediction
if st.button("Predict Weather"):
    input_data = np.array([[temperature, humidity, wind_speed, pressure,
                            visibility, dew_point, cloud_cover, uv_index,
                            precipitation, solar_radiation]])

    prediction = model.predict(input_data)[0]

    label_map = {0: "Sunny", 1: "Rainy", 2: "Cloudy"}
    result = label_map.get(prediction, str(prediction))

    st.subheader("Predicted Weather:")
    st.success(f"{result}")

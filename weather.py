import numpy as np
import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open("weather(logistic) (1).sva", 'rb'))

st.set_page_config(page_title="Weather Predictor")
st.title("Weather Prediction App")
st.markdown("Enter the weather details below:")

# Define a function to safely convert text input to float
def safe_float_input(label):
    value = st.text_input(label)
    try:
        return float(value)
    except:
        return None

# Get 10 inputs from user without steppers
temperature = safe_float_input("Temperature (°C)")
humidity = safe_float_input("Humidity (%)")
wind_speed = safe_float_input("Wind Speed (km/h)")
pressure = safe_float_input("Pressure (hPa)")
visibility = safe_float_input("Visibility (km)")
dew_point = safe_float_input("Dew Point (°C)")
cloud_cover = safe_float_input("Cloud Cover (%)")
uv_index = safe_float_input("UV Index")
precipitation = safe_float_input("Precipitation (mm)")
solar_radiation = safe_float_input("Solar Radiation (W/m²)")

# Predict only if all inputs are valid
if st.button("Predict Weather"):
    inputs = [temperature, humidity, wind_speed, pressure,
              visibility, dew_point, cloud_cover, uv_index,
              precipitation, solar_radiation]

    if None in inputs:
        st.error("Please enter valid numeric values in all fields.")
    else:
        input_array = np.array([inputs])
        prediction = model.predict(input_array)[0]
        label_map = {0: "Sunny", 1: "Rainy", 2: "Cloudy"}
        result = label_map.get(prediction, str(prediction))
        st.subheader("Predicted Weather:")
        st.success(result)

import numpy as np
import pickle
import streamlit as st

# Load model
model = pickle.load(open("C:/Users/Vraj/OneDrive/Desktop/internship/weather app/weather(logistic) (1).sva", 'rb'))

st.set_page_config(page_title="Weather Predictor")
st.title("Weather Prediction App")
st.markdown("Enter the weather details below to predict the weather type.")

# Function to get float input safely
def safe_float_input(label, placeholder=""):
    value = st.text_input(label, placeholder=placeholder)
    try:
        return float(value)
    except:
        return None

# Inputs with hints
temperature = safe_float_input("Temperature (°C)", "e.g. 25")
humidity = safe_float_input("Humidity (%)", "0 to 100")
wind_speed = safe_float_input("Wind Speed (km/h)", "e.g. 12")
pressure = safe_float_input("Pressure (hPa)", "Typical: 1013")
visibility = safe_float_input("Visibility (km)", "e.g. 10")
dew_point = safe_float_input("Dew Point (°C)", "e.g. 16")
cloud_cover = safe_float_input("Cloud Cover (%)", "0 (clear) to 100 (overcast)")
uv_index = safe_float_input("UV Index", "0 (low) to 11+ (extreme)")
precipitation = safe_float_input("Precipitation (mm)", "e.g. 0 if no rain")
solar_radiation = safe_float_input("Solar Radiation (W/m²)", "e.g. 500")

# Prediction button
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

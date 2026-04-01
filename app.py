import streamlit as st
import pandas as pd
import joblib

st.title("Parcel Delivery Delay Predictor")
st.markdown("Enter delivery details to predict if a parcel will be delayed:")

# Load trained model
rf = joblib.load('rf_model.pkl')

# User inputs
distance = st.slider("Distance (km)", 1, 50)
hour = st.slider("Hour of delivery (0-23)", 0, 23)
traffic = st.selectbox("Traffic", ["Low", "Medium", "High"])
weather = st.selectbox("Weather", ["Clear", "Rain", "Storm"])
vehicle = st.selectbox("Vehicle", ["Bike", "Van", "Truck"])

# Feature engineering
is_peak = 1 if (7 <= hour <= 9) or (17 <= hour <= 19) else 0

# One-hot encoding
traffic_medium = 1 if traffic=="Medium" else 0
traffic_high = 1 if traffic=="High" else 0
weather_rain = 1 if weather=="Rain" else 0
weather_storm = 1 if weather=="Storm" else 0
vehicle_van = 1 if vehicle=="Van" else 0
vehicle_truck = 1 if vehicle=="Truck" else 0

# Prepare input DataFrame
input_df = pd.DataFrame([{
    'distance_km': distance,
    'hour': hour,
    'is_peak': is_peak,
    'traffic_Medium': traffic_medium,
    'traffic_High': traffic_high,
    'weather_Rain': weather_rain,
    'weather_Storm': weather_storm,
    'vehicle_Van': vehicle_van,
    'vehicle_Truck': vehicle_truck
}])

# Ensure all model columns exist
for col in rf.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[rf.feature_names_in_]

# Prediction
prediction = rf.predict(input_df)[0]

if st.button("Predict Delay"):
    if prediction == 1:
        st.error("⚠️ This delivery is likely DELAYED!")
    else:
        st.success("✅ This delivery is likely ON-TIME.")

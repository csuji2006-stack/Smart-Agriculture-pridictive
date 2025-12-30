import streamlit as st, requests

st.title("🌱 Advanced Smart Irrigation System")

cols = st.columns(4)
soil = cols[0].slider("Soil",0,100)
temp = cols[1].slider("Temp",0,50)
hum  = cols[2].slider("Humidity",0,100)
rain = cols[3].slider("Rain",0,20)

if st.button("Predict Irrigation"):
    res = requests.post("http://localhost:8000/predict",json={
        "soil_moisture":soil,
        "temperature":temp,
        "humidity":hum,
        "rainfall":rain
    })
    st.success(res.json())
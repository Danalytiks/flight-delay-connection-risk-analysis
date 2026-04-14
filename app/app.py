import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pathlib import Path

MODELS = Path(__file__).parent.parent / "models"

st.set_page_config(page_title="GateRunner", page_icon="✈️", layout="centered")

@st.cache_resource
def load():
    return (
        joblib.load(MODELS / "model_binary.joblib"),
        joblib.load(MODELS / "carriers.joblib"),
        joblib.load(MODELS / "airports.joblib"),
        joblib.load(MODELS / "features.joblib"),
        joblib.load(MODELS / "carrier_risk_map.joblib"),
        joblib.load(MODELS / "route_risk_map.joblib"),
    )

model, carriers, airports, features, carrier_risk, route_risk = load()

st.title("✈️ GateRunner")
st.subheader("Flight Connection Risk Estimator")
st.divider()

col1, col2 = st.columns(2)
with col1:
    carrier = st.selectbox("Airline", carriers)
    origin  = st.selectbox("Origin Airport", airports)
    dest    = st.selectbox("Destination Airport", airports)
with col2:
    month       = st.slider("Month", 1, 12, 6)
    day_of_week = st.selectbox("Day of Week", [1,2,3,4,5,6,7], format_func=lambda x: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][x-1])
    dep_hour    = st.slider("Departure Hour", 0, 23, 8)
    distance    = st.number_input("Distance (miles)", min_value=50, max_value=5000, value=500)

st.divider()

if st.button("Check Connection Risk", use_container_width=True, type="primary"):
    le_c = LabelEncoder().fit(carriers)
    le_a = LabelEncoder().fit(airports)

    row = pd.DataFrame([{
        "month":             month,
        "day_of_week":       day_of_week,
        "is_weekend":        1 if day_of_week in [6,7] else 0,
        "dep_hour":          dep_hour,
        "op_unique_carrier": le_c.transform([carrier])[0],
        "origin":            le_a.transform([origin])[0],
        "dest":              le_a.transform([dest])[0],
        "distance":          distance,
        "route_risk_rate":   route_risk.get((origin, dest), 0.08),
        "carrier_risk_rate": carrier_risk.get(carrier, 0.08),
    }])[features]

    pred  = model.predict(row)[0]
    proba = model.predict_proba(row)[0][0] * 100

    st.subheader("Result")
    if pred == 0:
        st.error(f"⚠️ AT RISK — Estimated risk: **{proba:.0f}%**\n\n💡 Consider a longer layover.")
    else:
        st.success(f"✅ SAFE — Estimated risk: **{proba:.0f}%**\n\n💡 Have a great trip!")

st.divider()
st.caption("GateRunner · BTS Flight Data 2024 · Random Forest")

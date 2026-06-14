import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Smart Home Energy Monitor",
    layout="wide"
)

st.title("🏠 Smart Home Energy Monitoring Dashboard")

try:
    df = pd.read_csv("data/energy_log.csv")

    latest = df.iloc[-1]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Voltage (V)",
        latest["Voltage"]
    )

    col2.metric(
        "Current (A)",
        latest["Current"]
    )

    col3.metric(
        "Power (W)",
        latest["Power"]
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Energy (kWh)",
        latest["Energy"]
    )

    col5.metric(
        "Cost (₹)",
        latest["Cost"]
    )

    col6.metric(
        "Alert Status",
        latest["Alert"]
    )

    st.subheader("Power Consumption Trend")

    fig, ax = plt.subplots()

    ax.plot(df["Power"])

    ax.set_xlabel("Reading Number")
    ax.set_ylabel("Power (W)")

    st.pyplot(fig)

    st.subheader("Energy Usage Log")

    st.dataframe(df)

except Exception as e:
    st.error(f"Error loading data: {e}")
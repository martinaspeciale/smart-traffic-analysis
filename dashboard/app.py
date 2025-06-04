
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Title
st.title("🚦 Smart Traffic Analysis Dashboard")

# Load data
conn = sqlite3.connect("database/traffic.db")
df = pd.read_sql("SELECT * FROM traffic_data_clustered", conn)
conn.close()

# Select sensor
sensor = st.selectbox("Select a Sensor", df["location"].unique())
sensor_df = df[df["location"] == sensor].copy()
sensor_df["timestamp"] = pd.to_datetime(sensor_df["timestamp"])
sensor_df.set_index("timestamp", inplace=True)

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(sensor_df)

# Cluster Plot
st.subheader("Congestion Clustering")
fig1, ax1 = plt.subplots()
scatter = ax1.scatter(sensor_df["vehicle_count"], sensor_df["average_speed_kmph"],
                     c=sensor_df["congestion_cluster"], s=100, edgecolors='k')
ax1.set_xlabel("Vehicle Count")
ax1.set_ylabel("Average Speed (km/h)")
ax1.grid(True)
st.pyplot(fig1)

# Time Series Forecast
st.subheader("Traffic Forecast (ARIMA)")
model = ARIMA(sensor_df["vehicle_count"], order=(1, 1, 1))
fitted_model = model.fit()
forecast = fitted_model.forecast(steps=5)

fig2, ax2 = plt.subplots()
ax2.plot(sensor_df["vehicle_count"], label="Observed")
ax2.plot(pd.date_range(start=sensor_df.index[-1], periods=6, freq="H")[1:], forecast,
         label="Forecast", linestyle="--")
ax2.set_xlabel("Time")
ax2.set_ylabel("Vehicle Count")
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

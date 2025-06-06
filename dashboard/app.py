# dashboard/app.py

import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import plotly.express as px

# Title
st.title("🚦 Smart Traffic Analysis Dashboard")

# Load data
conn = sqlite3.connect("../database/traffic.db")
df = pd.read_sql("SELECT * FROM traffic_data", conn)
conn.close()

# Basic check
if df.empty:
    st.warning("⚠️ No data found in traffic_data. Please run the ETL pipeline first.")
    st.stop()

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df.dropna(subset=["timestamp"])
df = df.sort_values("timestamp")

# Sidebar: select city
cities = df["city_name"].unique()
selected_city = st.sidebar.selectbox("Select a City", sorted(cities))

# Filter by city
df_city = df[df["city_name"] == selected_city]

# Sidebar: select street
streets = df_city["street_name"].unique()
selected_street = st.sidebar.selectbox("Select a Street", sorted(streets))

# Filter by street
df_street = df_city[df_city["street_name"] == selected_street]

# KPI
st.header(f"Traffic Data for {selected_city} — {selected_street}")
st.write(f"**Number of records:** {len(df_street)}")
st.write(f"**Average vehicle count:** {df_street['vehicle_count'].mean():.2f}")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df_street)

# Line chart: vehicle count over time
# st.subheader("Vehicle Count Over Time")
# fig1, ax1 = plt.subplots()
# ax1.plot(df_street["timestamp"], df_street["vehicle_count"], marker='o', linestyle='-')
# ax1.set_xlabel("Timestamp")
# ax1.set_ylabel("Vehicle Count")
# ax1.grid(True)
# st.pyplot(fig1)

# Line chart: vehicle count over time (aggregated per hour)
st.subheader("Vehicle Count Over Time (Hourly Average)")

# Set timestamp as index
df_street_hourly = df_street.set_index("timestamp").resample('H').mean(numeric_only=True)

# Make plot wider and rotate x-axis labels
fig1, ax1 = plt.subplots(figsize=(12, 6))  # width 12, height 6

ax1.plot(df_street_hourly.index, df_street_hourly["vehicle_count"], marker='o', linestyle='-')

ax1.set_xlabel("Timestamp")
ax1.set_ylabel("Vehicle Count (Hourly Avg)")
ax1.grid(True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Adjust layout to avoid clipping
fig1.tight_layout()

# Show in Streamlit
st.pyplot(fig1)


# Line chart: vehicle count over time (Hourly Average) — Plotly version
st.subheader("Vehicle Count Over Time (Hourly Average) — Interactive")

df_street_hourly = df_street.set_index("timestamp").resample('H').mean(numeric_only=True).reset_index()

fig2 = px.line(
    df_street_hourly,
    x="timestamp",
    y="vehicle_count",
    title=f"Hourly Vehicle Count — {selected_city} / {selected_street}",
    labels={"vehicle_count": "Vehicle Count (Hourly Avg)", "timestamp": "Timestamp"}
)

st.plotly_chart(fig2)


# Bar chart: vehicle type distribution
st.subheader("Vehicle Type Distribution")
vehicle_type_counts = df_street["vehicle_type"].value_counts()
st.bar_chart(vehicle_type_counts)

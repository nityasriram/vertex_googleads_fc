
import streamlit as st
import pandas as pd
import altair as alt

# Load data
df = pd.read_csv("monthly_search_volume_by_seed_keyword_CT17_vertex.csv")

# Melt wide data to long format
df_long = df.melt(id_vars=["seed_keyword"], var_name="month", value_name="volume")
df_long["month"] = pd.to_datetime(df_long["month"])

# Sidebar: Select a keyword
selected = st.selectbox("Choose a seed keyword", df_long["seed_keyword"].unique())

# Filter data
filtered = df_long[df_long["seed_keyword"] == selected]

# Line chart
line = alt.Chart(filtered).mark_line().encode(
    x="month:T",
    y="volume:Q",
    tooltip=["month:T", "volume"]
).properties(
    title=f"Search Volume Trend for '{selected}'",
    width=700,
    height=400
)

st.altair_chart(line)

# Stats
st.metric("Max", int(filtered["volume"].max()))
st.metric("Min", int(filtered["volume"].min()))

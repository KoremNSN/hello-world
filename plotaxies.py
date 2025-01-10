import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interactive Data Playground")

# Initialize example data
df = pd.DataFrame({
    "Name": ["PE", "SEE FAR CBT"],
    "Closeness": [1.5, 2.0],
    "SD X": [0.3, 0.2],
    "Intensity": [0.8, 1.2],
    "SD Y": [0.1, 0.3],
})

# Interactive table with the ability to add rows
edited_df = st.data_editor(df, num_rows='dynamic')

# Scatter plot with error bars
fig = px.scatter(
    edited_df,
    x="Closeness",
    y="Intensity",
    error_x="SD X",
    error_y="SD Y",
    text="Name",
    title="Scatter Plot with Standard Deviations"
)
# Add lines at x=0, y=0
fig.add_vline(x=0, line_color="black")
fig.add_hline(y=0, line_color="black")

# Set axis limits to [-10, 10]
fig.update_layout(
    xaxis=dict(range=[-10, 10]),
    yaxis=dict(range=[-10, 10])
)

fig.update_traces(textposition="top center")
st.plotly_chart(fig)

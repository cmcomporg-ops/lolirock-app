import streamlit as st
import pandas as pd
import plotly.express as px
from theme import lr_theme

lr_theme("assets/volta.jpg")

import base64

# Load your audio file
audio_file = "assets/3.mp3"
with open(audio_file, "rb") as f:
    audio_bytes = f.read()
    base64_audio = base64.b64encode(audio_bytes).decode()

# Custom HTML audio player (hidden)
audio_html = f"""
<audio autoplay loop style="display:none">
    <source src="data:audio/mp3;base64,{base64_audio}" type="audio/mp3">
</audio>
"""

# Inject the audio
st.markdown(audio_html, unsafe_allow_html=True)

st.markdown("### 🔄 Navigate to Another Page")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Homepage",use_container_width=True):
        st.switch_page("lolirock.py")

with col2:
    if st.button("📊 Playlists",use_container_width=True):
        st.switch_page("pages/playlists.py")

with col3:
    if st.button("🎶 Songs",use_container_width=True):
        st.switch_page("pages/songs.py")

# Load data
data = pd.read_csv("lolirock_imdb_ratings.csv")

# Create Plotly line chart
fig = px.line(
    data,
    x="Episode_Number",
    y="IMDb_Rating",
    title="LoliRock IMDb Ratings",
    height=600
)
#Customizes the chart layout
fig.update_layout(
    title=dict(
        text="LoliRock IMDb Ratings",
        font=dict(
            family="Indie Flower",
            size=28,
            color="white"
        ),
        x=0.5,
        xanchor='center'
    ),
    font=dict(
        family="Indie Flower",
        color="white"
    ),
    xaxis=dict(
        title=dict(text="Episode Number"),
        gridcolor='white'
    ),
    yaxis=dict(
        title=dict(text="IMDb Rating"),
        gridcolor='white'
    ),
    paper_bgcolor='rgba(0,0,0,0.4)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Glowing line
fig.update_traces(line=dict(color='rgba(135, 206, 250, 0.8)', width=3))

st.plotly_chart(fig, use_container_width=True)

#I figured out how to make my line chart using this streamlit website:
#(Source: https://docs.streamlit.io/develop/api-reference/charts/st.line_chart retrieved in April 2025)

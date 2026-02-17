import streamlit as st
import pandas as pd
import plotly.express as px
from theme import lr_theme

lr_theme("assets/ephedia.jpg")

import base64

# Load your audio file
audio_file = "assets/2.mp3"
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
    if st.button("⭐ Ratings",use_container_width=True):
        st.switch_page("pages/ratings.py")

# Connect to MySQL using st.connection (configured in .streamlit/secrets.toml)
conn = st.connection("mysql", type="sql")
df = conn.query("SELECT * FROM SongAppearances", ttl=600)

# Melt wide format to long format
long_df = df.melt(id_vars=["Episode_Number"], var_name="Song", value_name="Appeared")
long_df = long_df[long_df["Appeared"] == 1]  # Keep only rows where song appeared


# Replace underscores in song titles
long_df["Song"] = long_df["Song"].str.replace("_", " ")

# Scatter chart using Plotly

fig = px.scatter(
    long_df,
    x="Episode_Number",
    y="Song",
    color="Song",  # Color code by song name
    title="Song Appearances per Episode",
    height=700
)

# Customized the marker style
fig.update_traces(marker=dict(size=10, opacity=0.75), selector=dict(mode='markers'))
# Customize axis labels and layout
fig.update_layout(
    title=dict(
        text='Song Appearances per Episode',
        font=dict(
            family='Indie Flower',
            size=28,
            color='white'
        ),
        x=0.5,
        xanchor='center'
    ),
    font=dict(
        family='Indie Flower',
        color='white'
    ),
    xaxis=dict(
        title=dict(text='Episode Number'),
        gridcolor='white'
    ),
    yaxis=dict(
        title=dict(text='Song Title'),
        gridcolor='white'
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0.5)'
)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

#I got the connection to streamlit from mysql from:
#(Source: https://docs.streamlit.io/develop/tutorials/databases/mysql retrieved in April 2025)

#I got the code to make the chart from:
#(Source: https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart retrieved in April 2025)

#I got the customization for the chart from:
#(Source: https://plotly.com/python/wide-form/ retrieved in April 2025)

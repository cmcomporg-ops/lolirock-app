import streamlit as st
import pandas as pd
from theme import lr_theme
import plotly.express as px

st.set_page_config(layout="wide")
import base64

# Load your audio file
audio_file = "assets/1.mp3"
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
    if st.button("🏠 Homepage",width='stretch'):
        st.switch_page("lolirock.py")

with col2:
    if st.button("🎶 Songs",width='stretch'):
        st.switch_page("pages/songs.py")

with col3:
    if st.button("⭐ Ratings",width='stretch'):
        st.switch_page("pages/ratings.py")

lr_theme("assets/xeris.jpg")
data = {
    'Playlist': [
        'Season 2 - Full Episodes', 'Season 1 - Full Episodes', 'IN REAL LIFE!', 'Soundtrack', 
        'Our Top Fans!', 'Season 2', 'Best Moments Compilations', 'Season 2 Songs!', 
        'Princess Transformations', 'Month of Making: Making Music', 'Fall in Love with Iris & Nathaniel', 
        'Karaoke', 'Promo', 'Shorts', 'Songs', 'Transformations Scenes', 'Behind the Scenes'
    ],
    'Number of Videos': [
        65, 37, 5, 20, 12, 112, 78, 19, 12, 9, 12, 21, 4, 39, 44, 118, 118
    ]
}
df = pd.DataFrame(data)

fig = px.bar(
    df,
    x='Playlist',
    y='Number of Videos',
    opacity=0.6,
    title='LoliRock Playlist Analysis',
    height=600,
    width=1200

)
fig.update_layout(
    title=dict(
        text='LoliRock Playlist Analysis',
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
        color='white',
        size=18
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0.4)',
    xaxis=dict(
        tickangle=-45,
        title=dict(text='Playlist')
    ),
    yaxis=dict(
        gridcolor='white',
        title=dict(text='Number of Videos')
    )
)

st.plotly_chart(fig, width='stretch')


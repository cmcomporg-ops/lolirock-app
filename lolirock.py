import streamlit as st
from theme import lr_theme

st.set_page_config(page_title="LoliRock Dashboard", layout="wide")


lr_theme("assets/p3.jpg")
import base64

# Load your audio file
audio_file = "assets/lolirock.mp3"
with open(audio_file, "rb") as f:
    audio_bytes = f.read()
    base64_audio = base64.b64encode(audio_bytes).decode()

# Custom HTML audio player (hidden)
audio_html = f"""
<audio id="bg-music" autoplay loop hidden>
    <source src="data:audio/mp3;base64,{base64_audio}" type="audio/mp3">
</audio>
"""

# Inject the audio
st.markdown(audio_html, unsafe_allow_html=True)

# Create buttons for pages
col1, col2, col3 = st.columns(3)


with col1:
    if st.button("📊 Playlist Stats",use_container_width=True):
        st.switch_page("pages/playlists.py")  

with col2:
    if st.button("🎶 Song Appearances",use_container_width=True):
        st.switch_page("pages/songs.py")

with col3:
    if st.button("⭐ IMDb Ratings",use_container_width=True):
        st.switch_page("pages/ratings.py")


# Title + Subtitle
st.markdown("<h1 style='text-align: center; font-size: 60px;'>Welcome to the LoliRock World🎤 </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #f4c2c2;'>Meet the band and explore their magic!!!</h3>", unsafe_allow_html=True)

# Tabs for band and members
tabs = st.tabs(["💫 The Band", "💖 Iris", "🔹 Talia", "🌙 Auriana"])

with tabs[0]:
    st.markdown("### 💫 About LoliRock")
    st.markdown("""
    <p style='font-size:20px;'>
    LoliRock is a magical girl band made up of Iris, Talia, and Auriana. With music, friendship, and magical transformations, 
    they fight evil while sharing their passion for performance. Their songs inspire hope and harmony and channels 
    their crystal powers.
    <p>
    """,unsafe_allow_html=True)
    st.markdown("#### Fun Fact:")
    st.markdown("""
     <p style='font-size:20px;'>
    The name "LoliRock" is a play on the phrases "LOL" (laugh out loud), and "i" (as in the Spanish conjunction meaning "and", and the word "rock".
     <p>
    """,unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/lol.jpg")

    with col2:
        st.image("assets/lol.gif",use_container_width=True)

with tabs[1]:
    st.markdown("### 💖 Iris – The Heart")
    st.markdown("""
    <p style='font-size:20px;'>
    Iris is the kind hearted and compassionate lead singer. She grew up on Earth with her Aunt Ellen, not knowing of her magical powers. She awakened her poweres with the help of Talia and Auriana, and now the 3 of them fight together to stop Gramorr from obtaining ultimate power.

    - **Weapon**: Scepter of Ephedia  
    - **Transformation Item**: Heart necklace 
    - **Kingdom**: Ephedia
    <p>
    """,unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/iris.jpg")

    with col2:
        st.image("assets/iris.gif")
        st.image("assets/i.jpg")
with tabs[2]:
    st.markdown("### 🔹 Talia – The Strategist")
    st.markdown("""
    <p style='font-size:20px;'>
    Talia is the brainy and serious guitarist/keytarist of the trio, often devising plans and guiding decisions with logic and precision. She joined together with Auriana, in search of Iris, to train her to recover Oracle Gems that would be used to defeat Gramorr once and for all.

    - **Weapon**: Wand of Xeris 
    - **Transformation Item**: Blue Wristband  
    - **Kingdom**: Xeris
    <p>
    """,unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/talia.jpg")

    with col2:
        st.image("assets/talia.gif")
        st.image("assets/t.jpg")

with tabs[3]:
    st.markdown("### 🌙 Auriana – The Spark")
    st.markdown("""
    <p style='font-size:20px;'>
    Auriana is the bubbly and klutzy tambourinist of the group. She can get distracted easily and develops crushes on boys easily, but she is shown to be very dependable when help is needed and is pretty proficient in defensive spells. 

    - **Weapon**: Ribbon of Volta  
    - **Transformation Item**: Orange Ring
    - **Kingdom**: Volta
    <p>
    """,unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/a.jpg", width=500)

    with col2:
        st.image("assets/red.gif",use_container_width=True)
        st.image("assets/ar.jpg")

# I referenced the code for buttons from:
#(Source: https://docs.streamlit.io/develop/api-reference/widgets/st.button retrieved May 2025)

# I referenced the code for switching pages from:
#(Source: https://docs.streamlit.io/develop/api-reference/navigation/st.switch_page retrieved May 2025)

#I referenced the code for st.markdown from:
#(Source: https://docs.streamlit.io/develop/api-reference/text/st.markdown retrieved May 2025)

#I referenced the code for tabs from:
#(Source: https://docs.streamlit.io/develop/api-reference/layout/st.tabs retrieved May 2025)

#I copied this code for audio playback from:
#(Source: https://chatgpt.com/share/681881eb-a91c-8003-8760-3c73321db10e retrieved May 2025)

#I got my character info from:
#(Source: https://lolirock.fandom.com/wiki/Category:Characters retrieved May 2025)

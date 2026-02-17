import streamlit as st
import base64
# Loads the local image and encode it
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
def lr_theme(img_file="ephedia.jpg"):
    img_base64 = get_base64_image(img_file)


    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
)
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap');
        h1, h2, h3, h4, h5, h6,
        p, div, span,
        html, body, [class*="css"] {
            font-family: 'Indie Flower', cursive !important;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.6);
        }
        </style>
        """,
        unsafe_allow_html=True
)
    st.markdown(
        """
        <style>
        header[data-testid="stHeader"] {
            background-color: rgba(0, 0, 0, 0);
        }
        </style>
        """,
        unsafe_allow_html=True
)
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: rgba(0, 0, 0, 0.6);
        }
        </style>
        """,
        unsafe_allow_html=True
)
    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: rgba(0, 0, 0, 0.5);
            color: white;
            border-radius: 10px;
            border: 1px solid white;
        }
        </style>
        """, 
        unsafe_allow_html=True
)

#I got and modified the code to embedded a photo as the background of my app from:
#(Source: https://discuss.streamlit.io/t/how-do-i-use-a-background-image-on-streamlit/5067/5 retrieved on April 2025)

#I got and modified the code to add custom fonts from:
#(Source: https://discuss.streamlit.io/t/custom-fonts-on-streamlit/25984/3 retrieved on April 2025)

#I got and modified the code to make the sidebar and headbar transparent: 
#(Source: https://chatgpt.com/share/68157704-580c-8003-8d86-ff05e31cdc63 retrieved on May 2025)

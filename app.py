import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import base64

st.set_page_config(
    page_title="PreFeas",
    page_icon="🌍",
    layout="wide"
)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_page_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
        .stApp {
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
        }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def set_header_image_text_background(png_file,text):
    bin_str = get_base64(png_file)
    header_bg_img = f'''
    <style>
        header[data-testid="stHeader"] {{
            display: flex;
            background: url("data:image/png;base64,{bin_str}") 25% center no-repeat; 
            background-size: auto 80%;
            align-items: center;
            padding-left: 50px;
            background-color: lightgray; 
            height: 70px;
        }}
        header[data-testid="stHeader"]::after {{
            content: '{text}'; /* Add your desired text here */
            position: absolute;
            top: 50%; /* Vertically center the text */
            left: 75%; /* Adjust the left position to around 75% */
            transform: translate(-50%, -50%); /* Center the text vertically */
            color: #002244;
            font-size: 20px; /* Font size */
        }}
    </style>
    '''
    st.markdown(header_bg_img, unsafe_allow_html=True)

def set_header_image_image_background(png_file1, png_file2):
    bin_str1 = get_base64(png_file1)
    bin_str2 = get_base64(png_file2)
    header_bg_img = f'''
    <style>
        header[data-testid="stHeader"] {{
            display: flex;
            background: url("data:image/png;base64,{bin_str1}") 35% center no-repeat, url("data:image/png;base64,{bin_str2}") 65% center no-repeat; /* Separate with a comma */
            background-size: auto 80%;
            align-items: center;
            padding-left: 50px;
            background-color: lightgray; 
            height: 70px;
        }}

    </style>
    '''
    st.markdown(header_bg_img, unsafe_allow_html=True)
    
set_page_background('blue.jpg')
set_header_image_image_background('DTA Logo.png', "prefeas.png")

custom_css = """
<style>
    .reportview-container .main .block-container {
        padding-top: 0rem;
    }

    div.block-container {
        padding-top: 1rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .stDeployButton {
        display: none !important;
    }

    body {
        background-image: url("data:image/jpeg;base64,{base64_background}");
        background-size: cover;
    }
</style>
"""


st.markdown(custom_css, unsafe_allow_html=True)
st.write("")
st.write("")
col1, col2, col3 = st.columns([6,1,3])

with col1:
    st.components.v1.iframe("https://green-coast-0bf4a5b00.4.azurestaticapps.net", width=850, height=700)
with col3:
    st.markdown("<h3 style='color: white;'>Analytics</h3>", unsafe_allow_html=True)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Copper", "Iron ore", "Gypsum"])
    st.area_chart(chart_data)
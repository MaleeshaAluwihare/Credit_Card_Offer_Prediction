import streamlit as st
from streamlit_lottie import st_lottie
import json

# Load Lottie animation
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
# sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

#Styles
st.markdown("""
    <style>
    .centered-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-top: 1%;
        margin-bottom:0.5%;
    }
    .centered-animation {
        margin-top: -10%;
        margin-bottom: -10%;
    }
    .centered-para {
        font-size: 20px;
        text-align: center;
    }
    .form{
        margin-top: 10%;
        margin-bottom: 10%;
    }
    </style>
    """, unsafe_allow_html=True)

#heading
st.markdown('<div class="centered-title"> Welcome to Smart Credit Card Marketing! </div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
lottie_animation = load_lottie_file("../Styles/card.json")
with col2:
    st.markdown('<div class="centered-animation">',unsafe_allow_html=True)
    st_lottie(lottie_animation, height=400, width=400)
    st.markdown('</div>',unsafe_allow_html=True)

st.markdown('<div class="centered-para"> In today\'s competitive banking industry, reaching the right customers is more important than ever. Our platform is designed to help banks optimize their credit card marketing strategy by leveraging the power of predictive analytics.</div>',unsafe_allow_html=True)

st.markdown('<div class="form">',unsafe_allow_html=True)

user_input = st.text_input("Enter your name:")

selected_option = st.selectbox(
    'Choose your favorite fruit:',
    ('Apple', 'Banana', 'Orange', 'Mango')
)

st.markdown('</div>',unsafe_allow_html=True)
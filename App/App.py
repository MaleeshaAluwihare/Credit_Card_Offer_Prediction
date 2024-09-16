import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from streamlit_lottie import st_lottie
import json

loaded_model = '../TrainedModels/credit_card_lead_prediction_model.pkl'

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

def predict_lead_outcome(data):
    # Apply one-hot encoding and reindex to match training data
    encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
    
    # Example of how you might preprocess the data
    data_encoded = pd.get_dummies(data)
    all_columns = df.columns.drop('Lead_Outcome')
    data_encoded = data_encoded.reindex(columns=all_columns, fill_value=0)
    
    # Make prediction
    prediction = loaded_model.predict(data_encoded)
    return 'Yes' if prediction[0] == 1 else 'No'


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


with st.form(key='lead_prediction_form'):
    # Form inputs
    gender = st.selectbox('Gender', ['Male', 'Female'])
    month_income = st.number_input('Month Income', min_value=0)
    age = st.number_input('Age', min_value=0)
    occupation = st.selectbox('Occupation', ['Entrepreneur', 'Other', 'Salaried', 'Self_Employed'])
    credit_score = st.number_input('Credit Score', min_value=0)
    loan_status = st.selectbox('Loan Status', ['Yes', 'No'])
    existing_credit_cards = st.number_input('Existing Credit Cards', min_value=0)
    avg_account_balance = st.number_input('Average Account Balance', min_value=0)
    account_category = st.selectbox('Account Category', ['Savings Account', 'Current Account', 'Senior Citizens Account', 'Investment Account'])
    tenure_with_bank = st.number_input('Tenure with Bank', min_value=0)
    
    # Submit button
    submit_button = st.form_submit_button(label='Predict')
    
    if submit_button:
        # Prepare data for prediction
        input_data = pd.DataFrame({
            'Gender': [gender],
            'Month_Income': [month_income],
            'Age': [age],
            'Occupation': [occupation],
            'Credit_Score': [credit_score],
            'Loan_Status': [loan_status],
            'Existing_Credit_Cards': [existing_credit_cards],
            'Avg_Account_Balance': [avg_account_balance],
            'Account_Category': [account_category],
            'Tenure_with_Bank': [tenure_with_bank]
        })
        
        # Predict and display result
        prediction = predict_lead_outcome(input_data)
        st.write(f'Predicted Lead Outcome: {prediction}')

st.markdown('</div>',unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import json
import time
from sklearn.preprocessing import OneHotEncoder
from streamlit_lottie import st_lottie
import joblib

# Load the trained model and dataset
loaded_model = joblib.load('../TrainedModels/credit_card_lead_prediction_model.pkl')
df = pd.read_csv('../Dataset/processed_training_data.csv')

# Function to load Lottie animation
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Apply custom CSS
st.markdown("""
    <style>
    .centered-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .centered-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .centered-para{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
   }
    .centered-animation {
        margin-top: 40px;
        margin-bottom: 40px;
        justify-content: center;
    }
    .form-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .submit-button {
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Prediction function
def predict_lead_outcome(data):
    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    data_encoded = pd.get_dummies(data)
    all_columns = df.drop('Lead_Outcome', axis=1).columns
    data_encoded = data_encoded.reindex(columns=all_columns, fill_value=0)
    prediction = loaded_model.predict(data_encoded)
    return 'yes' if prediction[0] == 1 else 'no'

# Title
st.markdown('<div class="centered-title">Welcome to Smart Credit Card Marketing!</div>', unsafe_allow_html=True)

# animation
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="centered-animation">',unsafe_allow_html=True)
    lottie_animation = load_lottie_file("../Styles/creditcard.json")
    st_lottie(lottie_animation, height=200, width=300)
    st.markdown('</div>',unsafe_allow_html=True)

st.markdown('<div class="centered-para"> In today\'s competitive banking industry, reaching the right customers is more important than ever. Our platform is designed to help banks optimize their credit card marketing strategy by leveraging the power of predictive analytics.</div>',unsafe_allow_html=True)

# Form 
st.markdown('<div class="form-container">', unsafe_allow_html=True)
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
    submit_button = st.form_submit_button(label='Predict', use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

if submit_button:
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
    
    # Loading animation before result
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="centered-container">', unsafe_allow_html=True)
        lottie_animation = load_lottie_file("../Styles/loading.json")
        st_lottie(lottie_animation, height=150, width=300)
        st.markdown('</div>', unsafe_allow_html=True)
        time.sleep(3)

    placeholder.empty() 

    # Display the prediction result
    prediction = predict_lead_outcome(input_data)

    if prediction == 'yes':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            lottie_animation = load_lottie_file("../Styles/selected.json")
            st_lottie(lottie_animation, height=150, width=300)
        st.markdown('<div style="text-align: center; color: green; background-color: #d4edda; padding: 10px; border-radius: 5px;"><strong>Customer may show interest in a credit card offer</strong></div>', unsafe_allow_html=True)

    else:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            lottie_animation = load_lottie_file("../Styles/rejected.json")
            st_lottie(lottie_animation, height=150, width=300)
        st.markdown('<div style="text-align: center; color: red; background-color: #f8d7da; padding: 10px; border-radius: 5px;"><strong>Customer may not show interest in a credit card offer</strong></div>', unsafe_allow_html=True)

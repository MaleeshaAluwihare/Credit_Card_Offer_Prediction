import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
import json
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_lottie import st_lottie
import second

import streamlit as st

model=pickle.load(open('predictor.pickle','rb'))

df = pd.read_csv('bank_customer.csv')

st.markdown('<p class="custom-title" >Check The Cutomer Interest In Credit Card Offer</p>', unsafe_allow_html=True)

def load_lottiefile(filepath: str):
                with open(filepath) as f:
                    lottie_json = json.load(f)
                return lottie_json

lottie_file= load_lottiefile(r'..\predic\card3.json')
st_lottie(
                lottie_file,
                speed=0.1, 
                reverse=False,
                loop=True,
                quality='medium',
                
                height=200,
                key=None)

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.markdown(
        """
        <h2 style='color: #1f77b4; text-decoration: underline;'>Why We're Here</h2>
        <p style='font-size: 16px;'>We want to help you understand if customers are interested in credit card offers. Our tool makes it easy to see if a customer is likely to say 'Yes' or 'No' to your offer. This way, you can focus your efforts where they matter most.</p>
        """, 
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <h2 style='color: #ff7f0e; text-decoration: underline;'>What We Offer</h2>
        <p style='font-size: 16px;'>Our tool predicts whether a customer will be interested in a credit card offer. Just enter some customer details, and we’ll give you a clear 'Yes' or 'No' prediction. This helps you make better decisions and target your offers effectively.</p>
        """, 
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <h2 style='color: #2ca02c; text-decoration: underline;'>What We Value</h2>
        <p style='font-size: 16px;'>We value making your job easier with clear and accurate predictions. Our goal is to help you connect with customers who are most likely to be interested. Thank you for using our tool and letting us assist you in improving your marketing efforts.</p>
        """, 
        unsafe_allow_html=True
    )

st.write("\n\n\n\n\n\n\n\n\n")




# Sidebar for graph selection
st.sidebar.title("Visualization Options")
plot_type = st.sidebar.selectbox("Choose a plot type", ["Distribution", "By Target"])

# Dropdown for column selection
selected_column = st.sidebar.selectbox("Select a column to plot", df.columns)

st.markdown(f"<h3 style='color:black;'>Input Customer Details Here..</h3>", unsafe_allow_html=True)

def load_lottiefile(filepath: str):
                with open(filepath) as f:
                    lottie_json = json.load(f)
                return lottie_json

lottie_file= load_lottiefile(r'..\predic\face.json')
st_lottie(
                lottie_file,
                speed=0.3, 
                reverse=False,
                loop=True,
                quality='medium',
                
                height=200,
                key=None
            )

# Numerical inputs
month_income = st.number_input('Monthly Income', min_value=0, max_value=1000000, step=1000)
age = st.number_input('Age', min_value=18, max_value=100)
credit_score = st.number_input('Credit Score', min_value=300, max_value=850)
avg_account_balance = st.number_input('Average Account Balance', min_value=0, max_value=1000000, step=1000)

# Categorical inputs

gender = st.selectbox('Gender', ['Female', 'Male'])

occupation = st.selectbox('Occupation', ['Entrepreneur', 'Other', 'Salaried', 'Self_Employed'])

loan_status = st.selectbox('Loan Status', ['No', 'Yes'])

existing_credit_cards = st.selectbox('Existing Credit Cards', ['None', 'One Or More'])

account_category = st.selectbox('Account Category', ['X1', 'X2', 'X3', 'X4'])

tenure_with_bank = st.selectbox('Tenure with Bank', 
                                ['1', '2', '3', '4', '5', '5 to 10', 'more than 10 years'])


data = {
    'Unnamed: 0': 0,
    'Month_Income': month_income,
    'Age': age,
    'Credit_Score': credit_score,
    'Avg_Account_Balance': avg_account_balance,
    'Gender_Female': 1 if gender == 'Female' else 0,
    'Gender_Male': 1 if gender == 'Male' else 0,
    'Occupation_Entrepreneur': 1 if occupation == 'Entrepreneur' else 0,
    'Occupation_Other': 1 if occupation == 'Other' else 0,
    'Occupation_Salaried': 1 if occupation == 'Salaried' else 0,
    'Occupation_Self_Employed': 1 if occupation == 'Self_Employed' else 0,
    'Loan_Status_No': 1 if loan_status == 'No' else 0,
    'Loan_Status_Yes': 1 if loan_status == 'Yes' else 0,
    'Existing_Credit_Cards_None': 1 if existing_credit_cards == 'None' else 0,
    'Existing_Credit_Cards_One Or More': 1 if existing_credit_cards == 'One Or More' else 0,
    'Account_Category_X1': 1 if account_category == 'X1' else 0,
    'Account_Category_X2': 1 if account_category == 'X2' else 0,
    'Account_Category_X3': 1 if account_category == 'X3' else 0,
    'Account_Category_X4': 1 if account_category == 'X4' else 0,
    'Tenure_with_Bank_1': 1 if tenure_with_bank == '1' else 0,
    'Tenure_with_Bank_2': 1 if tenure_with_bank == '2' else 0,
    'Tenure_with_Bank_3': 1 if tenure_with_bank == '3' else 0,
    'Tenure_with_Bank_4': 1 if tenure_with_bank == '4' else 0,
    'Tenure_with_Bank_5': 1 if tenure_with_bank == '5' else 0,
    'Tenure_with_Bank_5 to 10': 1 if tenure_with_bank == '5 to 10' else 0,
    'Tenure_with_Bank_more than 10 years': 1 if tenure_with_bank == 'more than 10 years' else 0,
}

# Convert input to dataframe
input_data = pd.DataFrame([data])



# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    outcome = 'Interest' if prediction[0] == 1 else 'Not Interest'
    st.markdown(f"<h3 style='color:white;'>Prediction Result</h3>", unsafe_allow_html=True)

    if outcome=='Not Interest':
            st.markdown(f"<p style='color:red; font-size:20px;'>Based on the provided input data,The lead outcome to be: <strong>{outcome}</strong>.</p>", unsafe_allow_html=True)
            def load_lottiefile(filepath: str):
                with open(filepath) as f:
                    lottie_json = json.load(f)
                return lottie_json

            lottie_file= load_lottiefile(r'..\predic\not.json')
            st_lottie(
                lottie_file,
                speed=0.5, 
                reverse=False,
                loop=True,
                quality='medium',
                
                height=100,
                key=None)
    else:
            st.markdown(f"<p style='color:green; font-size:20px;'>Based on the provided input data,The lead outcome to be: <strong>{outcome}</strong>.</p>", unsafe_allow_html=True)  
            def load_lottiefile(filepath: str):
                with open(filepath) as f:
                    lottie_json = json.load(f)
                return lottie_json

            lottie_file= load_lottiefile(r'..\predic\correct.json')
            st_lottie(
                lottie_file,
                speed=0.5, 
                reverse=False,
                loop=True,
                quality='medium',
                
                height=200,
                key=None

)    

st.header("Data Visualizations",divider=True)
    
def load_lottiefile(filepath: str):
    with open(filepath) as f:
        lottie_json = json.load(f)
    return lottie_json

lottie_file= load_lottiefile(r'..\predic\Animation1.json')
st_lottie(
    lottie_file,
    speed=1, 
    reverse=False,
    loop=True,
    quality='medium',
    
    height=200,
    key=None

)

# Visualization Functions
def plot_distribution(column):
    plt.figure(figsize=(12, 6))
    if df[column].dtype == 'object':
        sns.countplot(x=column, data=df, palette='viridis')
        plt.title(f'Distribution of {column}')
    else:
        sns.histplot(df[column], bins=30, kde=True, color='skyblue')
        plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    st.pyplot(plt.gcf())

def plot_by_target(column, target_column='Lead_Outcome'):
    plt.figure(figsize=(12, 6))
    if df[column].dtype == 'object':
        sns.countplot(x=column, hue=target_column, data=df, palette='Set2')
        plt.title(f'{column} Distribution by {target_column}')
    else:
        sns.boxplot(x=target_column, y=column, data=df, palette='Set2')
        plt.title(f'{column} Distribution by {target_column}')
    plt.xlabel(column)
    plt.ylabel('Count' if df[column].dtype == 'object' else column)
    st.pyplot(plt.gcf())
    
    # Display the selected graph type
if plot_type == 'Distribution':
    plot_distribution(selected_column)
elif plot_type == 'By Target':
    plot_by_target(selected_column)


st.markdown("""
    <style>
    .custom-title {
        font-size: 50px;
        color:black;
        font-family:'Lato', sans-serif;
        text-align: center;
        font-weight: bold;
    }
    .custom-subtitle {
        font-size: 30px;
        color: #FF5733;
        font-family: Arial, sans-serif;
        font-weight: bold;

    }
    .custom-body {
        font-size: 20px;
        color: #FFFFFF;
        font-family: 'Georgia', serif;
    }
    </style>
    """, unsafe_allow_html=True)

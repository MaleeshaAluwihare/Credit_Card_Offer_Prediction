import streamlit as st
import pandas as pd
import json
import time
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from streamlit_lottie import st_lottie
import joblib
from io import BytesIO

# Load the trained model and dataset
loaded_model = joblib.load(r'TrainedModels\Logistic_Regression_model.pkl')
ds = pd.read_csv(r'Dataset\processed_training_data.csv')
df = pd.read_csv(r'Dataset\bank_customer.csv')
df = df.drop(['Unnamed: 0','ID', 'Region_Code'], axis=1)

# Function to load Lottie animation
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# Title
st.markdown('<div class="centered-title">Welcome to Smart Credit Card Marketing!</div>', unsafe_allow_html=True)

# animation
lottie_file= load_lottie_file(r'Styles\card3.json')
st_lottie(
                lottie_file,
                speed=0.1, 
                reverse=False,
                loop=True,
                quality='medium',
                
                height=200,
                key=None)

# st.markdown('<div class="centered-para"> In today\'s competitive banking industry, reaching the right customers is more important than ever. Our platform is designed to help banks optimize their credit card marketing strategy by leveraging the power of predictive analytics.</div>',unsafe_allow_html=True)
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

st.markdown('---')

st.markdown(f"<h3>Enter Customer Details Here..</h3>", unsafe_allow_html=True)

def load_lottiefile(filepath: str):
                with open(filepath) as f:
                    lottie_json = json.load(f)
                return lottie_json

lottie_file= load_lottiefile(r'Styles\form.json')
st_lottie(
                lottie_file,
                speed=0.3, 
                reverse=False,
                loop=True,
                quality='medium',
                
                height=200,
                key=None
            )

# Prediction function
def predict_lead_outcome(data):
    # encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    data_encoded = pd.get_dummies(data)
    all_columns = ds.drop('Lead_Outcome', axis=1).columns
    data_encoded = data_encoded.reindex(columns=all_columns, fill_value=0)
    prediction = loaded_model.predict(data_encoded)
    return ['Interest' if p == 1 else 'Not interest' for p in prediction]

#function to generate a download link
def generate_csv_download_link(dataset, filename='predicted_data.csv'):
    output = BytesIO()
    dataset.to_csv(output, index=False)
    output.seek(0)
    return st.download_button(
        label="Download Result",
        data=output,
        file_name=filename,
        mime='text/csv',
    )

# Form 
st.markdown('<div class="form-container">', unsafe_allow_html=True)
with st.form(key='lead_prediction_form'):
    
    # Form inputs
    gender = st.selectbox('Gender', ['Male', 'Female'])
    month_income = st.number_input('Month Income', min_value=0)
    age = st.number_input('Age', min_value=0)
    occupation = st.selectbox('Occupation', ['Other', 'Salaried', 'Self_Employed'])
    credit_score = st.number_input('Credit Score', min_value=0)
    loan_status = st.selectbox('Loan Status', ['Yes', 'No'])
    existing_credit_cards = st.number_input('Existing Credit Cards', min_value=0)
    avg_account_balance = st.number_input('Average Account Balance', min_value=0)
    account_category = st.selectbox('Account Category', ['Savings Account', 'Current Account', 'Senior Citizens Account', 'Investment Account'])
    tenure_with_bank = st.number_input('Tenure with Bank', min_value=0)
    
    # Submit button
    submit_button = st.form_submit_button(label='Predict', use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Prediction for individual form inputs
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
        lottie_animation = load_lottie_file(r'Styles\loading.json')
        st_lottie(lottie_animation, height=150, width=300)
        st.markdown('</div>', unsafe_allow_html=True)
        time.sleep(3)

    placeholder.empty() 

    
    # Display the prediction result
    prediction = predict_lead_outcome(input_data)

    
    if prediction == 'yes':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            lottie_animation = load_lottie_file(r'Styles\selected.json')
            st_lottie(lottie_animation, height=150, width=300)
        st.markdown('<div style="text-align: center; color: green; background-color: #d4edda; padding: 10px; border-radius: 5px;"><strong>Customer may show interest in a credit card offer</strong></div>', unsafe_allow_html=True)

    else:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            lottie_animation = load_lottie_file(r'Styles\rejected.json')
            st_lottie(lottie_animation, height=150, width=300)
        st.markdown('<div style="text-align: center; color: red; background-color: #f8d7da; padding: 10px; border-radius: 5px;"><strong>Customer may not show interest in a credit card offer</strong></div>', unsafe_allow_html=True)


# CSV Upload Section
st.markdown('---')
st.header('Batch Prediction for Dataset')

with st.expander("Click here to see dataset instructions"):
    st.markdown("""
    ### Instructions for Dataset Upload:
    - The dataset should be in **CSV format**.
    - The file must contain the following columns with appropriate data types:
    1. **ID**: Unique identifier for each customer (This will not be used in prediction but will appear in the output file).
    2. **Gender**: The gender of the customer (should be either 'Male' or 'Female').
    3. **Month_Income**: The monthly income of the customer (numeric value).
    4. **Age**: The age of the customer (numeric value).
    5. **Occupation**: The occupation of the customer (should be one of the following: 'Entrepreneur', 'Other', 'Salaried', 'Self_Employed').
    6. **Credit_Score**: The credit score of the customer (numeric value).
    7. **Loan_Status**: The loan status of the customer (should be either 'Yes' or 'No').
    8. **Existing_Credit_Cards**: The number of existing credit cards the customer has (numeric value).
    9. **Avg_Account_Balance**: The average account balance of the customer (numeric value).
    10. **Account_Category**: The account category of the customer (should be one of the following: 'Savings Account', 'Current Account', 'Senior Citizens Account', 'Investment Account').
    11. **Tenure_with_Bank**: The number of years the customer has been with the bank (numeric value).

    - Make sure the dataset follows the above structure and the column names match exactly.
    - The **ID** column will be used to identify customers in the results and will not be part of the prediction inputs.
    - The **Lead_Outcome** will be predicted and added to the dataset after processing.
    """)

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    user_data = pd.read_csv(uploaded_file)

    # Check if 'User_ID' column exists
    if 'ID' not in user_data.columns:
        st.error("The dataset must contain a 'ID' column.")
    else:
        # remove 'User_ID' from prediction
        input_data = user_data.drop(columns=['ID'])
        
        # Loading animation
        placeholder = st.empty()
        with placeholder.container():
            st.markdown('<div class="centered-container">', unsafe_allow_html=True)
            lottie_animation = load_lottie_file(r'Styles\loading.json')
            st_lottie(lottie_animation, height=150, width=300)
            st.markdown('</div>', unsafe_allow_html=True)
            time.sleep(3)
        
        placeholder.empty()

        # Predict for the uploaded dataset
        user_data['Lead_Outcome'] = predict_lead_outcome(input_data)

        # Display the dataset with the predictions
        st.write(user_data[['ID', 'Lead_Outcome']])

        # Provide option to download the results
        generate_csv_download_link(user_data[['ID', 'Lead_Outcome']])


st.write("\n\n\n\n\n\n\n\n\n\n\n\n")
st.markdown('---')

#Data visualization
st.markdown('<div class="centered-para"><u>Data Visualizations</u></div>', unsafe_allow_html=True)

def load_lottiefile(filepath: str):
    with open(filepath) as f:
        lottie_json = json.load(f)
    return lottie_json

lottie_file= load_lottiefile(r'Styles\Animation1.json')
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
    .centered-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .centered-para{
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
   }
    </style>
    """, unsafe_allow_html=True)

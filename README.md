
---

# Customer Salary Prediction

## Project Overview
This project aims to predict a customer's salary based on demographic and lifestyle information. By analyzing features such as age, education level, job type, marital status, and others, we develop a machine learning model to predict the annual income of individuals. This project can be useful for financial institutions to optimize financial product offerings (e.g., loans, credit cards) based on a customer's predicted income.

## Business Problem
Financial institutions and companies often need to understand the income levels of their customers to provide relevant products and services. However, directly asking for salary information is not always feasible. In this project, we solve the problem of predicting salary from available customer data, enabling businesses to:
- Customize product offerings based on income.
- Improve customer experience with personalized offers.
- Reduce financial risk by targeting offers to customers with the appropriate income level.

## Dataset
The dataset used for this project contains 10,108 customer records with the following features:
- **Customer_Age**: Age of the customer.
- **Gender**: Gender of the customer.
- **Dependent_Count**: Number of dependents.
- **Education_Level**: Highest level of education attained.
- **Marital_Status**: Customer's marital status.
- **state_cd**: State code where the customer resides.
- **Zipcode**: Residential zip code.
- **Car_Owner**: Indicates if the customer owns a car.
- **House_Owner**: Indicates if the customer owns a house.
- **Personal_Loan**: Whether the customer has taken a personal loan.
- **contact**: Contact type with the customer (e.g., cellular, unknown).
- **Customer_Job**: Job type of the customer.
- **Income**: Annual income of the customer (target variable).
- **Cust_Satisfaction_Score**: A score indicating the customer’s satisfaction level.

## Key Features
- **Data Preprocessing**: Handling missing data, encoding categorical variables, and feature scaling.
- **Exploratory Data Analysis (EDA)**: Understanding the relationship between features and income.
- **Modeling**: Several regression models are trained, evaluated, and compared to predict customer income.
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting Regressor
  - Linear Regression
- **Model Evaluation**: Evaluating the model performance using metrics such as:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - R-squared (R²)

## Installation and Usage
To use this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/MaleeshaAluwihare/Customer_Salary_Prediction.git
    cd Customer_Salary_Prediction
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Jupyter notebook or Python script to train the model:
    ```bash
    jupyter notebook
    ```
   or
   ```bash
    python salary_prediction.py
    ```


## Results
The best-performing model was **[model_name]**, which achieved an R² score of **[score]** on the test set, indicating that the model explains a significant portion of the variance in customer salaries.

## Conclusion
By accurately predicting customer salaries, businesses can make data-driven decisions to personalize product offerings and better serve their customer base. This project demonstrates the potential of machine learning to solve practical business problems in financial services.

## Future Improvements
- Feature engineering to improve model performance.
- Testing with different machine learning algorithms.
- Deployment of the model as an API for real-time prediction.


---

# Customer Churn Prediction using Logistic Regression

## Project Overview
This project focuses on predicting customer churn using a Logistic Regression model. The goal is to identify customers who are likely to leave a service or business based on historical customer data.

The project covers the complete machine learning workflow including:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Building
- Model Evaluation

---

## Problem Statement
Customer churn is one of the major challenges faced by businesses. Retaining existing customers is often more cost-effective than acquiring new ones.

The objective of this project is to build a predictive model that helps identify customers who are likely to churn, enabling businesses to take proactive retention measures.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Workflow

### 1. Data Preprocessing
- Handled missing values
- Encoded categorical variables
- Performed feature selection

### 2. Exploratory Data Analysis (EDA)
- Analyzed customer behavior patterns
- Identified relationships between features and churn

### 3. Model Building
- Implemented Logistic Regression for binary classification
- Split data into training and testing sets

### 4. Model Evaluation
Evaluated the model using:
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

## Key Insights
- Certain customer attributes showed strong correlation with churn behavior.
- Logistic Regression provided an interpretable baseline model for churn prediction.
- Feature importance helped understand key churn drivers.

---

## Future Improvements
- Try advanced models such as Random Forest, XGBoost, and Gradient Boosting
- Perform hyperparameter tuning
- Handle class imbalance using SMOTE or class weights
- Deploy model using Flask or Streamlit

---

## Project Structure



├── data/
├── notebooks/
├── src/
├── models/
├── README.md
└── requirements.txt

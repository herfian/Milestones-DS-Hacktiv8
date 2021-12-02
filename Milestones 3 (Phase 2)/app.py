import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

st.title('HERFIAN MODEL DEPLOYMENT')
st.write("""
         Telco Customer Churn
         
         Context :
         Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs.
         
         Source : https://www.kaggle.com/blastchar/telco-customer-churn
         """)

@st.cache
def fetch_data():
    df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
    return df

df =  fetch_data()
st.write(df)

st.sidebar.header('User Input Features')
def user_input(data):
    gender = st.sidebar.selectbox('Gender', data['gender'].unique())
    SeniorCitizen = st.sidebar.selectbox('Senior Citizen', ['0','1'])
    Partner = st.sidebar.selectbox('Partner', ['Yes','No'])
    Dependents = st.sidebar.selectbox('Dependents', ['Yes','No'])
    tenure = st.sidebar.number_input('tenure', value=0)
    PhoneService = st.sidebar.selectbox('Phone Service', ['Yes','No'])
    MultipleLines = st.sidebar.selectbox('Multiple Lines', data['MultipleLines'].unique())
    InternetService = st.sidebar.selectbox('InternetService', data['InternetService'].unique())
    OnlineSecurity = st.sidebar.selectbox('Online Security', data['OnlineSecurity'].unique())
    OnlineBackup = st.sidebar.selectbox('Online Backup', data['OnlineBackup'].unique())
    DeviceProtection = st.sidebar.selectbox('Device Protection', data['DeviceProtection'].unique())
    TechSupport = st.sidebar.selectbox('Tech Support', data['TechSupport'].unique())
    StreamingTV = st.sidebar.selectbox('Streaming TV', data['StreamingTV'].unique())
    StreamingMovies = st.sidebar.selectbox('Streaming Movies', data['StreamingMovies'].unique())
    Contract = st.sidebar.selectbox('Contract', data['Contract'].unique())
    PaperlessBilling = st.sidebar.selectbox('Paperless Billing', data['PaperlessBilling'].unique())
    PaymentMethod = st.sidebar.selectbox('Payment Method', data['PaymentMethod'].unique())
    MonthlyCharges  = st.sidebar.number_input('MonthlyCharges ', value=0)
    TotalCharges = st.sidebar.number_input('Total Charges ', value=0)
    
    data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,
    }
    features = pd.DataFrame(data, index=[0])
    return features

input = user_input()

st.write('User Input')
st.write(input)

best_model = keras.models.load('ridcv_model_ANNfunc.h5')
prediction = best_model.predict(input)

st.write('Based on user input, Churn predicted:')
st.write(prediction)
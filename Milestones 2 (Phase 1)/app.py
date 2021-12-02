import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title('HERFIAN MODEL DEPLOYMENT')
st.write("""
         Challenger Ranked Games League of Legends
         """)

@st.cache
def fetch_data():
    df = pd.read_csv('Challenger_Ranked_Games.csv')
    return df

df =  fetch_data()
st.write(df)

st.sidebar.header('User Input Features')

def user_input():
    blueFirstBlood = st.sidebar.number_input('First Blood', value=0)
    blueFirstTower = st.sidebar.number_input('First Tower', value=0)
    blueFirstBaron = st.sidebar.number_input('First Baron ', value=0)
    blueFirstDragon = st.sidebar.number_input('First Dragon', value=0)
    blueFirstInhibitor = st.sidebar.number_input('First Inhibitor', value=0)
    blueDragonKills = st.sidebar.number_input('DragonKills', value=0)
    blueBaronKills = st.sidebar.number_input('Baron Kills', value=0)
    blueTowerKills = st.sidebar.number_input('Tower Kills', value=0)

    data = {
        'blueFirstBlood': blueFirstBlood,
        'blueFirstTower': blueFirstTower,
        'blueFirstBaron': blueFirstBaron,
        'blueFirstDragon': blueFirstDragon,
        'blueFirstInhibitor': blueFirstInhibitor,
        'blueDragonKills': blueDragonKills,
        'blueBaronKills': blueBaronKills,
        'blueTowerKills': blueTowerKills,
    }
    features = pd.DataFrame(data, index=[0])
    return features

input = user_input()

st.write('User Input')
st.write(input)

load_model = joblib.load('RandomForest_model')
prediction = load_model.predict(input)

st.write('Based on user input, league of legends predicted:')
st.write(prediction)
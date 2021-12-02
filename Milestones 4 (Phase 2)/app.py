import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import pandas as pd

from tensorflow import keras


st.title('HERFIAN MODEL DEPLOYMENT')
st.write("""
         73 Sports Image Classification
         
         Context :
         Collection of sports images covering 73 different sports. Images are 224,224,3 jpg format. Data is separated into train, test and valid directories. Additional a csv file is includes for those that wish to use it to create there own train, test and validation datasets.
         
         Source : https://www.kaggle.com/gpiosenka/sports-classification
         """)

@st.cache
def fetch_data():
    df = pd.read_csv('class_dict.csv')
    return df

df =  fetch_data()
st.write(df)

st.title("SPORTS IMAGE CLASSIFICATIOn")

@st.cache(allow_output_mutation=True)
def teachable_machine_classification(img, weights_file):
    # Load the model
    model = keras.models.load_model(weights_file)

    size = (15, 15)
    image = ImageOps.fit(img, size)
    image = np.asarray(image)

    img_reshape = image[np.newaxis, ...]

    # run the inference
    predictions = model.predict(img_reshape)
    predictions = tf.nn.sigmoid(predictions)
    predictions = tf.where(predictions < 0.5, 0, 1)

    return  predictions

st.sidebar.header("Please input an image to be classified:")
uploaded_file = st.sidebar.file_uploader("Choose Image : ", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded file', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, 'model_base_MobileNetV2.h5')
    if label == 1:
        st.write("Its a ")
    else:
        st.write("Its a ")
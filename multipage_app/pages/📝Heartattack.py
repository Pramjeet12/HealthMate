import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

def load_model():
    with open("Heart_model_pickle", "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()

st.title("Heart attack Prediction💔")

st.write("""### We need some information to predict the heart attack.""")

age = st.number_input("Age ",0,150)
gender = st.number_input("Gender(0 for Female, 1 for Male)",0,1)
impluse = st.number_input("Impluse",0,1200)
pressurehight = st.number_input("Pressurehight",0,250)
pressurelow = st.number_input("Pressurelow",0,200)
glucose = st.number_input("Glucose ",0.0,600.0)
kcm = st.number_input("kcm",0.00,350.00)
troponin = st.number_input("Troponin ",0.000,10.000)

ok = st.button("Predict Heart attack")
if ok:
    input_data = (age, gender, impluse, pressurehight, pressurelow, glucose, kcm, troponin)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = data.predict(input_data_reshaped)
    if prediction == 0:
        st.subheader("The person does not have Heart attack problem.")
    else:
        st.subheader("The person has Heart attack problem.")

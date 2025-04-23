import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("Diabetes_model_pickle", "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()




st.title("Diabetes Prediction🍬")

st.write("""### We need some information to predict the diabetes.""")

Pregnancies = st.number_input("Pregnancies ",0,50)
Glucose = st.number_input("Glucose",0,500)
BloodPressure = st.number_input("BloodPressure",0,200)
SkinThickness = st.number_input("SkinThickness",0,200)
Insulin = st.number_input("Insulin",0,1000)
BMI = st.number_input("BMI ",0.0,105.0)
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction",0.000,5.000)
Age = st.number_input("Age ",0,150)

ok = st.button("Predict Diabetes")
if ok:
    input_data = (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    diabetes = data.predict(input_data_reshaped)

    if diabetes == 1:
        st.subheader("The person has Diabetes.")
    else:
        st.subheader("The person has no Diabetes.")



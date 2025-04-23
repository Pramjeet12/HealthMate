import streamlit as st
import numpy as np
import pickle

def load_model():
    with open("Lung_cancer_model_pickle", "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()

st.title("Lung cancer Prediction🫁")

st.write("""### We need some information to predict the lung cancer.""")

gender = st.number_input("Gender(0 for Female, 1 for Male)",0,1)
age = st.number_input("Age ",0,200)
smoking = st.number_input("Smoking(1 for No, 2 for Yes)",1,2)
yellow_fingers = st.number_input("Yellow Fingers(1 for No, 2 for Yes)",1,2)
anxiety = st.number_input("Anxiety(1 for No, 2 for Yes)",1,2)
peer_pressure = st.number_input("Peer Pressure(1 for No, 2 for Yes)",1,2)
chronic_Disease = st.number_input("Chronic Disease(1 for No, 2 for Yes)",1,2)
fatigue = st.number_input("Fatigue(1 for No, 2 for Yes)",1,2)
allergy = st.number_input("Allergy(1 for No, 2 for Yes)",1,2)
wheezing = st.number_input("Wheezing(1 for No, 2 for Yes)",1,2)
alcohol = st.number_input("Alcohol(1 for No, 2 for Yes)",1,2)
coughing = st.number_input("Coughing(1 for No, 2 for Yes)",1,2)
shortness_of_Breath = st.number_input("Shortness of Breath(1 for No, 2 for Yes)",1,2)
swallowing_Difficulty = st.number_input("Swallowing Difficulty(1 for No, 2 for Yes)",1,2)
chest_pain = st.number_input("Chest pain(1 for No, 2 for Yes)",1,2)

ok = st.button("Predict Lung cancer")
if ok:
    input_data = (gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_Disease, fatigue, allergy, wheezing, alcohol, coughing, shortness_of_Breath, swallowing_Difficulty, chest_pain)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = data.predict(input_data_reshaped)
    if prediction == [0]:
        st.subheader("The person does not have Lung Cancer.")
    else:
        st.subheader("The person have Lung Cancer.")



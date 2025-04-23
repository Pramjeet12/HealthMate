import streamlit as st
import os
import tensorflow as tf
from keras.models import load_model
import librosa
import numpy as np


def load_model():
    model=tf.keras.models.load_model("Heartbeat_audioclassification.keras")
    return model

model=load_model()

st.title("Heartbeat Classifier🫀")
st.subheader("(Heart conditions detection.)")

# File uploader
file = st.file_uploader("Choose an audio file for classification...", type=["wav", "mp3", "m4a"])
ok = st.button("Predict Heart conditions")
if ok:
   y, sr = librosa.load(file, duration=3, offset=0.5)
   mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
   mfcc=mfcc.reshape(1,-1)
   predicted_label=np.argmax(model.predict(mfcc), axis=-1)
   if predicted_label == [0]:
        st.subheader("Artifact")
   elif predicted_label == [1]:
        st.subheader("Aunlabelledtest")
   elif predicted_label == [2]:
        st.subheader("Bunlabelledtest")
   elif predicted_label == [3]:
        st.subheader("Extrahls")
   elif predicted_label == [4]:
       st.subheader("Extrastole")
   elif predicted_label == [5]:
        st.subheader("Murmur")
   elif predicted_label == [6]:
       st.subheader("Normal")
   else:
       st.subheader("Unlabelledtest")

st.markdown("---")  # Adds a horizontal line
if st.button("About the Developer"):
    st.write("Created by: 👨‍💻Kumar")  # Replace with your name


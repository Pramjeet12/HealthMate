import streamlit as st
import os
import tensorflow as tf
from keras.models import load_model
import librosa
import numpy as np


def load_model():
    model=tf.keras.models.load_model("Asthma_audioclassification.keras")
    return model

model=load_model()

st.title("Asthma Detection💨")
st.subheader("(Lung conditions detection.)")

# File uploader
file = st.file_uploader("Choose an audio file for classification...", type=["wav", "mp3", "m4a"])
ok = st.button("Predict lung conditions")
if ok:
   y, sr = librosa.load(file, duration=3, offset=0.5)
   mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
   mfcc=mfcc.reshape(1,-1)
   predicted_label=np.argmax(model.predict(mfcc), axis=-1)
   if predicted_label == [0]:
        st.subheader("Asthma")
   elif predicted_label == [1]:
        st.subheader("Bronchial")
   elif predicted_label == [2]:
        st.subheader("Copd")
   elif predicted_label == [3]:
        st.subheader("Healthy")
   else:
       st.subheader("Pneumonia")


import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
st.title("Welcome to HealthMate🩺.")
st.sidebar.success("Select a page above.")
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_factory = load_lottieurl("https://lottie.host/d5e67235-ae5c-427b-937d-d4ba6c9c9589/XQug5dpK0s.json")
st_lottie(lottie_factory, key="factory")


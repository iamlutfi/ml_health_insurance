import streamlit as st
import pandas as pd
import joblib

from utils.validate import validate_input
from utils.preprocessing import transform

# config page
st.set_page_config(page_title='Health Insurance Predictor', page_icon='💰')

# laod model
# used cache so model will be load at the first user log
@st.cache_resource
def load_model():
    return joblib.load('../model/final_model_xgboost.pkl')
model = load_model

st.title('Health Insurance Predictor')
st.markdown('Select an input method below to make a prediction.')

method = st.radio('Input Methods:', ['Manual Input', 'Upload file .csv'], horizontal=True)
input_df = None

if method == 'Manual Input':
    with st.container(border=True):
        st.subheader('Data Form')
        

import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load("Dream_House_Price.joblib")

st.title("HOUSE PRICE PREDICTION APP")
st.write("Enter The House Area(in square feet)To Predict The Price")
area = st.number_input("Enter Area(sqft):",min_value=500, max_value=10000,step=100)

if st.button("Predict Price"):
    input_data = pd.DataFrame([[area]], columns=['area'])
    prediction = model.predict(input_data)
    st.success(f"Predict Price:${np.round(prediction[0],2)}")

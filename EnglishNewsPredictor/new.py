import streamlit as st
import joblib 
st.title("🔥News Category Prediction")
input_text = st.text_area("Enter the news you want to predict")

model = joblib.load("new_category_prediction.joblib")
if st.button("PREDICT"):
    output = model.predict([input_text])
    st.success(output[0])
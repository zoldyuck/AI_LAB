import streamlit as st
import joblib 
st.header("🔥 NEPALI NEWS CATEGORY PREDICTOR 🔥")
input_text = st.text_area("Enter the news you want to predict")

model = joblib.load("nepali_news_category_predictor.joblib")
if st.button("PREDICT"):
    output = model.predict([input_text])
    st.success(f"Predicted Category: {output[0]}")
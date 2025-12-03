import streamlit as st
import joblib
import os

MODEL_PATH = os.path.join("models", "netflix_genre_model.joblib")
ENCODER_PATH = os.path.join("models", "label_encoder.joblib")

model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)

st.title(" Netflix Genre Prediction App")
st.write("Enter details of a show/movie and I’ll predict its primary genre.")

title = st.text_input("Title")
description = st.text_area("Description")
cast = st.text_input("Cast (comma separated)")
director = st.text_input("Director")
country = st.text_input("Country")

if st.button("Predict Genre"):
    combined_text = " ".join([title, description, cast, director, country])
    
    pred_label = model.predict([combined_text])[0]
    pred_genre = label_encoder.inverse_transform([pred_label])[0]
    
    st.subheader(f"Predicted Genre: **{pred_genre}**")

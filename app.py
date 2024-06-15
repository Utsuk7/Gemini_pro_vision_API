from dotenv import load_dotenv
load_dotenv()

from PIL import Image
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(inpu,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title="FASHION RECOMMENDATION")

st.header("Know Your Fashion")
input=st.text_input("Input Prompt: ",key="input")

uploaded_file=st.file_uploader("Choose your dress combination ..", type=['jpeg','jpg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image", use_column_width=True)

submit=st.button("Recommend me the fashion")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("Recommendation is...")
    st.write(response)
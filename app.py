from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

#loading the environment variables:
load_dotenv()

#configure the genai key:
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#creating a fucntion to load the gemini-pro-vision model:
model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)

    return response.text

#creating the UI using streamlit:
st.set_page_config(page_title="Gemini Image Description")
st.header("Image Description")

#taking the input from the user
input = st.text_input("Input Prompt: ",key="input") 

#creating an image uploader:
uploaded_file = st.file_uploader("Choose and image:", type=["jpg","jpeg","png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image")

#creating the submit button:
submit = st.button("Submit")

if submit:
    response = get_gemini_response(input,image)
    st.write(response)
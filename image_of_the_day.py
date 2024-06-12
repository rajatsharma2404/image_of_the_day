import os
import requests
import streamlit as st

#Get Content using URL and API_KEY
apod_key = os.getenv("IMAGE_API_KEY")
apod_url = f"https://api.nasa.gov/planetary/apod?api_key={apod_key}"
response = requests.get(apod_url)
content = response.json()


#Save Image using url in content
image_url = content['hdurl']
img_response = requests.get(image_url)
with open("apod.jpg", "wb") as file:
    file.write(img_response.content)


#Create interface showing image and its details
st.set_page_config(layout="wide")
centered_title = f'<h1 style="text-align: center;">Astronomy Image of the Day </h1>'
st.markdown(centered_title, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,10,1])
with col2:
    st.image(image="apod.jpg", caption="Astronomy Image of the Day")
detail = content['explanation']
st.write(f"## {detail}")






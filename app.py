import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from PIL import Image

# Set page config
st.set_page_config(page_title="FlowerClassifier", page_icon="🌸")

# Path to your saved model (local path or URL)
model_path = './workspace/cnn/data/Model.h5'

# Load the model
saved_model = load_model(model_path)

# App title
st.title("Flower Classification")

# Description
st.markdown("""
Flower classification involves identifying the species or category of a flower from an image.
This task is complex due to the vast diversity of flower species, varying environmental conditions,
and different angles from which photos can be taken. Convolutional Neural Networks (CNNs) are a popular
choice for this task due to their ability to automatically learn features from images.
""")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=False)
    st.write("Image Uploaded Successfully!")

    if st.button('Click to Predict'):
        # Class list
        class_names = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

        # Preprocess the uploaded image
        test_image = img.resize((224, 224))  # Resize to model input size
        test_image = img_to_array(test_image)

import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image

# Load the trained model
model = load_model('model.h5')

# Define image size and number of channels (as used in training)
IMAGE_SIZE = 128  # Replace with actual size used in your model
CHANNELS = 3  # 3 for RGB images

# Define class names if available
class_names = ['yawn', 'no_yawn', 'closed', 'open']  # Replace with actual class names

st.title("Driver Drowsiness Predictor")

st.write("""
Upload an image, and the model will predict its class.
""")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Preprocess the image for the model
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    image_array = img_to_array(image) / 255.0  # Normalize the image
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Make a prediction
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions[0])

    # Show results
    st.write(f"Predicted Class: {class_names[predicted_class]}")
    st.write(f"Confidence: {np.max(predictions[0]) * 100:.2f}%")

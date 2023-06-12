import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

from tensorflow import keras

# Load the model architecture from the JSON file
with open('fakevsreal_model.json', 'r') as json_file:
    model_json = json_file.read()
model = keras.models.model_from_json(model_json)

# Load the model weights from the saved file
model.load_weights('fakevsreal_weights.h5')

# Define the labels
labels = ['Real', 'Fake']

def classify_image(file_path):
    image = Image.open(file_path) # reading the image
    image = image.resize((128, 128)) # resizing the image to fit the trained model
    image = image.convert("RGB") # converting the image to RGB
    img = np.asarray(image) # converting it to numpy array
    img = np.expand_dims(img, 0)
    predictions = model.predict(img) # predicting the label
    label = labels[np.argmax(predictions[0])] # extracting the label with maximum probability
    probab = float(round(predictions[0][np.argmax(predictions[0])] * 100, 2))

    result = {
        'label': label,
        'probability': probab
    }

    return result

# Streamlit app code
st.title('Fake vs Real Image Classifier')

uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    result = classify_image(uploaded_file)

    st.write('Prediction:', result['label'])
    st.write('Probability:', result['probability'], '%')

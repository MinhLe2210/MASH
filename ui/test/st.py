import streamlit as st
import torch
from pathlib import Path
import joblib

st.title("TEST MODEL")

# Get model
model_file = st.file_uploader('Upload your model', type=['h5', 'pkl', 'joblib', 'pickle', 'pt', 'pth'])
# print type model_file

if model_file is not None:
    model_content = model_file.getvalue()  # Read the contents of the uploaded file
    with open('minh_model.pt', 'wb') as f:
        f.write(model_content)
    st.success('Model loaded successfully!')

    # # Load model
    # model = torch.load(model_path)
    # print(f'Model loaded from {model_path}')

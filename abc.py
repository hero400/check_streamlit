import numpy as np
from flask import Flask, request, make_response
import json
import pickle
from flask_cors import cross_origin
import logging
import streamlit as st
z=True
def load_image():
    uploaded_file = st.file_uploader(label='Pick an image to test')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
app = Flask(__name__)        
@app.route('/dog')
def hello():
    global z
    if z:
        z=False
        print("ok")
        st.title(z)
    else:
        z=True
        return st.title(z)        
def main():
    st.title('Image upload demo')
    app = Flask(__name__)
    #load_image()
    hello()
    
    #model = pickle.load(open('rf.pkl', 'rb'))
if __name__ == '__main__':
    main()
import streamlit as st
import numpy as np
import pickle


st.title('Laptop Price Prediction')
with open('MODEL.pkl', 'rb') as file:
    model = pickle.load(file)
file.close()

# Input 
operating_system = st.number_input("operating_system")
RAM_nth = st.number_input("RAM_nth")
storage_nth = st.number_input("storage_nth")
storage_type = st.number_input("storage_type")
cpu_benchmark = st.number_input("cpu_benchmark")
gpu_class = st.number_input("gpu_class")
screen_size = st.number_input("screen_size")
PPI = st.number_input("PPI")
warranty= st.number_input("warranty")    

if st.button('Predict'):
    x = np.array([[operating_system, RAM_nth, storage_nth, storage_type,
       cpu_benchmark, gpu_class, screen_size, PPI, warranty]])
    Y_predict = model.predict(x)
    st.success('Predicted price is{}'.format(Y_predict))
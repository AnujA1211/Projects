import numpy as np
import pickle
import streamlit as st


st.markdown('<style>h1{color: #0066cc;}</style>', unsafe_allow_html=True)

with open('MODEL1.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Drug Classification")
st.image("drugs.jpg", use_column_width=True)

Age = st.slider("Age", min_value=0, max_value=100, step=1)
sex = st.selectbox("Sex", ['F', 'M'])
bp = st.selectbox("Blood Pressure", ['LOW', 'NORMAL', 'HIGH'])
cholesterol = st.selectbox("Cholesterol", ['NORMAL', 'HIGH'])
Na_to_K = st.number_input('Na_to_K')


# Convert categorical variables to numerical values
Sex_mapping = {'F': 0, 'M': 1}
Sex = Sex_mapping.get(sex)

BP_mapping = {'LOW': 0, 'NORMAL': 1, 'HIGH' :2}
BP = BP_mapping.get(bp)

Cholesterol_mapping = {'NORMAL': 0, 'HIGH' :1}
Cholesterol = Cholesterol_mapping.get(cholesterol)

# Predict when the button is clicked
if st.button('Predict'):
    x = np.array([[Age,Sex,BP,Cholesterol,Na_to_K]])
    y_predict = model.predict(x)
    y_predict = y_predict.tolist()[0]
    Y_predict =  y_predict.index(1)
    if Y_predict == 0:
        st.success('Prediction is: DrugA')
    elif Y_predict == 1:
        st.success('Prediction is: DrugB')
    elif Y_predict == 2:
        st.success('Prediction is: DrugC')
    elif Y_predict == 3:
        st.success('Prediction is: DrugX')
    elif Y_predict == 4:
        st.success('Prediction is: DrugY')

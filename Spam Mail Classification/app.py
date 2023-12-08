import streamlit as st
import pickle

# Load the trained model and TfidfVectorizer
with open('model_file', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer_file', 'rb') as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)

st.title("Spam Email Classification")

# Create a text input box for user input
user_input = st.text_area("Enter an email message")

if st.button("Classify"):
    # Transform user input using the TfidfVectorizer
    input_tfidf = tfidf_vectorizer.transform([user_input])

    # Make a prediction
    prediction = model.predict(input_tfidf)

    # Display the result
    if prediction[0] == 0:
        st.write("This email is spam.")
    else:
        st.write("This email is Ham.")
import streamlit as st
from intent_classifier import classify_intent

st.title("BotTrainer NLU Demo")

user_input = st.text_input("Enter your message:")

if user_input:
    result = classify_intent(user_input)

    st.write("**Predicted Intent:**", result.get("intent"))
    st.write("**Confidence:**", result.get("confidence"))

    st.write("**Entities:**")
    st.json(result.get("entities"))

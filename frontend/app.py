import streamlit as st
import requests

st.title("🛍️ Shopify Support Bot")

user_input = st.text_input("You:", key="user_input")

if user_input:
    res = requests.post("http://localhost:8000/shopify/shopify-chat", json={
        "customer_id": "12345",
        "question": user_input
    })

    bot_reply = res.json().get("reply")

    st.markdown(f"**Bot:** {bot_reply}")

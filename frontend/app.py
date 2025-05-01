import streamlit as st
import requests

st.title("🛍️ Shopify Chatbot Assistant")

customer_id = st.text_input("Enter Customer ID 👤")
question = st.text_input("Ask something... 🤖")

if st.button("Ask") and customer_id and question:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "http://localhost:8000/shopify/shopify-chat",
                json={
                    "customer_id": customer_id,
                    "question": question
                }
            )
            data = response.json()

            # 🔍 DEBUGGING LINE
            st.write("🧪 Response from backend:", data)

            # ✅ SAFELY try to access reply
            if "reply" in data:
                st.success("✅ Assistant replied:")
                st.write(data["reply"])
            else:
                st.error("❌ 'reply' key not found in backend response.")
        except Exception as e:
            st.error(f"Something went wrong 😢: {e}")

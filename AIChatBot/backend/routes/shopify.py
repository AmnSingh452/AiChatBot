from fastapi import APIRouter
from pydantic import BaseModel
import openai # assuming you have OpenAI client configured in config.py
# <-- Import logic here

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from routes.shopify_api import get_order_info
router = APIRouter()
from routes.shopify_api import get_order_info

# Fetch order info with error handling
@router.get("/order/{order_id}")
async def fetch_order(order_id: str):
    try:
        return get_order_info(order_id)
    except Exception as e:
        return {"error": f"Failed to fetch order info: {str(e)}"}

# Temporary in-memory storage for chat history
chat_history = {}

# Define the request structure for chat
class ChatRequest(BaseModel):
    customer_id: str
    question: str

# Toggle GPT use
USE_GPT = True  # Switch this to True when you have OpenAI API access

@router.post("/shopify-chat")
async def shopify_chat(req: ChatRequest):
    customer_id = req.customer_id
    question = req.question

    # Fetch previous messages for that user
    history = chat_history.get(customer_id, [])
    history.append({"role": "user", "content": question})

    if USE_GPT:
        try:
            # Compose the full chat log
            messages = [{"role": "system", "content": "You are a friendly and professional Shopify customer support assistant. Answer users’ questions in a clear, polite, and concise manner. If they ask about orders, products, shipping, or refunds, guide them with relevant info or politely redirect if unavailable."}] + history

            response = openai.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages
            )
            print(response)
            reply = response.choices[0].message.content
            
            
        except Exception as e:
            reply = "Sorry, I encountered an issue while processing your request. Please try again later."
            print(f"Error with OpenAI API: {str(e)}")
    else:
        # Simulated response if GPT is off
        reply = f"(Simulated GPT) You asked: '{question}'. I'm your Shopify assistant 🤖"

    # Save bot response in memory
    history.append({"role": "assistant", "content": reply})
    chat_history[customer_id] = history

    return {"reply": reply}
    

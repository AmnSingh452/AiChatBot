import sys
import os
from fastapi import FastAPI

# Add root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes import chatbot, shopify

app = FastAPI()

# Register routes
app.include_router(chatbot.router, prefix="/chatbot")
app.include_router(shopify.router, prefix="/shopify")

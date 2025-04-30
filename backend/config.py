# config.py

import os
from dotenv import load_dotenv
import openai

# Load .env file
load_dotenv()

# Get your keys
shopify_token = os.getenv("SHOPIFY_ACCESS_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")

# Validate them
if not shopify_token:
    raise ValueError("❌ SHOPIFY_ACCESS_TOKEN is not set.")
if not openai_key:
    raise ValueError("❌ OPENAI_API_KEY is not set.")

# Set the OpenAI API key globally (v1+ way)
openai.api_key = openai_key

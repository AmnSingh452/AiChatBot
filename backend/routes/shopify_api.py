import os
import requests
from dotenv import load_dotenv

# Load env variables from .env
load_dotenv()

# Fetch environment variables correctly
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")  # Use the name of the variable from .env
SHOPIFY_STORE_DOMAIN = os.getenv("SHOPIFY_STORE_DOMAIN")  # Use the name of the variable from .env

def get_order_info(order_id: str):
    url = f"https://{SHOPIFY_STORE_DOMAIN}/admin/api/2023-10/orders/{order_id}.json"
    headers = {
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["order"]
        return {
            "order_id": data["id"],
            "status": data.get("fulfillment_status", "Unfulfilled"),
            "total": data["total_price"],
            "customer_name": data["customer"]["first_name"]
        }
    else:
        return {"error": f"Failed to fetch order. Status code: {response.status_code}"}

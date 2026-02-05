import requests
import os
from dotenv import load_dotenv
import logging

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

#print("API KEY:", API_KEY)   # Quick test line

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR
)

def ask_deepseek(messages):

    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "DeepSeek Chat App"
        }

        data = {
            "model": "deepseek/deepseek-chat",
            "messages": messages
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=15
        )

        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "⚠ API Timeout"

    except Exception as e:
        logging.error(str(e))
        print("ERROR:", e)
        return "⚠ Error contacting OpenRouter API"

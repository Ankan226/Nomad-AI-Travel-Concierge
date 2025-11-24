import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: API Key not found in .env file")
else:
    genai.configure(api_key=api_key)
    print("Fetching available models...")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"VALID MODEL: {m.name}")
    except Exception as e:
        print(f"Error listing models: {e}")
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class Agent:
    def __init__(self, name, role, instructions):
        self.name = name
        self.role = role
        self.instructions = instructions
        
        # CHANGED: Using "gemini-2.0-flash" which is explicitly in your list
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate_response(self, prompt):
        full_prompt = f"""
        You are {self.name}, a {self.role}.
        Your core instructions: {self.instructions}
        
        Task: {prompt}
        """
        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {e}"
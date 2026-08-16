import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model=genai.GenerativeModel("gemini-3.5-flash")

def generate_ai_response(prompt):
    response=model.generate_content(prompt)
    return response.text
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load env
load_dotenv()

# Correct way
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")

def analyze_resume(resume, job_description):
    
"""
    response = model.generate_content(prompt)
    return response.text
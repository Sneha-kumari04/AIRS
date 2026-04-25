import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load env
load_dotenv()

# Correct way
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")

def analyze_resume(resume, job):
    prompt = f"""
You are an AI resume screening system.

Analyze the resume vs job description and return STRICTLY in this format:

Match Score: XX%

Strengths:
- point 1
- point 2

Missing Skills:
- point 1
- point 2

Suggestions:
- point 1
- point 2

Resume:
{resume}

Job: 
{job}

"""
    response = model.generate_content(prompt)
    return response.text
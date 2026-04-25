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
    prompt = f"""
You are an AI resume screening system.

Analyze the resume against the job description and provide:

1. Match Score (in percentage)
2. Key Strengths
3. Missing Skills
4. Improvement Suggestions

Resume:
{resume}

Job Description:
{job_description}
"""
    response = model.generate_content(prompt)
    return response.text
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Initialize model
model = genai.GenerativeModel("gemini-pro")


def analyze_resume(resume, job_description):

    prompt = f"""
You are an AI resume screening system.

Analyze the resume against the job description and provide:

1. Match Score (in percentage)
2. Key Strengths
3. Missing Skills
4. Improvement Suggestions

Keep the response clear, concise, and well-structured.

Resume:
{resume}

Job Description:
{job_description}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating response: {str(e)}"
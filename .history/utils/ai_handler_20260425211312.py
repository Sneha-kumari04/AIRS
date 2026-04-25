import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume(resume, job):
    prompt = f"""
You are an AI resume screening system.

Analyze the resume vs job description and return:

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

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=prompt
        )
            return response.text
        else:
            return "No response from AI"

    except Exception as e:
        return f"Error: {str(e)}"
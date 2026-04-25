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
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.candidates[0].content.parts[0].text

    except Exception as e:
        return f"Error: {str(e)}"
    
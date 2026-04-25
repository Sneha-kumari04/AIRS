import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_resume(jd_text, resume_text):
    prompt = f"""
You are an expert HR recruiter and resume analyst.

Given the Job Description and Resume below, analyze the fit and return ONLY valid JSON with exactly this structure:
{{
  "match_score": (integer between 0 and 100),
  "matched_skills": ["skill1", "skill2"],
  "missing_skills": ["skill1", "skill2"],
  "improvement_tips": ["tip1", "tip2"],
  "verdict": "Strong Fit" or "Moderate Fit" or "Weak Fit"
}}

Job Description:
{jd_text}

Resume:
{resume_text}

Return ONLY valid JSON. No explanation. No markdown. No backticks.
"""

    try:
        response = client.models.generate_content(
            ,
            contents=prompt
        )
        raw = response.text.strip()

        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
            raw = raw.strip()

        result = json.loads(raw)
        return result

    except json.JSONDecodeError:
        raise Exception(f"Gemini returned invalid JSON: {raw}")
    except Exception as e:
        raise Exception(f"Gemini API error: {str(e)}")
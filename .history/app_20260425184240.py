from flask import Flask, render_template, request
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

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        resume = request.form.get("resume")
        job = request.form.get("job")

        if resume and job:
            prompt = f"""
You are an AI resume screening system.

Analyze the resume against the job description and provide:

1. Match Score (in percentage)
2. Key Strengths
3. Missing Skills
4. Improvement Suggestions

Keep the response clear and structured.

Resume:
{resume}

Job Description:
{job}
"""
            try:
                response = model.generate_content(prompt)
                result = response.text
            except Exception as e:
                result = f"Error: {str(e)}"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
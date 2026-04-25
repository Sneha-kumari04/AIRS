

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
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
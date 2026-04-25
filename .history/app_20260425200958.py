import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from utils.ai_handler import analyze_resume
from PyPDF2 import PdfReader

app = Flask(__name__)

# Home route (loads UI)
@app.route("/")
def home():
    return render_template("index.html")



@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("resume")
    job = request.form.get("job")

    if not file or not job:
        return jsonify({"result": "Missing input"})
    if file.filename.endswith(".pdf"):
    
    else:
             resume_text = file.read().decode("utf-8", errors="ignore")
    try:
        reader = PdfReader(file)
        resume_text = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:
                resume_text += text

    except Exception as e:
        return jsonify({"result": f"Error reading PDF: {str(e)}"})
    
    result = analyze_resume(resume_text, job)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
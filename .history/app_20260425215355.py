import os
from flask import Flask, render_template, request, jsonify
from utils.ai_handler import analyze_resume
from PyPDF2 import PdfReader

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("resume")
    jd_text = request.form.get("job")

    # Validation
    if not file or not jd_text:
        return jsonify({"error": "Please upload a resume and enter a job description."}), 400
    
    filename = file.filename.lower()
    if not (filename.endswith(".pdf") or filename.endswith(".txt")):
     return jsonify({"error": "Only PDF or TXT files are allowed."}), 400

    # Extract resume text
    try:
        if file.filename.endswith(".pdf"):
            reader = PdfReader(file)
            resume_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    resume_text += text
        else:
            resume_text = file.read().decode("utf-8", errors="ignore")

        if not resume_text.strip():
            return jsonify({"error": "Only PDF or TXT files are allowed."}), 400

    except Exception as e:
        return jsonify({"error": f"File read error: {str(e)}"}), 500

    # AI Analysis
    try:
        result = analyze_resume(jd_text, resume_text)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": f"AI analysis failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
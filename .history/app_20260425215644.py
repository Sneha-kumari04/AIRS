import os
from flask import Flask, render_template, request, jsonify
from utils.ai_handler import analyze_resume
from PyPDF2 import PdfReader

app = Flask(__name__)

ALLOWED_EXTENSIONS = {".pdf", ".txt"}
MAX_FILE_SIZE_MB = 5


def allowed_file(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Check file exists
    file = request.files.get("resume")
    jd_text = request.form.get("job", "").strip()

    if not file or file.filename == "":
        return jsonify({"error": "Please upload a resume file."}), 400

    if not jd_text:
        return jsonify({"error": "Please enter a job description."}), 400

    # Check file type
    if not allowed_file(file.filename):
        return jsonify({"error": "Only PDF or TXT files are allowed."}), 400

    # Check file size
    file.seek(0, os.SEEK_END)
    file_size_mb = file.tell() / (1024 * 1024)
    file.seek(0)
    if file_size_mb > MAX_FILE_SIZE_MB:
        return jsonify({"error": f"File too large. Max size is {MAX_FILE_SIZE_MB}MB."}), 400

    # Extract resume text
    try:
        _, ext = os.path.splitext(file.filename)
        if ext.lower() == ".pdf":
            reader = PdfReader(file)
            resume_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    resume_text += text
        else:
            resume_text = file.read().decode("utf-8", errors="ignore")

        if not resume_text.strip():
            return jsonify({"error": "Could not extract text from resume. Please try a different file."}), 400

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
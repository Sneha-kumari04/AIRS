from flask import Flask, render_template, request, jsonify
from utils.ai_handler import analyze_resume(resume, job),
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("resume")
    job = request.form.get("job")

    if not file or not job:
        return jsonify({"result": "Missing input"})

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

    except Exception as e:
        return jsonify({"result": f"Error reading file: {str(e)}"})

    result = analyze_resume(resume_text, job)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
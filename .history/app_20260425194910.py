from flask import Flask, render_template, request, jsonify
from utils.ai_handler import analyze_resume

app = Flask(__name__)

# Home route (loads UI)
@app.route("/")
def home():
    return render_template("index.html")


# API route (called by JS fetch)
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    resume = data.get("resume")
    job = data.get("job")

    # Basic validation
    if not resume or not job:
        return jsonify({"result": "Please provide both resume and job description."})

    # Call AI handler
    result = analyze_resume(resume, job)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
import json
from datetime import date
from flask import Flask, render_template, request, jsonify
from utils.ai_handler import analyze_resume

app = Flask(__name__)

# Home route (loads UI)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    resume = data.get("resume")
    job = data.get("job")

    if not resume or not job:
        return jsonify({"result": "Please provide both resume and job description."})

    result = analyze_resume(resume, job)

    # ✅ SAVE TO JSON
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "resume": resume,
        "job": job,
        "result": result
    }

    try:
        with open("data.json", "r") as f:
            existing_data = json.load(f)
    except:
        existing_data = []

    existing_data.append(entry)

    with open("data.json", "w") as f:
        json.dump(existing_data, f, indent=4)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
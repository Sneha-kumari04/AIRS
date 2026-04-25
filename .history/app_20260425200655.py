import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from utils.ai_handler import analyze_resume

app = Flask(__name__)

# Home route (loads UI)
@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
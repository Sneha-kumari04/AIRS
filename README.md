# AIRS — AI Resume Screening System

AIRS (Automated Intelligence for Resume Screening) is an AI-powered web application that analyzes resumes against job descriptions and provides instant insights such as match score, skill gaps, and improvement suggestions.
Built using Flask and powered by Google Gemini AI, AIRS helps streamline the hiring process with fast, intelligent, and actionable analysis.
---

##  Features

1. User uploads a resume
2. User enters job description
3. Resume text is extracted (PDF/TXT)
4. Gemini AI analyzes resume vs job
5. System returns:

   * Match score
   * Strengths
   * Missing skills
   * Suggestions

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **AI Engine:** Google Gemini API
* **Deployment:** Render
* **PDF Parsing:** PyPDF2



##  Project Structure

```
AIRS/
│
├── app.py
├── utils/
│   └── ai_handler.py
├── templates/
│   ├── index.html
│   └── analyzer.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
└── README.md
```

---

##  Demo

👉 

---

##  Live 🔗

👉 https://airs-1.onrender.com

---

##  Use Cases

* Resume screening automation
* Job seekers improving resumes
* Recruiters filtering candidates faster

---

##  Limitations

* Depends on API quota (Gemini limits)
* Works best with text-based PDFs
* Accuracy depends on prompt quality

---

## 👩‍💻 Author

**Sneha Kumari**
Built as part of an AI project / hackathon submission.

---

##  License

This project is for educational and demonstration purposes.

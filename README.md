# 🚀 LinkedIn Profile Optimizer AI

An AI-powered web application that analyzes LinkedIn profile PDFs and provides intelligent suggestions to improve profile quality, ATS compatibility, and recruiter visibility.

---

## 📌 Features

- 📄 Upload LinkedIn Profile PDF
- 🤖 AI-powered profile analysis
- 📊 Overall Profile Score
- 💼 ATS Compatibility Evaluation
- ✨ Improved Professional Headline Suggestions
- 📝 About Section Enhancement
- 🛠️ Skill Recommendations
- 💡 Experience Improvement Suggestions
- 📈 Career & Profile Insights
- 🎯 Recruiter-focused Feedback

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI

### AI
- Groq API (LLM)

### Libraries
- PyMuPDF
- python-dotenv
- python-multipart

---

## 📂 Project Structure

```
LinkedIn-Profile-Optimizer-AI/
│
├── backend/
│   ├── main.py
│   ├── groq_ai.py
│   └── pdf_reader.py
│
├── css/
│   ├── style.css
│   ├── upload.css
│   ├── loading.css
│   └── result.css
│
├── index.html
├── upload.html
├── loading.html
├── result.html
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/LinkedIn-Profile-Optimizer-AI.git
```

### Navigate to the project

```bash
cd LinkedIn-Profile-Optimizer-AI
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```
GROQ_API_KEY=your_api_key_here
```

### Run the backend

```bash
uvicorn backend.main:app --reload
```

### Open the frontend

Run a local server and open:

```
index.html
```

---

## 📸 Workflow

1. Upload your LinkedIn Profile PDF.
2. AI extracts profile information.
3. The model analyzes the content.
4. Receive:
   - Overall Score
   - ATS Score
   - Headline Suggestions
   - About Section Improvements
   - Skills to Add
   - Experience Suggestions
   - Career Recommendations

---

## 🎯 Future Enhancements

- LinkedIn URL Analysis
- Resume Upload Support
- Skill Gap Analysis
- Job Role Matching
- Downloadable PDF Report
- Interactive Dashboard
- Data Visualizations & Charts

---

## 👩‍💻 Developed By

**Likitha Bandaru**

BCA Data Science Student

Passionate about AI, Data Analytics, and Web Development.

---

## ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub!

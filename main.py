from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from dotenv import load_dotenv

from pdf_reader import extract_text_from_pdf
from groq_ai import analyze_profile

load_dotenv()

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "LinkedIn Profile Optimizer AI Backend Running"}


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    # Save uploaded PDF
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    profile_text = extract_text_from_pdf(file_path)

    # Analyze LinkedIn profile using Groq
    analysis = analyze_profile(profile_text)

    return {
        "status": "success",
        "analysis": analysis
    }

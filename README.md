# 🧠 Summarizer Service

A lightweight, Python-based microservice built using **FastAPI** that summarizes long pull request (PR) descriptions into concise summaries using Hugging Face Transformers.

---

## 🚀 Features

- 🔁 `/summarize` – Summarize long PR descriptions via POST request
- ❤️ `/health` – Basic health check route
- 🤖 Uses Hugging Face's `distilbart-cnn-12-6` model (runs locally, free)
- ⚡ Built for speed, modularity, and ease of deployment

---

## 🛠 Tech Stack

- **Python 3.8+**
- **FastAPI** (framework)
- **Hugging Face Transformers** (NLP model)
- **Uvicorn** (ASGI server)

---

## 🔧 Setup Instructions

### 1. Clone the repository

git clone https://github.com/your-username/Summarizer-Service.git
cd summarizer-service

### 2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the app

python run.py

**The app will be live at: http://localhost:8000**

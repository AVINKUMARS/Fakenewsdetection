# Fake News Detection

A Python and React-based project to detect whether a news article is **real** or **fake** using a pre-trained NLP model.

---

## Project Structure

- **Backend**: Python + Flask + Hugging Face Transformers
- **Frontend**: React.js

---

## Features

- Detects if a news article is real or fake
- Simple UI to input news headlines
- Uses a pre-trained NLP model (`facebook/bart-large-mnli`) with zero-shot classification

---

## Prerequisites

- Python 3.11+
- Node.js & npm
- Internet connection to download the model from Hugging Face

---

## Setup Instructions

### 1. Backend

1. Navigate to the backend folder (if you have separate backend folder)  
   ```bash
   cd backend
2.Install Python dependencies
  ```bash
  py requirement.py
3.Run the backend server:
 ```bash
py app.py

###  2.Frontend Setup

Navigate to the frontend folder:
cd frontend
Install npm dependencies:
npm i
Start the frontend server:

npm run start

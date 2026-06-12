# AI-Powered Document Summarization System

**Teyzix Core Internship - June Batch**  
**Task ID:** AI-INT-1  
**Domain:** Artificial Intelligence / NLP  
**Difficulty:** Intermediate  

---

## Project Overview

This is an AI-based document summarization system that automatically extracts
key information from long text documents and generates short, meaningful summaries
using Natural Language Processing (NLP) techniques.

---

## Features

- Accept input from Direct Text, TXT file, or PDF file
- Text Preprocessing (Lowercasing, Tokenization, Stopword Removal)
- Frequency-Based Extractive Summarization
- TF-IDF Based Extractive Summarization
- Adjustable Summary Length (1-10 sentences)
- Top Keywords Extraction
- Sentence Importance Scoring with Bar Chart
- Text Statistics (Words, Sentences, Characters)
- Export Summary as .TXT file
- Streamlit Web UI (Bonus)

---

## Project Structure

    document_summarizer/
    |
    |-- app.py              -> Streamlit UI (main entry point)
    |-- summarizer.py       -> Core summarization logic
    |-- preprocessor.py     -> Text preprocessing (NLTK)
    |-- file_handler.py     -> File loading and export
    |-- analytics.py        -> Keywords and frequency analysis
    |-- sample_docs/
    |   |-- sample.txt      -> Sample test document
    |-- README.md           -> Project documentation

---

## Tech Stack

| Tool          | Purpose                  |
|---------------|--------------------------|
| Python 3.12   | Core language            |
| NLTK          | NLP preprocessing        |
| Scikit-learn  | TF-IDF vectorization     |
| PyPDF2        | PDF file reading         |
| Streamlit     | Web UI                   |
| NumPy         | Numerical operations     |

---

## Installation and Setup

Step 1 - Install dependencies:

    pip install nltk scikit-learn PyPDF2 streamlit numpy

Step 2 - Download NLTK data:

    python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"

Step 3 - Run the app:

    streamlit run app.py

Step 4 - Open browser:

    http://localhost:8501

---

## How It Works

    Input Text / File
          |
    Preprocessing (NLTK)
    -> Lowercase -> Tokenize -> Remove Stopwords
          |
    Summarization
    -> Frequency Scoring / TF-IDF Scoring
    -> Rank Sentences -> Pick Top N
          |
    Output
    -> Summary + Keywords + Chart + Export

---

## Modules

### preprocessor.py
Handles all NLP preprocessing:
- Sentence segmentation
- Word tokenization
- Stopword removal
- Word frequency counting

### summarizer.py
Core summarization logic:
- Frequency-based scoring
- TF-IDF based scoring
- Sentence ranking and selection

### file_handler.py
File operations:
- Load .txt files
- Load .pdf files
- Export summary as .txt

### analytics.py
Text analysis:
- Top keyword extraction
- Sentence importance scores
- Text statistics

### app.py
Streamlit web interface:
- Input options (text/txt/pdf)
- Settings sidebar
- Results display
- Download buttons

---

## Developer

**Name:** Haseeb  
**Internship:** Teyzix Core - June Batch  
**Task:** AI-INT-1 - AI-Powered Document Summarization System

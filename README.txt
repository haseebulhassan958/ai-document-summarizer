PROJECT: AI-Powered Document Summarization System
Task ID: AI-INT-1
Intern: Haseeb
Internship: Teyzix Core - June Batch

-----------------------------------------
SHORT DESCRIPTION:
-----------------------------------------
This project is an AI-based document summarization system built using
Python and NLP techniques. It automatically extracts key sentences from
long documents and generates short, meaningful summaries. It supports
text input, TXT file upload, and PDF file upload. A Streamlit web UI
is included as a bonus feature.

-----------------------------------------
HOW TO RUN THE PROJECT:
-----------------------------------------
Step 1: Install required libraries:
pip install nltk scikit-learn PyPDF2 streamlit numpy

Step 2: Download NLTK data:
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"

Step 3: Run the app:
streamlit run app.py

Step 4: Open browser and go to:
http://localhost:8501

-----------------------------------------
BONUS FEATURES:
-----------------------------------------
- Streamlit Web UI for live summarization
- Language Detection (detects input language using langdetect library)

-----------------------------------------
PROJECT FILES:
-----------------------------------------
app.py          -> Streamlit UI
summarizer.py   -> Summarization logic
preprocessor.py -> NLP preprocessing
file_handler.py -> File loading/export
analytics.py    -> Keywords & analytics
sample_docs/    -> Sample test document
README.md       -> Full documentation
README.txt      -> This file
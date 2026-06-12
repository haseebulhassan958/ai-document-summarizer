# file_handler.py
# File Loading and Export Module

import os
import PyPDF2

def load_text_file(filepath):
    """Load content from .txt file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"

def load_pdf_file(filepath):
    """Load content from .pdf file"""
    try:
        text = ""
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text.strip()
    except FileNotFoundError:
        return "Error: PDF file not found."
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def load_file(filepath):
    """Auto-detect file type and load"""
    if not os.path.exists(filepath):
        return "Error: File does not exist."
    
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext == '.txt':
        return load_text_file(filepath)
    elif ext == '.pdf':
        return load_pdf_file(filepath)
    else:
        return "Error: Only .txt and .pdf files supported."

def export_summary(summary, output_path="summary_output.txt"):
    """Export summary to .txt file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=== AI GENERATED SUMMARY ===\n\n")
            f.write(summary)
        return f"Summary saved to: {output_path}"
    except Exception as e:
        return f"Error saving file: {str(e)}"
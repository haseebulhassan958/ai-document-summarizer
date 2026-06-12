# preprocessor.py
# Text Preprocessing Module

import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

def preprocess_text(text):
    """Full preprocessing pipeline"""
    sentences = get_sentences(text)
    words = get_words(text)
    cleaned_words = remove_stopwords(words)
    return sentences, words, cleaned_words

def get_sentences(text):
    """Split text into sentences"""
    return sent_tokenize(text)

def get_words(text):
    """Lowercase + tokenize into words"""
    text = text.lower()
    words = word_tokenize(text)
    words = [w for w in words if w not in string.punctuation]
    return words

def remove_stopwords(words):
    """Remove common stopwords"""
    stop_words = set(stopwords.words('english'))
    return [w for w in words if w not in stop_words]

def get_word_frequency(cleaned_words):
    """Count frequency of each word"""
    freq = {}
    for word in cleaned_words:
        freq[word] = freq.get(word, 0) + 1
    return freq
# summarizer.py
# Core Summarization Logic

from preprocessor import get_sentences, get_words, remove_stopwords, get_word_frequency
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def frequency_based_summary(text, num_sentences=3):
    """Extractive summarization using word frequency scoring"""
    sentences = get_sentences(text)
    
    if len(sentences) <= num_sentences:
        return text
    
    words = get_words(text)
    cleaned_words = remove_stopwords(words)
    word_freq = get_word_frequency(cleaned_words)
    
    # Score each sentence
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = get_words(sentence)
        score = 0
        for word in sentence_words:
            if word in word_freq:
                score += word_freq[word]
        sentence_scores[sentence] = score
    
    # Pick top N sentences
    ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    top_sentences = ranked[:num_sentences]
    
    # Return in original order
    summary = [s for s in sentences if s in top_sentences]
    return ' '.join(summary)


def tfidf_based_summary(text, num_sentences=3):
    """Extractive summarization using TF-IDF scoring"""
    sentences = get_sentences(text)
    
    if len(sentences) <= num_sentences:
        return text
    
    # TF-IDF vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)
    
    # Score = sum of TF-IDF values per sentence
    scores = np.array(tfidf_matrix.sum(axis=1)).flatten()
    
    # Get top N sentence indices
    ranked_indices = np.argsort(scores)[::-1][:num_sentences]
    ranked_indices = sorted(ranked_indices)
    
    summary = [sentences[i] for i in ranked_indices]
    return ' '.join(summary)


def get_summary(text, method='frequency', num_sentences=3):
    """Main summarization function"""
    if not text or len(text.strip()) == 0:
        return "Error: Empty text provided."
    
    if method == 'frequency':
        return frequency_based_summary(text, num_sentences)
    elif method == 'tfidf':
        return tfidf_based_summary(text, num_sentences)
    else:
        return frequency_based_summary(text, num_sentences)
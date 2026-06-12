# analytics.py
# Analytics Module - Keywords & Word Frequency

from preprocessor import get_sentences, get_words, remove_stopwords, get_word_frequency

def get_top_keywords(text, top_n=10):
    """Extract top N most important keywords"""
    words = get_words(text)
    cleaned_words = remove_stopwords(words)
    freq = get_word_frequency(cleaned_words)
    
    # Sort by frequency
    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_keywords[:top_n]

def get_sentence_scores(text):
    """Score every sentence by importance"""
    sentences = get_sentences(text)
    words = get_words(text)
    cleaned_words = remove_stopwords(words)
    word_freq = get_word_frequency(cleaned_words)
    
    scored = {}
    for i, sentence in enumerate(sentences):
        sentence_words = get_words(sentence)
        score = sum(word_freq.get(w, 0) for w in sentence_words)
        scored[f"Sentence {i+1}"] = score
    
    return scored

def get_text_stats(text):
    """Basic text statistics"""
    sentences = get_sentences(text)
    words = get_words(text)
    cleaned_words = remove_stopwords(words)
    
    stats = {
        "Total Characters": len(text),
        "Total Sentences": len(sentences),
        "Total Words": len(words),
        "Unique Words (no stopwords)": len(set(cleaned_words))
    }
    return stats

# ─── Language Detection ────────────────────────────────

from langdetect import detect, LangDetectException

LANGUAGE_NAMES = {
    'en': 'English',
    'ur': 'Urdu',
    'hi': 'Hindi',
    'ar': 'Arabic',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'zh-cn': 'Chinese',
    'ru': 'Russian',
    'pt': 'Portuguese',
    'tr': 'Turkish',
    'fa': 'Persian'
}

def detect_language(text):
    """Detect the language of the given text"""
    try:
        code = detect(text)
        name = LANGUAGE_NAMES.get(code, code.upper())
        return code, name
    except LangDetectException:
        return "unknown", "Unknown"
# app.py
# Main Streamlit UI - AI Document Summarizer

import streamlit as st
import os
import tempfile
from summarizer import get_summary
from file_handler import load_file, export_summary
from analytics import get_top_keywords, get_sentence_scores, get_text_stats, detect_language

# ─── Page Config ───────────────────────────────────────
st.set_page_config(
    page_title="AI Document Summarizer",
    page_icon="📄",
    layout="wide"
)

# ─── Title ─────────────────────────────────────────────
st.title("📄 AI-Powered Document Summarization System")
st.markdown("**Teyzix Core Internship | Task ID: AI-INT-1**")
st.divider()

# ─── Sidebar Settings ──────────────────────────────────
st.sidebar.header("⚙️ Settings")

input_method = st.sidebar.radio(
    "Input Method:",
    ["Direct Text Input", "Upload TXT File", "Upload PDF File"]
)

summary_method = st.sidebar.selectbox(
    "Summarization Method:",
    ["frequency", "tfidf"],
    format_func=lambda x: "Frequency Based" if x == "frequency" else "TF-IDF Based"
)

num_sentences = st.sidebar.slider(
    "Summary Length (sentences):",
    min_value=1,
    max_value=10,
    value=3
)

top_keywords_n = st.sidebar.slider(
    "Top Keywords to Show:",
    min_value=5,
    max_value=20,
    value=10
)

# ─── Input Section ─────────────────────────────────────
input_text = ""

if input_method == "Direct Text Input":
    st.subheader("✍️ Enter Your Text")
    input_text = st.text_area(
        "Paste your document here:",
        height=200,
        placeholder="Enter long text here to summarize..."
    )

elif input_method == "Upload TXT File":
    st.subheader("📁 Upload Text File")
    uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])
    if uploaded_file:
        input_text = uploaded_file.read().decode("utf-8")
        st.success("✅ File loaded successfully!")
        with st.expander("Preview Loaded Text"):
            st.write(input_text)

elif input_method == "Upload PDF File":
    st.subheader("📑 Upload PDF File")
    uploaded_file = st.file_uploader("Choose a .pdf file", type=["pdf"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        input_text = load_file(tmp_path)
        os.unlink(tmp_path)
        st.success("✅ PDF loaded successfully!")
        with st.expander("Preview Loaded Text"):
            st.write(input_text)

# ─── Summarize Button ──────────────────────────────────
st.divider()

if st.button("🚀 Generate Summary", use_container_width=True):
    if not input_text or len(input_text.strip()) == 0:
        st.error("❌ Please provide some text first!")
    else:
        with st.spinner("Analyzing and summarizing..."):

            # Generate Summary
            summary = get_summary(input_text, method=summary_method, num_sentences=num_sentences)

            # Analytics
            keywords = get_top_keywords(input_text, top_n=top_keywords_n)
            sentence_scores = get_sentence_scores(input_text)
            stats = get_text_stats(input_text)

        # ─── Results ───────────────────────────────────
        st.success("✅ Summary Generated!")

        # ─── Language Detection ─────────────────────────
        lang_code, lang_name = detect_language(input_text)
        if lang_code == "en":
            st.info(f"🌐 Detected Language: **{lang_name}**")
        elif lang_code == "unknown":
            st.warning("🌐 Could not detect language.")
        else:
            st.warning(f"🌐 Detected Language: **{lang_name}** — Note: Summarization is optimized for English text only.")

        # Two columns layout
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📝 Original Text")
            st.info(input_text)

        with col2:
            st.subheader("✨ AI Summary")
            st.success(summary)

        st.divider()

        # ─── Text Stats ────────────────────────────────
        st.subheader("📊 Text Statistics")
        stat_cols = st.columns(4)
        for i, (key, value) in enumerate(stats.items()):
            stat_cols[i].metric(key, value)

        st.divider()

        # ─── Keywords ──────────────────────────────────
        st.subheader("🔑 Top Keywords")
        keyword_cols = st.columns(5)
        for i, (word, freq) in enumerate(keywords):
            keyword_cols[i % 5].metric(word, f"freq: {freq}")

        st.divider()

        # ─── Sentence Scores ───────────────────────────
        st.subheader("📈 Sentence Importance Scores")
        st.bar_chart(sentence_scores)

        st.divider()

        # ─── Export ────────────────────────────────────
        st.subheader("💾 Export Summary")
        export_col1, export_col2 = st.columns(2)

        with export_col1:
            st.download_button(
                label="⬇️ Download Summary as TXT",
                data=f"=== AI GENERATED SUMMARY ===\n\n{summary}",
                file_name="summary_output.txt",
                mime="text/plain",
                use_container_width=True
            )

        with export_col2:
            st.download_button(
                label="⬇️ Download Keywords as TXT",
                data="\n".join([f"{w}: {f}" for w, f in keywords]),
                file_name="keywords_output.txt",
                mime="text/plain",
                use_container_width=True
            )
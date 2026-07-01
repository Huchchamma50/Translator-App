import os
import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="About",
    page_icon="👨‍💻",
    layout="wide"
)

# =====================================================
# LOAD CSS
# =====================================================

def load_css():
    css_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "style.css"
    )

    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# =====================================================
# TITLE
# =====================================================

st.title("👨‍💻 About AI Language Translator Pro")

st.divider()

# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.subheader("📌 Project Overview")

st.write("""
AI Language Translator Pro is a modern AI-powered translation application
built using Python and Streamlit.

The application allows users to:

✅ Translate text instantly

✅ Upload TXT and PDF files

✅ Automatically detect languages

✅ Save translation history

✅ Manage favorite translations

✅ View dashboard analytics

✅ Convert translated text into speech
""")

st.divider()

# =====================================================
# DEVELOPER
# =====================================================

st.subheader("👨‍💻 Developer")

st.write("**Name:** Shivam Soni")
st.write("**Branch:** Electronics & Communication Engineering")
st.write("**Role:** AI/ML & Embedded Systems Enthusiast")

st.divider()

# =====================================================
# TECHNOLOGIES
# =====================================================

st.subheader("🛠 Technologies Used")

st.markdown("""
- 🐍 Python
- 🎨 Streamlit
- 🌐 Deep Translator (GoogleTranslator)
- 🔎 LangDetect
- 📄 PyPDF2
- 📊 Pandas
- 📈 Matplotlib
- 🔊 gTTS
""")

st.divider()

# =====================================================
# SUPPORTED LANGUAGES
# =====================================================

st.subheader("🌍 Supported Languages")

languages = [
    "English", "Hindi", "French", "German", "Spanish",
    "Italian", "Japanese", "Chinese", "Arabic", "Russian",
    "Portuguese", "Dutch", "Bengali", "Punjabi", "Marathi",
    "Tamil", "Telugu", "Kannada", "Malayalam", "Urdu",
    "Korean", "Turkish", "Greek", "Polish", "Swedish",
    "Norwegian", "Finnish", "Danish", "Czech", "Romanian",
    "Hungarian", "Vietnamese", "Thai", "Indonesian",
    "Gujarati", "Nepali", "Persian", "Hebrew",
    "Ukrainian", "Croatian", "Slovak", "Slovenian",
    "Catalan", "Afrikaans", "Swahili"
]

st.success(f"🌍 Total Supported Languages: {len(languages)}+")

cols = st.columns(4)

for i, lang in enumerate(languages):
    cols[i % 4].write(f"• {lang}")

st.divider()

# =====================================================
# FEATURES
# =====================================================

st.subheader("🚀 Application Features")

st.markdown("""
- ✅ Real-time Translation
- ✅ Automatic Language Detection
- ✅ PDF Document Translation
- ✅ TXT File Translation
- ✅ Download Translation
- ✅ Translation History
- ✅ Favorite Translations
- ✅ Text-to-Speech Support
- ✅ Dashboard Analytics
""")

st.divider()

# =====================================================
# PROJECT STATUS
# =====================================================

st.subheader("📊 Project Status")

st.success("🚀 AI Language Translator Pro v2.0 is Ready for Use!")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
### 👨‍💻 Developer

****Huchchamma**

Electronics & Communication Engineering Student

Built with ❤️ using:

- 🐍 Python
- 🎨 Streamlit
- 🌐 Deep Translator
- 📄 PyPDF2
- 🔎 LangDetect

### AI Language Translator Pro v2.0
""")
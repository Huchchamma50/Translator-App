import os
import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect
from PyPDF2 import PdfReader

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Translator Pro",
    page_icon="🌍",
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
# LANGUAGE CODES
# =====================================================

lang_codes = {
    "Automatic": "auto",
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Dutch": "nl",
    "Greek": "el",
    "Turkish": "tr",
    "Polish": "pl",
    "Romanian": "ro",
    "Hungarian": "hu",
    "Czech": "cs",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Croatian": "hr",
    "Serbian": "sr",
    "Bulgarian": "bg",
    "Ukrainian": "uk",
    "Danish": "da",
    "Swedish": "sv",
    "Norwegian": "no",
    "Finnish": "fi",
    "Estonian": "et",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Vietnamese": "vi",
    "Thai": "th",
    "Indonesian": "id",
    "Malay": "ms",
    "Filipino": "tl",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Urdu": "ur",
    "Nepali": "ne",
    "Persian": "fa",
    "Hebrew": "he"
}

# =====================================================
# SESSION STATE
# =====================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "translation_count" not in st.session_state:
    st.session_state.translation_count = 0

if "languages_used" not in st.session_state:
    st.session_state.languages_used = set()

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if "detected_language" not in st.session_state:
    st.session_state.detected_language = ""

if "original_text" not in st.session_state:
    st.session_state.original_text = ""

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🌍 AI Translator Pro")

st.sidebar.write("👨‍💻 Developer: Huchchamma")
st.sidebar.write("📌 Version: 2.0")

st.sidebar.divider()

st.sidebar.metric(
    "Total Translations",
    st.session_state.translation_count
)

st.sidebar.metric(
    "Languages Used",
    len(st.session_state.languages_used)
)

# =====================================================
# MAIN TITLE
# =====================================================

st.title("🌍 AI Language Translator Pro")

st.write(
    "Translate text, TXT files, and PDF documents instantly into multiple languages."
)

st.divider()

# =====================================================
# MAIN LAYOUT
# =====================================================

col1, col2 = st.columns(2)
# =====================================================
# LEFT COLUMN - INPUT
# =====================================================

with col1:

    # Text Input
    text = st.text_area(
        "✍️ Enter Text",
        height=250,
        placeholder="Type your text here..."
    )

    st.caption(f"Characters: {len(text)}")

    # File Upload
    uploaded_file = st.file_uploader(
        "📄 Upload TXT or PDF",
        type=["txt", "pdf"]
    )

    if uploaded_file is not None:

        if uploaded_file.name.endswith(".txt"):

            text = uploaded_file.read().decode("utf-8")

        elif uploaded_file.name.endswith(".pdf"):

            reader = PdfReader(uploaded_file)

            pdf_text = ""

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:
                    pdf_text += extracted + "\n"

            text = pdf_text

        st.success("✅ File Loaded Successfully")

        st.text_area(
            "File Content",
            value=text,
            height=180
        )

    # Language Selection
    language = st.selectbox(
        "🌍 Select Target Language",
        list(lang_codes.keys()),
        index=1
    )

    # Translate Button
    translate_btn = st.button(
        "🚀 Translate",
        use_container_width=True
    )

# =====================================================
# TRANSLATION LOGIC
# =====================================================

if translate_btn:

    if not text.strip():

        st.warning("⚠ Please enter text or upload a file.")

    else:

        try:

            st.session_state.original_text = text

            detected = detect(text)

            translated = GoogleTranslator(
                source="auto",
                target=lang_codes[language]
            ).translate(text)

            st.session_state.detected_language = detected
            st.session_state.translated_text = translated

            st.session_state.translation_count += 1
            st.session_state.languages_used.add(language)

            preview = (
                text[:100] + "..."
                if len(text) > 100
                else text
            )

            translated_preview = (
                translated[:100] + "..."
                if len(translated) > 100
                else translated
            )

            st.session_state.history.append(
                f"{preview} → {translated_preview}"
            )

            st.success("✅ Translation Successful!")

        except Exception as e:

            st.error(f"❌ Translation Error: {e}")

# =====================================================
# RIGHT COLUMN - OUTPUT
# =====================================================

with col2:

    st.subheader("📤 Translation Output")

    if st.session_state.detected_language:

        st.info(
            f"Detected Language: {st.session_state.detected_language.upper()}"
        )

    if st.session_state.translated_text:

        st.text_area(
            "Translated Result",
            value=st.session_state.translated_text,
            height=220
        )

        st.download_button(
            label="📥 Download Translation",
            data=st.session_state.translated_text,
            file_name="translation.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.divider()

        if st.button(
            "⭐ Add To Favorites",
            use_container_width=True
        ):

            already_exists = any(
                fav["original"] == st.session_state.original_text
                and fav["language"] == language
                for fav in st.session_state.favorites
            )

            if already_exists:

                st.warning(
                    "This translation is already in Favorites."
                )

            else:

                st.session_state.favorites.append(
                    {
                        "original": st.session_state.original_text,
                        "translated": st.session_state.translated_text,
                        "language": language,
                    }
                )

                st.success("⭐ Added to Favorites!")
                # =====================================================
# TRANSLATION HISTORY
# =====================================================

st.divider()

st.subheader("📜 Translation History")

if st.session_state.history:

    for i, item in enumerate(
        reversed(st.session_state.history),
        start=1
    ):

        st.write(f"**{i}.** {item}")

else:

    st.info("No translations yet.")

# =====================================================
# FAVORITE TRANSLATIONS
# =====================================================

st.divider()

st.subheader("⭐ Favorite Translations")

if st.session_state.favorites:

    for i, fav in enumerate(
        st.session_state.favorites,
        start=1
    ):

        with st.expander(f"Favorite {i}"):

            st.markdown("**Original Text**")
            st.write(fav["original"])

            st.markdown("**Translated Text**")
            st.write(fav["translated"])

            st.markdown("**Target Language**")
            st.write(fav["language"])

else:

    st.info("No favorite translations yet.")

# =====================================================
# QUICK STATS
# =====================================================

st.divider()

st.subheader("📊 Quick Statistics")

stat1, stat2, stat3 = st.columns(3)

with stat1:
    st.metric(
        "Total Translations",
        st.session_state.translation_count
    )

with stat2:
    st.metric(
        "Languages Used",
        len(st.session_state.languages_used)
    )

with stat3:
    st.metric(
        "Favorites",
        len(st.session_state.favorites)
    )

# =====================================================
# MANAGE DATA
# =====================================================

st.divider()

st.subheader("🧹 Manage Data")

clear1, clear2 = st.columns(2)

with clear1:

    if st.button(
        "🗑️ Clear History",
        use_container_width=True
    ):

        st.session_state.history = []

        st.success("✅ History cleared successfully.")

        st.rerun()

with clear2:

    if st.button(
        "⭐ Clear Favorites",
        use_container_width=True
    ):

        st.session_state.favorites = []

        st.success("✅ Favorites cleared successfully.")

        st.rerun()

# =====================================================
# RESET TRANSLATOR
# =====================================================

st.divider()

if st.button(
    "🔄 Reset Translator",
    use_container_width=True
):

    st.session_state.original_text = ""
    st.session_state.translated_text = ""
    st.session_state.detected_language = ""

    st.success("✅ Translator reset successfully.")

    st.rerun()

# =====================================================
# SESSION SUMMARY
# =====================================================

st.divider()

with st.expander("📈 Session Summary", expanded=False):

    st.write(
        f"**Total Translations:** {st.session_state.translation_count}"
    )

    st.write(
        f"**Languages Used:** {len(st.session_state.languages_used)}"
    )

    st.write(
        f"**Favorite Translations:** {len(st.session_state.favorites)}"
    )

    if st.session_state.languages_used:

        st.markdown("**Languages Selected:**")

        for lang in sorted(st.session_state.languages_used):

            st.write(f"• {lang}")

    else:

        st.info("No languages used yet.")
        # =====================================================
# HELP SECTION
# =====================================================

st.divider()

with st.expander("ℹ️ How To Use", expanded=False):

    st.markdown("""
### 🚀 Steps

1. ✍️ Enter text in the text box or upload a **TXT/PDF** file.
2. 🌍 Select your target language.
3. 🚀 Click **Translate**.
4. 📤 View the translated output.
5. 📥 Download the translated text.
6. ⭐ Save important translations to Favorites.
7. 📜 Review Translation History.
8. 🧹 Clear History or Favorites whenever required.
""")

# =====================================================
# FEATURES
# =====================================================

st.divider()

st.subheader("✨ Features")

feature1, feature2 = st.columns(2)

with feature1:

    st.success("✔ Real-time Text Translation")
    st.success("✔ Automatic Language Detection")
    st.success("✔ TXT File Translation")
    st.success("✔ PDF File Translation")

with feature2:

    st.success("✔ Translation History")
    st.success("✔ Favorite Translations")
    st.success("✔ Download Translation")
    st.success("✔ Session Statistics")

# =====================================================
# ABOUT DEVELOPER
# =====================================================

st.divider()

with st.expander("👨‍💻 About Developer", expanded=False):

    st.markdown("""
## Shivam Soni

**Electronics & Communication Engineering Student**

### Interests

- 🤖 Artificial Intelligence
- 🐍 Python Development
- ⚡ Electronics
- 🔌 Embedded Systems
- 🧠 Machine Learning
- 💻 Software Development

This project demonstrates an AI-powered multilingual translator
built using Python and Streamlit with support for text, TXT,
and PDF translation.

It is designed to provide a clean, fast, and user-friendly
translation experience.
""")

# =====================================================
# TECHNOLOGIES USED
# =====================================================

st.divider()

st.subheader("🛠 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.info("🐍 Python")

with tech2:
    st.info("🎨 Streamlit")

with tech3:
    st.info("🌍 Deep Translator")

tech4, tech5 = st.columns(2)

with tech4:
    st.info("📄 PyPDF2")

with tech5:
    st.info("🔍 LangDetect")

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div style="
text-align:center;
padding:25px;
color:#6B7280;
font-size:16px;
">

<h3 style="color:#2563EB;">
🌍 AI Language Translator Pro
</h3>

<p>
Built with ❤️ using <b>Python</b> & <b>Streamlit</b>
</p>

<p>
Version <b>2.0</b>
</p>

<p>
Developed by <b>Shivam Soni</b>
</p>

<hr style="margin-top:20px; margin-bottom:15px;">

<p style="font-size:14px;">
© 2026 All Rights Reserved
</p>

</div>
""", unsafe_allow_html=True)
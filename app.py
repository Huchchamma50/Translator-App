import os
import streamlit as st

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

    file_path = os.path.join(
        os.path.dirname(__file__),
        "style.css"          # <-- ".." hata diya
    )

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# =====================================================
# HOME PAGE
# =====================================================

st.title("🌍 AI Language Translator Pro")

st.markdown("""
### Welcome to AI Translator Pro

Use the sidebar to navigate between the pages:

- 🌍 Translator
- 📜 History
- 📊 Dashboard
- 👨‍💻 About
""")

st.info("Built by Huchchamma 🚀")

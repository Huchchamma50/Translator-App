import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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
# SESSION STATE
# =====================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "languages_used" not in st.session_state:
    st.session_state.languages_used = set()

if "translation_count" not in st.session_state:
    st.session_state.translation_count = 0

if "favorites" not in st.session_state:
    st.session_state.favorites = []

# =====================================================
# TITLE
# =====================================================

st.title("📊 AI Translator Dashboard")

st.write("Monitor your translation activity and usage statistics.")

st.divider()

# =====================================================
# QUICK METRICS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Translations",
    st.session_state.translation_count
)

col2.metric(
    "Languages Used",
    len(st.session_state.languages_used)
)

col3.metric(
    "History",
    len(st.session_state.history)
)

col4.metric(
    "Favorites",
    len(st.session_state.favorites)
)

st.divider()

# =====================================================
# LANGUAGES USED
# =====================================================

st.subheader("🌍 Languages Used")

if st.session_state.languages_used:

    cols = st.columns(3)

    for i, lang in enumerate(sorted(st.session_state.languages_used)):
        cols[i % 3].success(lang)

else:
    st.info("No language data available yet.")

st.divider()

# =====================================================
# LANGUAGE ANALYTICS
# =====================================================

st.subheader("📈 Language Analytics")

if st.session_state.languages_used:

    language_list = list(st.session_state.languages_used)

    df = pd.DataFrame({
        "Language": language_list,
        "Count": [1] * len(language_list)
    })

    st.bar_chart(
        df.set_index("Language")
    )

    st.divider()

    st.subheader("🥧 Language Distribution")

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        df["Count"],
        labels=df["Language"],
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

else:
    st.info("Translate something to generate analytics.")

st.divider()

# =====================================================
# HISTORY
# =====================================================

st.subheader("📜 Recent Translation History")

if st.session_state.history:

    for item in reversed(st.session_state.history[-10:]):
        st.write("•", item)

else:
    st.info("No translation history yet.")

st.divider()

# =====================================================
# INSIGHTS
# =====================================================

st.subheader("🏆 Insights")

if st.session_state.translation_count == 0:

    st.info("No insights available yet.")

else:

    st.success(
        f"You have completed **{st.session_state.translation_count}** translations."
    )

    st.write(
        f"🌍 Languages explored: **{len(st.session_state.languages_used)}**"
    )

    st.write(
        f"⭐ Favorite translations: **{len(st.session_state.favorites)}**"
    )

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown(
"""
### 📊 Dashboard

Monitor your AI Translator usage in real time.

Developed by **Huchchamma**

**AI Language Translator Pro v2.0**
"""
)
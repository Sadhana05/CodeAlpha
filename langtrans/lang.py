import streamlit as st
from googletrans import Translator, LANGUAGES

# Page setup
st.set_page_config(
    page_title="Smart Translator",
    page_icon="🌍",
    layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        color: black;
    }

    h1, h2, h3, h4, h5, h6, p, span, label {
        color: black !important;
    }

    textarea, select, input {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
    }

    button {
        background-color: #f0f0f0 !important;
        color: black !important;
        border: 1px solid #bbb !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

translator = Translator()

def get_key(val):
    for key, value in LANGUAGES.items():
        if value == val:
            return key
    return None

# Title
st.title("🌍 Smart AI Language Translator")
st.caption("Simple • Stable • Student-friendly")

# Tabs for unique UI
tab1, tab2 = st.tabs(["✍️ Translate", "ℹ️ About"])

with tab1:
    st.subheader("Select Target Language")
    language = st.selectbox(
        "Language",
        options=sorted(LANGUAGES.values())
    )

    st.subheader("Enter Text")
    text = st.text_area(
        "",
        height=150,
        placeholder="Type your text here..."
    )

    if st.button("🚀 Translate"):
        if text.strip() == "":
            st.warning("⚠️ Please enter some text")
        else:
            try:
                lang_key = get_key(language)
                result = translator.translate(text, dest=lang_key)

                st.success("✅ Translation Successful")
                st.text_area(
                    "Translated Text",
                    result.text,
                    height=150
                )
            except Exception:
                st.error("❌ Translation failed. Please try again later.")

with tab2:
    st.markdown("""
    ### 🌐 About This App
    - Built using **Streamlit**
    - Uses **Google Translate API**
    - Supports **100+ languages**
    - Beginner-friendly UI

    👩‍💻 Perfect for:
    - College mini projects  
    - Hackathons  
    - Resume demos  
    """)

st.divider()
st.caption("🚀 Developed for learning & demonstration")


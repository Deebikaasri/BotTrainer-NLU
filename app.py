import streamlit as st
import pandas as pd
from intent_classifier import classify_intent
from evaluate_model import evaluate_model

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="BotTrainer NLU Demo",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS – LAVENDER MIXED THEME + BLACK TEXT + TOP SPACING
# --------------------------------------------------
st.markdown("""
<style>

/* ---------- APP BACKGROUND ---------- */
.stApp {
    background: linear-gradient(180deg, #ede9fe, #e0e7ff); /* light lavender */
    color: #000000; /* text black */
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"] {
    background-color: #312e81; /* dark lavender */
    border-right: 1px solid #4338ca;
}
section[data-testid="stSidebar"] * {
    color: #f8fafc !important; /* sidebar text readable */
}

/* ---------- MAIN CONTAINER ---------- */
.block-container {
    padding-top: 3rem; /* more space from top */
}

/* ---------- TOP BAR (STOP / DEPLOY AREA) ---------- */
header[data-testid="stHeader"] {
    background: linear-gradient(180deg, #ede9fe, #e0e7ff); /* same as main background */
    border-bottom: 1px solid #c7d2fe;
}

/* ---------- TITLES ---------- */
.main-title {
    font-size: 42px;
    font-weight: 900;
    text-align: center;
    color: #000000; /* black text */
    margin-top: 60px; /* added extra spacing above BotTrainer heading */
}
.subtitle {
    text-align: center;
    color: #1e1b4b; /* slightly darker lavender for subtitle */
    margin-bottom: 22px;
}

/* ---------- INPUT LABEL ---------- */
label {
    color: #000000 !important;
    font-size: 16px;
    font-weight: 700;
}

/* ---------- INPUT BOX ---------- */
input {
    background-color: #f5f3ff !important; /* light lavender */
    color: #000000 !important;
    border-radius: 12px !important;
    border: 2px solid #6366f1 !important;
    font-size: 16px !important;
}

/* Placeholder */
input::placeholder {
    color: #4f46e5 !important;
}

/* ---------- SECTION HEADERS ---------- */
h3 {
    color: #4338ca !important; /* deep violet for headers */
    font-weight: 800;
}

/* ---------- METRICS ---------- */
div[data-testid="metric-container"] {
    background-color: #f5f3ff; /* light lavender */
    border: 1px solid #a5b4fc;
    border-radius: 14px;
    padding: 20px;
}

div[data-testid="metric-container"] label {
    color: #1e1b4b !important;
    font-size: 14px;
}

div[data-testid="metric-container"] div {
    color: #000000 !important;
    font-size: 28px !important;
    font-weight: 900 !important;
}

/* ---------- JSON OUTPUT ---------- */
pre {
    background-color: #f5f3ff !important;
    color: #000000 !important;
    border-radius: 12px;
    border: 1px solid #a5b4fc;
}

/* ---------- DATAFRAME ---------- */
[data-testid="stDataFrame"] {
    background-color: #f5f3ff;
    color: #000000;
    border-radius: 12px;
}

/* ---------- BUTTONS ---------- */
button[kind="primary"] {
    background-color: #4f46e5 !important; /* violet button */
    color: white !important;
    border-radius: 10px;
    font-weight: 800;
}
button:hover {
    background-color: #4338ca !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("🔎 Navigation")
page = st.sidebar.radio("Go to", ["NLU Tester", "Model Evaluation"])

# --------------------------------------------------
# NLU TESTER PAGE
# --------------------------------------------------
if page == "NLU Tester":

    st.markdown('<div class="main-title">🤖 BotTrainer NLU Demo</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Intent Detection & Entity Extraction</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        user_input = st.text_input(
            "Enter your message",
            placeholder=""
        )

        if user_input:
            result = classify_intent(user_input)

            st.markdown("### Prediction")
            st.write("**Intent:**", result.get("intent"))
            st.write("**Confidence:**", result.get("confidence"))

            st.markdown("### Extracted Entities")
            st.json(result.get("entities"))

# --------------------------------------------------
# MODEL EVALUATION PAGE
# --------------------------------------------------
elif page == "Model Evaluation":

    st.markdown('<div class="main-title">📊 Model Evaluation</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Performance metrics on test dataset</div>', unsafe_allow_html=True)

    if st.button("▶ Run Evaluation"):
        metrics = evaluate_model()

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Accuracy", f"{metrics['accuracy']*100:.2f}%")
        c2.metric("Precision", f"{metrics['precision']*100:.2f}%")
        c3.metric("Recall", f"{metrics['recall']*100:.2f}%")
        c4.metric("F1 Score", f"{metrics['f1']*100:.2f}%")

        st.markdown("## Confusion Matrix")

        cm = metrics.get("confusion_matrix")
        labels = metrics.get("labels")

        if cm is not None and labels is not None:
            df_cm = pd.DataFrame(cm, index=labels, columns=labels)
            st.dataframe(df_cm, use_container_width=True)

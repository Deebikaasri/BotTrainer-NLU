# 🤖 BotTrainer – LLM-Based NLU Model Trainer & Evaluator

BotTrainer is an end-to-end **LLM-based Natural Language Understanding (NLU)** system that performs **intent classification** and **entity extraction** using **prompt engineering** instead of traditional machine learning classifiers.

The system follows a **JSON-first design**, uses a **local Gemma-3 model via Ollama**, and provides **evaluation metrics** along with an **interactive Streamlit web interface** for real-time testing.

---

## 📌 Project Objectives

* Build an NLU pipeline using **Large Language Models (LLMs)**
* Replace classical ML-based intent classifiers with **prompt-based inference**
* Perform **intent detection** and **entity extraction** in a single step
* Evaluate performance using:

  * Accuracy
  * Precision
  * Recall
  * F1-score
* Provide a **real-time chatbot-style UI** using Streamlit
* Follow a **production-style project structure** suitable for academic and real-world use

---

## 🧠 Key Features

* 📄 **JSON-based intent & entity schema** (`intents.json`)
* 🧩 **Prompt engineering** with schema-guided constraints
* 🖥️ **Local LLM inference** using **Gemma-3** (via Ollama)
* ✅ **Automatic JSON parsing & validation** of LLM output
* 📊 **Evaluation pipeline** with confusion matrix
* 🌐 **Streamlit web interface** for live intent testing

---

## 📦 Dataset Design

### Primary Dataset: `intents.json`

The dataset defines:

* Intent names
* Example utterances
* Entity schema per intent


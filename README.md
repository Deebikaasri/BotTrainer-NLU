# 🤖 BotTrainer – LLM-Based NLU Model Trainer & Evaluator for Chatbots

BotTrainer is an end-to-end **LLM-powered Natural Language Understanding (NLU)** system designed to perform **intent classification** and **entity extraction** using **prompt engineering** instead of traditional machine learning classifiers.

The project demonstrates how modern **Large Language Models (LLMs)** can replace classical NLU pipelines while still supporting **evaluation metrics**, **structured outputs**, and a **real-time interactive UI**.

---

## 📌 Project Overview

Traditional NLU systems require large labeled datasets, feature engineering, and frequent retraining.  
BotTrainer eliminates these limitations by using **schema-guided prompt engineering** with LLMs to perform NLU tasks without model training.

The system uses:
- JSON-based intent and evaluation datasets
- Local LLM inference (Gemma-3 via Ollama)
- Structured JSON outputs
- Streamlit-based interactive UI
- Standard classification evaluation metrics

---

## 🎯 Objectives

- Build an NLU pipeline using Large Language Models (LLMs)
- Replace classical ML intent classifiers with prompt-based inference
- Perform intent detection and entity extraction simultaneously
- Evaluate predictions using Accuracy, Precision, Recall, and F1-score
- Visualize results using a confusion matrix
- Provide a real-time chatbot-style interface
- Follow a modular, production-style project structure

---

## 🧠 Key Features

- 📄 JSON-first NLU dataset design
- 🧩 Schema-guided prompt engineering
- 🖥️ Local LLM inference using **Gemma-3 (Ollama)**
- ✅ Automatic JSON parsing and validation
- 📊 Evaluation pipeline with confusion matrix
- 🌐 Interactive Streamlit web application
- 🧱 Modular and scalable architecture

---

## 📊 Evaluation Metrics

The performance of the NLU system is evaluated using standard classification metrics:

- Accuracy – Measures overall correctness of predictions
- Precision – Measures correctness of predicted intents
- Recall – Measures how well actual intents are identified
- F1-score – Harmonic mean of precision and recall

A confusion matrix is also generated to visualize prediction errors and analyze intent-level performance.

## 🖥️ Run the Application

### Install dependencies
pip install -r requirements.txt

### Start the local LLM
ollama run gemma:3

### Run the Streamlit app
streamlit run app.py

### 🧩Technologies Used
- python
- Streamlit
- Scitkit learn
- pandas
- prompt engineering

### 🎓 Learning Outcomes 

- Basic knowledge of Python programming.
- Familiarity with Streamlit for interactive web applications.
- Understanding of Natural Language Processing (NLP) concepts like intents and entities.
- Basic knowledge of Python programming.
- Basic knowledge of prompt engineering for LLMs.

### 🔮 Future Enhancements
  - Entity Extraction: Extend the system to extract multiple entities from messages.
  - Multi-Language Support: Support intents in multiple languages.
  - Custom Model Training: Allow fine-tuning of models on domain-specific data.
  - Improved Evaluation Metrics: Add precision, recall, and F1-score evaluation.
  - Analytics Dashboard: Visualize model performance trends using charts.
  - Integration with Messaging Platforms: Connect with Slack, WhatsApp, or Telegram bots.
  - User Feedback Loop: Collect user feedback to improve intent accuracy over time.

  

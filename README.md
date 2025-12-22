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
## 🗂️ Project Structure

BotTrainer/
│
├── data/
│ └── eval_data.json # Evaluation dataset
├── prompts/
│ └── intent_prompt.txt # Prompt template
├── app.py # Streamlit application
├── intent_classifier.py # LLM-based NLU logic
├── evaluator_model.py # Evaluation & metrics
├── requirements.txt # Dependencies
└── README.md # Project documentation
## 🗂️ Project Structure


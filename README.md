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

 🧠 System Architecture – BotTrainer
User Input (Text Query)
        ↓
Prompt Template + Intent Schema (JSON-first)
        ↓
Gemma-3 LLM (Local Inference via Ollama)
        ↓
Structured JSON Output (Intent + Entities)
        ↓
Intent & Entity Parsing & Validation
        ↓
Evaluation Engine (Accuracy, Precision, Recall, F1, Confusion Matrix)
        ↓
Streamlit UI Visualization (Predictions, Metrics, Dashboard)

📦 Dataset Design & 🧪 Evaluation Strategy
1️⃣ Primary Dataset – intents.json (Core Dataset)

The BotTrainer system follows a JSON-first dataset design, where the LLM directly consumes the intent schema during inference.
No intermediate feature extraction or vector embeddings are used.

Each intent definition contains:

Intent name

Training examples (user utterances)

Supported entity types

📌 Example
{
  "intents": [
    {
      "name": "book_flight",
      "examples": [
        "Book a flight to Delhi",
        "I want to fly to Mumbai tomorrow"
      ],
      "entities": ["location", "date"]
    }
  ],
  "entities": {
    "location": ["Delhi", "Mumbai", "Chennai"],
    "date": ["today", "tomorrow"]
  }
}
2️⃣ Flattened Dataset – full_nlu_dataset_200.csv

The flattened dataset is programmatically generated from intents.json and is used for:

Model evaluation

Performance visualization

Dataset analysis

📊 Dataset Schema
Column Name	Description
text	User utterance
true_intent	Ground truth intent label

✔ Enables compatibility with evaluation libraries
✔ Supports confusion matrix and metric computation

🧪 Evaluation Strategy

The evaluation approach is designed to fairly validate all intents without bias.

🔹 Evaluation Setup

Total Intents: 10

Evaluation Samples: 1 sample per intent

Total Evaluation Size: 10 samples

📈 Metrics Used

The following standard classification metrics are computed:

Accuracy

Precision (Weighted)

Recall (Weighted)

F1-Score (Weighted)

Confusion Matrix

These metrics provide a comprehensive view of NLU performance, including both overall accuracy and per-intent behavior.

---


## 📦 Dataset Design

### Primary Dataset: `intents.json`

The dataset defines:

* Intent names
* Example utterances
* Entity schema per intent


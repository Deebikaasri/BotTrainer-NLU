# 🤖 BotTrainer – LLM-Based NLU Model Trainer & Evaluator

BotTrainer is a modern Natural Language Understanding (NLU) framework built using Large Language Models (LLMs) to identify user intents and extract entities through prompt engineering, rather than relying on conventional machine-learning classifiers.

The system is designed around a JSON-centric dataset, runs locally using the Gemma-3 model via Ollama, and offers live predictions, evaluation metrics, and dataset insights through an intuitive Streamlit interface.

🚀 Core Features

🔹 Intent recognition powered by LLM reasoning

🔹 JSON-based intent and entity definitions

🔹 Prompt-driven structured responses

🔹 Fully local inference using Gemma-3

🔹 Built-in evaluation with performance metrics

🔹 Modular, scalable project organization

🔹 Interactive dashboard for testing and analysis

🎯 Project Goals

Eliminate dependency on traditional intent classifiers

Combine intent classification and entity extraction in a single inference step

Ensure LLM outputs follow a strict JSON structure

Measure NLU performance using standard evaluation metrics

Provide an easy-to-use interface for experimentation

Follow industry-standard ML project practices

🧠 System Architecture Overview
User Query
   ↓
Prompt Template + Intent Definitions
   ↓
Gemma-3 LLM (Ollama – Local Execution)
   ↓
Structured JSON Response
   ↓
Intent & Entity Extraction
   ↓
Evaluation Results & UI Display

📦 Dataset Design
1️⃣ Core Dataset – intents.json

BotTrainer follows a JSON-first approach, where intent definitions are directly injected into the LLM prompt.

Each intent includes:

Intent label

Example user queries

Associated entity types

Sample Structure
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


Why JSON-first?

✔ Directly consumed by the LLM

✔ No embeddings or vector stores required

✔ Easy to modify and extend for new domains

2️⃣ Evaluation Dataset – full_nlu_dataset_200.csv

A flattened dataset generated from intents.json to support:

Performance evaluation

Metric computation

Dataset visualization

Dataset Columns

Field	Description
text	Input sentence
true_intent	Expected intent
🧪 Evaluation Methodology

Number of intents: 10

Test samples: One example per intent

Total evaluation inputs: 10

Evaluation Benefits

Ensures equal coverage for all intents

Avoids skew caused by repeated samples

Enables transparent intent-wise validation

Metrics Calculated

Accuracy

Precision (weighted)

Recall (weighted)

F1-Score (weighted)

Confusion Matrix

🗂️ Repository Structure
INFOSIS_BOTTRAINER/
│
├── assets/                 # UI screenshots
├── config/                 # Configuration files
├── data/
│   └── raw_data/           # Dataset files
├── logs/                   # Application logs
├── src/
│   ├── components/         # Core logic modules
│   ├── pipeline/           # End-to-end workflows
│   └── utils/              # Utilities & helpers
├── app.py                  # Streamlit app
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation & Usage
Install Dependencies
pip install -r requirements.txt

Download Gemma-3 Model
ollama pull gemma3:latest

Launch Application
streamlit run app.py

🧩 Technology Stack

Python

Streamlit

Pandas

Scikit-learn

Ollama

Gemma-3 LLM

Prompt Engineering

🎓 Skills & Learnings

Building LLM-driven NLU pipelines

Designing JSON-centric AI systems

Structured prompt engineering

Evaluating intent classification models

Developing interactive ML dashboards

Managing scalable ML project layouts

👨‍💻 Developer
S.Deebikaasri

⭐ Planned Improvements

Entity-level performance evaluation

Visual confusion matrix heatmaps

Prompt debugging and inspection tools

Multi-model comparison support

Containerized deployment using Docker

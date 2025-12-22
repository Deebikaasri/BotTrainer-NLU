🤖 BotTrainer – LLM-Based NLU Model Trainer & Evaluator

BotTrainer is a Natural Language Understanding (NLU) framework powered by Large Language Models (LLMs) that performs intent classification and entity extraction using prompt engineering instead of traditional machine learning classifiers.

The project adopts a JSON-first dataset design, uses a local Gemma-3 model via Ollama, and provides real-time predictions and evaluation capabilities through a Streamlit-based interface.

🚀 Features

LLM-driven intent classification

Prompt-based entity extraction

JSON-centric intent and entity schema

Structured LLM outputs enforced via prompts

Local inference using Gemma-3 (no cloud dependency)

Built-in evaluation pipeline with standard metrics

Modular and production-oriented project structure

🎯 Project Objectives

Replace classical intent classification models with LLM-based inference

Perform intent detection and entity extraction in a single step

Ensure structured JSON output from LLM responses

Evaluate NLU performance using industry-standard metrics

Provide an interactive interface for testing and evaluation

Follow best practices in ML project organization

🧠 System Architecture
User Input
   ↓
Prompt Template + Intent Schema
   ↓
Gemma-3 LLM (Local Execution via Ollama)
   ↓
Structured JSON Output
   ↓
Intent & Entity Parsing
   ↓
Evaluation Results & UI Display

📦 Dataset Design
1️⃣ Core Dataset – intents.json

The system follows a JSON-first approach, where the intent schema is directly provided to the LLM during inference.

Each intent definition contains:

Intent name

Example user utterances

Supported entity types

Example Structure
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


Key Advantages

Directly consumed by the LLM

No embeddings or vector databases required

Easy to extend with new intents and entities

2️⃣ Evaluation Dataset – full_nlu_dataset_200.csv

A flattened dataset generated from intents.json, used for:

Model evaluation

Metric computation

Dataset analysis

Schema

Column	Description
text	User utterance
true_intent	Ground truth intent
🧪 Evaluation Strategy

Total intents: 10

Evaluation samples: One sample per intent

Total evaluation size: 10 samples

This strategy ensures:

All intents are evaluated at least once

No bias from repeated samples

Clear intent-wise correctness validation

Metrics Used

Accuracy

Precision (weighted)

Recall (weighted)

F1-score (weighted)

Confusion Matrix

🖥️ User Interface (Streamlit)

The Streamlit application provides:

Real-time intent prediction

Confidence score display

Structured entity extraction output

One-click model evaluation

Dataset statistics and analysis

🗂️ Project Structure
INFOSIS_BOTTRAINER/
│
├── config/                  # Configuration files
├── data/
│   └── raw_data/            # Dataset files
├── logs/                    # Log files
├── src/
│   ├── components/          # Core NLU logic
│   ├── pipeline/            # Evaluation pipeline
│   └── utils/               # Utility modules
├── app.py                   # Streamlit application
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Setup and Execution
Install Dependencies
pip install -r requirements.txt

Pull Gemma-3 Model
ollama pull gemma3:latest

Run the Application
streamlit run app.py

🧩 Technologies Used

Python

Streamlit

Pandas

Scikit-learn

Ollama

Gemma-3 LLM

Prompt Engineering

🎓 Learning Outcomes

Building LLM-based NLU systems

Designing JSON-first AI pipelines

Prompt engineering for structured outputs

Evaluating intent classification systems

Developing modular ML applications

Applying industry-style project structuring

👨‍💻 Author

S.Deebikaasri

⭐ Future Scope

Entity-level evaluation metrics

Visual confusion matrix representations

Prompt debugging and inspection tools

Multi-LLM model comparison

Deployment using Docker or cloud platforms


import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

EVAL_FILE = r"C:\Users\kamal\OneDrive\Desktop\BotTrainer\eval_data.json"

with open(EVAL_FILE, "r", encoding="utf-8") as f:
    eval_data = json.load(f)

y_true = [item["intent"] for item in eval_data]
y_pred = [item["predicted_intent"] for item in eval_data]

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average="weighted", zero_division=0)
recall = recall_score(y_true, y_pred, average="weighted", zero_division=0)
f1 = f1_score(y_true, y_pred, average="weighted", zero_division=0)

print(f"Accuracy : {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall   : {recall:.2f}")
print(f"F1-score : {f1:.2f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_true, y_pred))

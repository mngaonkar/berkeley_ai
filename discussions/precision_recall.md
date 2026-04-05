# Difference between precision, recall, and F1-score. When would you optimize for precision vs recall?

| Metric | Formula | What it measures | Interpretation |
|--------|---------|------------------|----------------|
| Precision | TP / (TP + FP) | Of all the positive predictions the model made, how many were actually correct? | Accuracy of positive predictions |
| Recall | TP / (TP + FN) | Of all the actual positives in the data, how many did the model correctly find? | Coverage of actual positives |
| F1-Score | 2 × (Precision × Recall) / (Precision + Recall) | Harmonic mean of Precision and Recall | Balanced score between Precision & Recall |

- **When to optimize for Precision**:
  - When the cost of a false positive is high.
  - Example: Email spam detection (you don't want to mark important emails as spam).
- **When to optimize for Recall**:
  - When the cost of a false negative is high.
  - Example: Disease screening (you don't want to miss any positive cases).
- **When to optimize for F1-Score**:
  - When you want a balance between Precision and Recall, especially when the class distribution is imbalanced.
  - Example: Document classification where both false positives and false negatives are costly.
  - Example: Fraud detection (you want to catch as many fraud cases as possible while minimizing false alarms).


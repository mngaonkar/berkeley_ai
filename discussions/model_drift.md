# Model Drift

1. Monitor for drift continuously
   track three things separately:
   - Data drift: input feature distributions changing from training
   - Concept drift: relationship between inputs and target changing
   - Prediction drift: model output distribution shifting

2. Compare production vs training and recent baseline
   - training baseline
   - recent production performance (last 7-30 days)
   - recent production input distribution (last 7-30 days)

3. Measure business impact, not just statistical drift
   Some drift is harmless. I connect drift to:
   - accuracy / precision / recall / F1 / AUC
   - calibration
   - false positive / false negative cost
   - business KPIs like conversion, fraud catch rate, SLA, escalation rate

4. Diagnose root cause before acting
    - Is it data drift, concept drift, or prediction drift?
    - Which features are drifting? (feature importance + SHAP)
    - Is the drift due to seasonality, new user behavior, or a bug?
    - data pipeline/schema changes
  
  A lot of “model drift” is actually data quality or feature computation mismatch.

5. Respond with guardrails
   Depending on severity, use:
   - alerts only
   - threshold adjustment
   - fallback rules / heuristic model
   - route low-confidence cases to human review
   - canary rollback to previous model
   - traffic shifting between champion and challenger models

6. Retrain only when justified
   Do not retrain automatically on every drift signal. Retrain when:
   - performance degradation is confirmed
   - drift is persistent
   - new data is representative
   - retraining passes validation
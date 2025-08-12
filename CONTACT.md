# EXECUTIVE SUMMARY
Loan Default / Risk Scoring — Executive Summary

Project goal
Build a reproducible ML pipeline that predicts loan defaults using real-world tabular data. The pipeline demonstrates data cleaning, targeted feature engineering, multicollinearity handling (VIF), imbalance mitigation (SMOTETomek), and model explainability.

Approach
- Clean raw data and derive robust features (e.g., `credit_history_length` computed from a fixed snapshot date).  
- Use frequency encoding for high-cardinality categories and careful numeric transforms.  
- Detect and remove multicollinear features using iterative VIF.  
- Train and evaluate classifiers (RandomForest baseline, XGBoost primary) within a cross-validation.  
- Tune decision thresholds by optimizing F1 for the chosen operating point and produce PR/ROC and calibration plots.

Key results (example)
- XGBoost (CV + threshold tuning): ROC-AUC ≈ 0.74, F1 ≈ 0.36  
Interpretation: The model provides useful discrimination between good and bad loans; further business-driven calibration (precision@k, cost-sensitive thresholds) is recommended before production use.

Next steps
1. Formalize the labeling policy (business definition of default).  
2. Finalize reproducibility: add config file, deterministic snapshot date, and run scripts.  
3. Add calibration and precision@k analyses and run hyperparameter tuning (Optuna).  
4. Prepare a short demo & one-page slide for interviews.

Contact
Juba Amari — amari.juba2006@gmail.com — github.com/Juba-Amr

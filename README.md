# README.md
# Loan Default / Risk Scoring — End-to-End Project

**One-line:** An end-to-end data science project that builds a loan default classifier from raw CSVs to trained XGBoost models, with feature engineering, imbalance handling (SMOTETomek), a preprocessing pipeline, threshold tuning and explainability.

**Status:** Work in progress — reproducible pipeline + notebooks included.  
**Author:** Juba Amari — Math student / aspiring AI engineer

---

## TL;DR (elevator pitch)
This repo demonstrates hands-on experience with messy, real-world tabular data: cleaning, feature engineering, multicollinearity handling (VIF), class imbalance strategies, model training (RandomForest, XGBoost), and model evaluation with business-minded threshold tuning. Primary evaluation: **XGBoost — AUC ≈ 0.74, F1 ≈ 0.36** (example results). The code is organized so a reviewer can run the preprocessing and training end-to-end.

---


---

## Project goals
1. Build a reproducible pipeline that transforms raw loan data into model-ready features.  
2. Create a classifier that predicts loan defaults (business-oriented metric).  
3. Demonstrate ML hygiene: avoid leakage, handle imbalance, evaluate with appropriate metrics, and explain model behavior.

---

## Dataset
Place your CSV/Parquet loan dataset in `data/raw/`. The notebooks assume a tabular CSV file from the lending club dataset.

---

## Key design choices & rationale
- **Target definition:** Binary `bad_loan` label (customizable in `app/src/map.py`).  
- **Feature engineering:** Convert `earliest_cr_line` into a fixed snapshot date. Use frequency encoding for high-cardinality, and one hot encoding for low cardinality features.  
- **Multicollinearity:** Iterative VIF dropping to stabilize importance measures.  
- **Imbalance handling:** `SMOTETomek` within folds to avoid leakage (not used at the end because of poor generalization on synthetic data).  
- **Modeling:** XGBoost as primary model with threshold tuning to maximize business-oriented F1.  
- **Explainability:** Permutation importance for global feature attribution.

---

## Quickstart (example)
1. Clone the repo:
```bash
git clone <repo-url>
cd loan-default-project
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.\.venv\Scripts\activate     # Windows PowerShell
pip install -r requirements.txt
```


Results (example)

- ROC-AUC: ~0.74

- F1-score (tuned threshold): ~0.36 (primarly because of a lot of false positives)

These are sample results used to demonstrate experimentation. Business-driven tuning required for deployment.

See `CONTACT.md` for contact details.






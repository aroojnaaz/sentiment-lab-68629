# 🧠 LEGAL NOTICE CLASSIFICATION SYSTEM  
# SENTIMENT LAB 68629  

# 🚀 PROJECT DESCRIPTION  

This project is a multi-class text classification system designed to categorize legal notices into three classes:

- Contract Dispute  
- Intellectual Property Claim  
- Regulatory Compliance  

It compares two machine learning models:

- Logistic Regression  
- Naive Bayes  

Feature extraction methods:

- Bag of Words (BoW)  
- TF-IDF  

# 📊 DATASET INFORMATION  

The dataset contains:

- id  
- category  
- label (target class)  
- notice (raw legal text)  

Classes:

- Contract Dispute  
- Intellectual Property Claim  
- Regulatory Compliance  

# ⚙️ SETUP INSTRUCTIONS  

## 1. CLONE REPOSITORY  

git clone https://github.com/aroojnaaz/sentiment-lab-68629.git  

## 2. CREATE VIRTUAL ENVIRONMENT  

python -m venv venv  
venv\Scripts\activate  

## 3. INSTALL DEPENDENCIES  

pip install -r requirements.txt  

## 4. RUN NOTEBOOK  

notebooks/sentiment_analysis.ipynb  

Run all cells from top to bottom  

# ⚙️ CONFIGURATION (config.json)  

Random seed = 42  
Test size = 0.2  
Max features = 5000  
Model parameters for Logistic Regression and Naive Bayes  

# 🧪 METHODOLOGY  

TEXT PREPROCESSING  
- Lowercasing  
- Cleaning text  

FEATURE ENGINEERING  

Bag of Words (BoW)  
TF-IDF  

MODELS USED  
- Logistic Regression  
- Naive Bayes  

# 📊 RESULTS SUMMARY  

Naive Bayes (BoW) → Accuracy 1.0, F1 1.0  
Naive Bayes (TF-IDF) → Accuracy 1.0, F1 1.0  
Logistic Regression (BoW) → Accuracy 1.0, F1 1.0  
Logistic Regression (TF-IDF) → Accuracy 1.0, F1 1.0  

# 📌 KEY INSIGHTS  

Dataset is highly separable  
Both models perform equally well  
Naive Bayes is faster  
Logistic Regression is more stable  

# 🧾 MLFLOW TRACKING  

Multiple runs executed (6+)  
Accuracy logged  
F1-score logged  
Model comparison performed  

# ⚠️ LIMITATIONS  

Small dataset  
No deep learning models  
Limited noise variation  

# 🚀 FUTURE IMPROVEMENTS  

BERT / Transformer models  
Larger dataset  
Hyperparameter tuning  
API deployment  

# 👩‍💻 AUTHOR  

Machine Learning Lab Project  
GitHub: https://github.com/aroojnaaz/sentiment-lab-68629  

# 📌 CONCLUSION  

This project demonstrates a complete machine learning pipeline for legal text classification using traditional NLP techniques. Logistic Regression and Naive Bayes both achieve high accuracy due to strong separability in dataset.

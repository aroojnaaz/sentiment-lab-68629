🧠 LEGAL NOTICE CLASSIFICATION SYSTEM
SENTIMENT LAB 68629
<br>
🚀 PROJECT DESCRIPTION

This project is a multi-class text classification system designed to categorize legal notices into three classes:

Contract Dispute
Intellectual Property Claim
Regulatory Compliance

It compares two machine learning models:

Logistic Regression
Naive Bayes

with two feature extraction methods:

Bag of Words (BoW)
TF-IDF
<br>
📊 DATASET INFORMATION

The dataset contains:

id
category
label (target class)
notice (raw legal text)

Classes:

Contract Dispute
Intellectual Property Claim
Regulatory Compliance
<br>
⚙️ SETUP INSTRUCTIONS
1. CLONE REPOSITORY
git clone https://github.com/aroojnaaz/sentiment-lab-68629.git
2. CREATE VIRTUAL ENVIRONMENT
python -m venv venv

Activate:

venv\Scripts\activate
3. INSTALL DEPENDENCIES
pip install -r requirements.txt
4. RUN NOTEBOOK

Open:

notebooks/sentiment_analysis.ipynb

Run all cells from top to bottom.

<br>
⚙️ CONFIGURATION (config.json)

This file contains all hyperparameters:

Random seed = 42
Test size = 0.2
Max features = 5000
Model parameters (LR & NB)
<br>
🧪 METHODOLOGY
TEXT PREPROCESSING
Lowercasing text
Cleaning raw legal notices
FEATURE ENGINEERING
Bag of Words (BoW)

Word frequency based representation

TF-IDF

Weighted importance of words

MACHINE LEARNING MODELS
Logistic Regression
Multinomial Naive Bayes
<br>
📊 RESULTS SUMMARY
Model	Feature	Accuracy	F1 Score
Naive Bayes	BoW	1.0	1.0
Naive Bayes	TF-IDF	1.0	1.0
Logistic Regression	BoW	1.0	1.0
Logistic Regression	TF-IDF	1.0	1.0
<br>
📌 KEY INSIGHTS
Dataset has strong separable vocabulary
Both models perform equally well
Naive Bayes is faster
Logistic Regression is more stable
<br>
🧾 MLFLOW EXPERIMENT TRACKING
Multiple runs executed (6+)
Accuracy and F1-score logged
Model comparison performed
<br>
⚠️ LIMITATIONS
Small dataset
No deep learning models
Limited noise variation
<br>
🚀 FUTURE IMPROVEMENTS
BERT / Transformer models
Larger dataset
Hyperparameter tuning
API deployment
<br>
👩‍💻 AUTHOR

Machine Learning Lab Project
GitHub: https://github.com/aroojnaaz/sentiment-lab-68629

<br>
📌 CONCLUSION

This project demonstrates effective legal text classification using traditional machine learning techniques with high accuracy on structured data.

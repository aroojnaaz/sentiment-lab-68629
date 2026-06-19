README.md (Rewritten Version)
Legal Notice Classification System

Sentiment Lab 68299

Project Overview

This project is a multi-class text classification system designed to automatically categorize legal notices into predefined legal categories. It is built as a prototype for a legal-tech environment where fast document understanding is required.

The system compares traditional NLP approaches using:

Logistic Regression
Naive Bayes

with two feature extraction methods:

Bag of Words (BoW)
TF-IDF Vectorization

The goal is to evaluate performance trade-offs between accuracy and computational efficiency.

Problem Statement

Legal documents are often lengthy and time-consuming to analyze manually. This project solves this problem by automatically classifying short legal notices into:

Contract Dispute
Intellectual Property Claim
Regulatory Compliance
Installation & Setup

Follow the steps below to run the project locally:

1. Clone Repository
git clone https://github.com/javeriakhalid15/sentiment-lab-68299.git
2. Create Virtual Environment
python -m venv venv

Activate environment (Windows):

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run Notebook

Open the file:

notebooks/sentiment_analysis.ipynb

Then:

Select the virtual environment kernel
Run all cells sequentially from top to bottom
Configuration (config.json)

All model parameters are externalized in config.json to avoid hardcoding.

It includes:

Random seed for reproducibility
Train-test split ratio (e.g., 0.2)
Maximum vocabulary size (e.g., 5000)
Model hyperparameters for:
Logistic Regression
Naive Bayes

This ensures modularity and easy tuning.

Methodology
Text Preprocessing
Lowercasing text
Cleaning raw legal notices
Preparing structured input for vectorization
Feature Engineering

Two approaches were used:

Bag of Words (BoW) → word frequency representation
TF-IDF → weighted importance of words
Machine Learning Models

Two classifiers were trained:

Logistic Regression (linear model, strong with TF-IDF)
Multinomial Naive Bayes (efficient probabilistic model for text)
Results Overview
Model	Feature Type	Accuracy	F1 Score	Training Time
Naive Bayes	BoW	1.00	1.00	Very Fast
Naive Bayes	TF-IDF	1.00	1.00	Very Fast
Logistic Regression	BoW	1.00	1.00	Fast
Logistic Regression	TF-IDF	1.00	1.00	Moderate
Key Insights
Dataset contains highly distinguishable vocabulary across classes
Both models achieve strong performance due to clear separability
Naive Bayes is more computationally efficient
Logistic Regression provides stable performance with TF-IDF
Experiment Tracking

MLflow was used to track experiments including:

Accuracy per run
F1-score per configuration
Multiple training runs for comparison

This ensures reproducibility and structured model evaluation.

Limitations
Small dataset size
No deep learning models used
Limited real-world noise in data
Future Improvements
Integration of transformer-based models (BERT, RoBERTa)
Deployment as a web API
Larger and more diverse dataset
Hyperparameter optimization (Grid/Random search)
Author Note

This project was developed as part of a machine learning lab assignment focusing on text classification, NLP preprocessing, and experiment tracking using MLflow.

Conclusion

The system successfully demonstrates how traditional machine learning techniques can effectively classify legal documents with high accuracy when trained on clean and structured data.

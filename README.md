📄 README.md (LAB SUBMISSION VERSION)
🧠 Legal Notice Classification, Sentiment Lab 68629
🚀 Project Description

This project is a multi-class text classification system developed to categorize legal notices into three classes:

Contract Dispute
Intellectual Property Claim
Regulatory Compliance

The system is built using traditional NLP and machine learning techniques and compares the performance of:

Logistic Regression
Naive Bayes

with two feature representations:

Bag of Words (BoW)
TF-IDF

The objective is to evaluate model performance on structured legal text data.

📊 Dataset Information

The dataset contains the following columns:

id
category
label (target class)
notice (raw legal text)
Class Distribution:
Contract Dispute
Intellectual Property Claim
Regulatory Compliance
⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/aroojnaaz/sentiment-lab-68629.git
2. Create Virtual Environment
python -m venv venv

Activate (Windows):

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run Notebook

Open:

notebooks/sentiment_analysis.ipynb

Run all cells sequentially.

⚙️ Configuration (config.json)

All hyperparameters are stored in config.json:

Random seed = 42
Test size = 0.2
Max features = 5000
Model parameters for:
Logistic Regression
Naive Bayes

This ensures reproducibility and modular design.

🧪 Methodology
1. Preprocessing
Lowercasing text
Cleaning raw notices
Removing noise
2. Feature Extraction
Bag of Words (BoW)
Word frequency based representation
TF-IDF
Weighted importance of words
3. Models Used
Logistic Regression
Multinomial Naive Bayes
📊 Results Summary (FROM YOUR LAB)
Model	Features	Accuracy	F1 Score
Naive Bayes	BoW	1.0	1.0
Naive Bayes	TF-IDF	1.0	1.0
Logistic Regression	BoW	1.0	1.0
Logistic Regression	TF-IDF	1.0	1.0
📌 Observations
Both models achieved high performance due to strong vocabulary separation
TF-IDF slightly improves interpretability
Naive Bayes is faster in training and inference
Logistic Regression provides stable classification
🧾 MLflow Experiment Tracking

MLflow was used to:

Track multiple runs
Log accuracy and F1-score
Compare model performance

At least 6 runs were logged successfully.

⚠️ Limitations
Small dataset size
No deep learning models
Limited real-world noise
🚀 Future Improvements
Transformer-based models (BERT)
Larger dataset
Hyperparameter tuning
Deployment as API
👩‍💻 Author

This project was completed as part of a Machine Learning Lab assignment.

GitHub Repository:
👉 https://github.com/aroojnaaz/sentiment-lab-68629

📌 Conclusion

This project demonstrates effective classification of legal notices using traditional NLP techniques and machine learning models, achieving strong performance on structured data.

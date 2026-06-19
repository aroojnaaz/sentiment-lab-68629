from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


def extract_features(df: pd.DataFrame, text_column: str = "text") -> tuple[CountVectorizer, pd.DataFrame]:
    """Convert preprocessed text into bag-of-words features."""
    vectorizer = CountVectorizer(max_features=1000, stop_words="english")
    X = vectorizer.fit_transform(df[text_column].astype(str))
    feature_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    return vectorizer, feature_df

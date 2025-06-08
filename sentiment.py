import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
from src.utils import label_sentiment

def train_model(df, model_path):
    df['sentiment'] = df['headline'].apply(label_sentiment)
    X = df['headline']
    y = df['sentiment']

    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('clf', LogisticRegression(max_iter=200))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, model_path)
    print("Model trained and saved.")

def predict_headline(headline, model_path):
    model = joblib.load(model_path)
    return model.predict([headline])[0]

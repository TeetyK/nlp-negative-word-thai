from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from src.token import thai_tokenizer
import pandas as pd
import joblib

def train(df:pd.DataFrame):
    model_pipeline = Pipeline([
        ('tfidf',TfidfVectorizer(tokenizer=thai_tokenizer)),
        ('clf',LogisticRegression())
    ])

    model_pipeline.fit(df['text'],df['labels'])

    joblib.dump(model_pipeline,'.\\models\\sentiment.pkl')
    print("Model Save")

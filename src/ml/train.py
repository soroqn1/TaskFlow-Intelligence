import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import os

def train_and_save_model():
    data_path = "data/train_data.csv"
   
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found!")
        return

    model_path = "data/model.joblib"

    df = pd.read_csv(data_path)
    
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])
    
    print("Training model...")
    pipeline.fit(df['task_description'], df['priority'])
    
    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model()
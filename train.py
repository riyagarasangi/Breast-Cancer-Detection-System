import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier
import joblib


file_path = r"F:\3rd year\ai\mini project\project_new\data.xlsx"
df = pd.read_excel(file_path)


if 'id' in df.columns:
    df = df.drop(columns=['id'])

label_encoder = LabelEncoder()
df['diagnosis'] = label_encoder.fit_transform(df['diagnosis'])

X = df.drop(columns=['diagnosis'])
y = df['diagnosis']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


model = GradientBoostingClassifier(random_state=42)
model.fit(X_train, y_train)


model_path = r"F:\3rd year\ai\mini project\project_new\breast_cancer_model.pkl"
joblib.dump(model, model_path)
print(f"Model saved at {model_path}")

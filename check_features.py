import pandas as pd

file_path = "../data.xlsx"
df = pd.read_excel(file_path)

if 'id' in df.columns:
    df = df.drop(columns=['id'])

X = df.drop(columns=['diagnosis'])  # Assuming 'diagnosis' is the target column
print(X.columns.tolist())

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline



from src.data.preprocess import create_preprocessor


df=pd.read_csv("data/cleaned/cleaned_data.csv")

X = df.drop(["Loan_Approved", "Unnamed: 0"], axis=1)
y = df["Loan_Approved"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

numerical_columns=X.select_dtypes(include="number").columns

categorical_columns=X.select_dtypes(include="object").columns
print(numerical_columns,categorical_columns)

preprocessor=create_preprocessor(
    numerical_columns,categorical_columns
)
dt=DecisionTreeClassifier(
    criterion='gini',
    max_depth= 5,
 min_samples_leaf= 4,
 min_samples_split= 2
)
model=Pipeline([
    ("prepocessor",preprocessor),
    ("model",dt)
])

model.fit(X_train,y_train)

with open("models/model_pipeline.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model Trained Successsfully")
print("Model Saved Successfully !")

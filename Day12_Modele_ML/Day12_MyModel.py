import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "heures_etude": [5, 1, 8, 2, 6, 3, 7, 4],
    "absences": [2, 10, 0, 5, 1, 7, 0, 3],
    "moyenne": [12, 8, 15, 10, 14, 9, 16, 11],
    "reussi": [1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)


X = df[["heures_etude", "absences", "moyenne"]]
y = df["reussi"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy :", accuracy)
print("y_test :", y_test.values)
print("predictions :", predictions)
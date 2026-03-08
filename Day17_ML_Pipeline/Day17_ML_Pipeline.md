# 📘 Day 17 — ML Pipelines (Scikit-Learn)

## 🎯 Objectif

Comprendre le concept de **Machine Learning Pipeline** et pourquoi il est utilisé dans les projets ML réels.

Un pipeline permet d'organiser toutes les étapes du Machine Learning dans **un workflow propre et reproductible**.

Sources :

- Scikit-learn Documentation
  https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html

---

# 1️⃣ Le problème sans Pipeline

Dans un projet Machine Learning classique, plusieurs étapes sont nécessaires.

```text
Dataset
 ↓
Feature Scaling
 ↓
Feature Engineering
 ↓
Train Model
 ↓
Prediction
```

Si on code chaque étape séparément, le code devient rapidement difficile à maintenir.

---

# 2️⃣ Exemple sans Pipeline

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

scaler = StandardScaler()
model = LogisticRegression()

scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)

model.fit(X_train_scaled, y_train)
```

Pour tester :

```python
X_test_scaled = scaler.transform(X_test)
predictions = model.predict(X_test_scaled)
```

### Problèmes

- code plus long
- risque d'erreurs
- difficile à reproduire

---

# 3️⃣ Solution : ML Pipeline

Un **Pipeline** permet de chaîner plusieurs étapes dans un seul objet.

Workflow :

```text
Data
 ↓
Preprocessing
 ↓
Feature Engineering
 ↓
Model
```

---

# 4️⃣ Structure d’un Pipeline

Un pipeline contient plusieurs étapes :

```python
Pipeline([
    ("step1", transformer),
    ("step2", transformer),
    ("model", estimator)
])
```

Chaque étape peut être :

| Type           | Exemple            |
| -------------- | ------------------ |
| Transformation | StandardScaler     |
| Encodage       | OneHotEncoder      |
| Modèle         | LogisticRegression |

---

# 5️⃣ Exemple simple de Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)
```

Documentation :
https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html

---

# 6️⃣ Cross Validation avec Pipeline

Les pipelines fonctionnent directement avec la validation croisée.

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(pipeline, X, y, cv=5)

print(scores)
```

Source :
https://scikit-learn.org/stable/modules/cross_validation.html

---

# 7️⃣ Exemple Pipeline plus complet

Pipeline avec plusieurs étapes :

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ("imputer", SimpleImputer()),
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier())
])

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)
```

---

# 8️⃣ Schéma mental

```text
Pipeline

Data
 ↓
Transformations
 ↓
Feature Engineering
 ↓
Model
 ↓
Prediction
```

---

# 📊 Avantages des Pipelines

| Sans Pipeline          | Avec Pipeline       |
| ---------------------- | ------------------- |
| Code désorganisé       | Code propre         |
| Risque de data leakage | workflow sécurisé   |
| difficile à maintenir  | facile à reproduire |

---

# 🧠 Mini exercice

On veut créer un pipeline avec :

- StandardScaler
- LogisticRegression

Quelle est la bonne structure ?

### A

```python
Pipeline([
("model", LogisticRegression()),
("scaler", StandardScaler())
])
```

### B

```python
Pipeline([
("scaler", StandardScaler()),
("model", LogisticRegression())
])
```

Explique pourquoi.

---

# 📚 Sources

Scikit-learn Documentation
https://scikit-learn.org/stable/

Scikit-learn Pipeline
https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html

Ramadan Tech Challenge 🌙\
Jour 17 --  ML Pipelines 

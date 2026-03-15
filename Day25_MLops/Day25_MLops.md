# 📘 Day 25 — MLOps — Déploiement de Modèles ML

## 🎯 Objectif

Comprendre **MLOps** — la discipline qui permet de **déployer, surveiller et maintenir des modèles de Machine Learning en production**.

Concepts étudiés :

* Définition MLOps
* ML en recherche vs ML en production
* Composantes MLOps
* MLOps Pipeline
* Outils MLOps
* Servir un modèle avec FastAPI
* Model Monitoring

Sources :

* Google — *Practitioners Guide to MLOps*
  https://cloud.google.com/resources/mlops-whitepaper
* MLflow Documentation
  https://mlflow.org/docs/latest/index.html

---

# 1️⃣ C'est quoi MLOps ?

**MLOps** (Machine Learning Operations) est une discipline qui combine :

* Machine Learning
* DevOps
* Data Engineering

Objectif :

> Déployer et maintenir des modèles ML en production de manière **fiable**, **reproductible** et **scalable**.

---

## Le problème sans MLOps

Dans la réalité des projets ML :

```text
Data Scientist → entraîne un modèle dans un notebook
↓
"Ça marche sur ma machine"
↓
En production → erreurs, données différentes, performances dégradées
```

MLOps résout ce problème.

---

# 2️⃣ ML en recherche vs ML en production

| Aspect         | ML en recherche         | ML en production          |
| -------------- | ----------------------- | ------------------------- |
| Objectif       | Explorer, expérimenter  | Servir des prédictions    |
| Données        | Statiques               | Dynamiques, en temps réel |
| Environnement  | Notebook local          | Serveur cloud             |
| Reproductible  | Pas toujours            | Obligatoire               |
| Monitoring     | Non                     | Obligatoire               |

Un modèle en production doit :

* répondre rapidement
* être disponible 24/7
* gérer les erreurs
* être surveillé en continu

---

# 3️⃣ Les composantes MLOps

Un système MLOps complet contient plusieurs blocs :

---

## 🗄️ Data Versioning

Versionner les données utilisées pour l'entraînement.

Outil : **DVC (Data Version Control)**

```text
Code versionné avec Git
Données versionnées avec DVC
```

---

## 🏋️ Model Training

Entraînement reproductible avec tracking des expériences.

Outil : **MLflow**

```python
import mlflow

mlflow.log_param("learning_rate", 0.01)
mlflow.log_metric("accuracy", 0.92)
mlflow.sklearn.log_model(model, "model")
```

---

## 📦 Model Registry

Stocker et versionner les modèles entraînés.

```text
Model v1 → accuracy 85%
Model v2 → accuracy 90%
Model v3 → accuracy 92% ← Production
```

---

## 🚀 Model Serving

Exposer le modèle via une **API REST** pour que d'autres systèmes puissent l'utiliser.

Outil : **FastAPI**

---

## 📊 Model Monitoring

Surveiller le comportement du modèle en production.

---

# 4️⃣ MLOps Pipeline

Voici le pipeline complet d'un projet MLOps :

```text
Data Collection
      ↓
Data Versioning (DVC)
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Experiment Tracking (MLflow)
      ↓
Model Registry
      ↓
Model Serving (FastAPI / Docker)
      ↓
Model Monitoring
      ↓
Retrain si nécessaire
```

Ce cycle est **continu** — comme le cycle DevOps.

---

# 5️⃣ Outils MLOps

| Outil        | Rôle                             |
| ------------ | -------------------------------- |
| MLflow       | Tracking des expériences         |
| DVC          | Versioning des données           |
| FastAPI      | Servir le modèle via API         |
| Docker       | Conteneuriser le modèle          |
| Kubernetes   | Orchestrer le déploiement        |
| Prometheus   | Monitoring des métriques         |
| Grafana      | Visualisation du monitoring      |

---

# 6️⃣ Exemple — Servir un modèle avec FastAPI

Voici comment exposer un modèle ML via une API REST.

---

## Étape 1 — Entraîner et sauvegarder le modèle

```python
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, random_state=42)

model = LogisticRegression()
model.fit(X, y)

# Sauvegarder le modèle
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
```

---

## Étape 2 — Créer l'API avec FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Charger le modèle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Définir le schéma d'entrée
class InputData(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: InputData):
    X = np.array(data.features).reshape(1, -1)
    prediction = model.predict(X)
    probability = model.predict_proba(X).max()

    return {
        "prediction": int(prediction[0]),
        "probability": round(float(probability), 4)
    }
```

---

## Étape 3 — Lancer l'API

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## Étape 4 — Faire une prédiction

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [0.5, -1.2, 0.3, 1.1, ...]}'
```

Réponse :

```json
{
  "prediction": 1,
  "probability": 0.9231
}
```

---

## Étape 5 — Conteneuriser avec Docker

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build et run :

```bash
docker build -t ml-model-api .
docker run -p 8000:8000 ml-model-api
```

---

# 7️⃣ Model Monitoring

Déployer un modèle ne suffit pas. Il faut le **surveiller en continu**.

---

## Data Drift

Les données en production changent avec le temps.

```text
Modèle entraîné sur : données 2023
Production en 2025 → données différentes
→ performance dégradée
```

---

## Concept Drift

La relation entre les features et la cible change.

Exemple :

```text
Modèle de prédiction de prix immobilier
Entraîné avant une crise économique
Après la crise → les patterns changent
```

---

## Ce qu'il faut surveiller

| Métrique              | Description                         |
| --------------------- | ----------------------------------- |
| Accuracy en prod      | Performance réelle                  |
| Distribution des inputs | Vérifier si les données ont changé |
| Latence API           | Temps de réponse                    |
| Erreurs               | Taux d'erreurs de l'API             |

---

## Solution : Retrain automatique

Quand les performances chèvent sous un seuil :

```text
Monitoring détecte dégradation
        ↓
Alerte déclenchée
        ↓
Retraining automatique
        ↓
Nouveau modèle déployé
```

---

# 8️⃣ Bonnes pratiques Senior

✔ Toujours versionner les données **et** le code\
✔ Tracker chaque expérience (paramètres, métriques, modèle)\
✔ Containeriser le modèle avec Docker\
✔ Exposer via API REST (FastAPI)\
✔ Monitorer en production (data drift, concept drift)\
✔ Automatiser le retraining si nécessaire\
✔ Utiliser un Model Registry pour gérer les versions

---

# 🧠 Mini exercice

Un modèle de classification est déployé en production.

Après 3 mois, l'accuracy passe de **92%** à **74%**.

Questions :

1️⃣ Qu'est-ce qui peut expliquer cette dégradation ?\
2️⃣ Comment détecter ce problème automatiquement ?\
3️⃣ Quelle solution mettre en place ?

---

# 📚 Sources

Google Cloud
*Practitioners Guide to MLOps*
https://cloud.google.com/resources/mlops-whitepaper

MLflow Documentation
https://mlflow.org/docs/latest/index.html

FastAPI Documentation
https://fastapi.tiangolo.com/

Ramadan Tech Challenge 🌙\
Jour 25 — MLOps — Déploiement de Modèles ML 🚀
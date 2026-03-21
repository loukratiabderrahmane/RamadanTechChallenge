# 📘 Day 30 — Projet Final : Student Score Predictor

## 🎯 Objectif

Clôturer le **Ramadan Tech Challenge** en construisant un projet complet qui mobilise les concepts clés des 29 jours précédents.

Le projet **Student Score Predictor** est la suite directe du **Jour 12** — un modèle Logistic Regression de 30 lignes transformé en une vraie plateforme ML déployée en production.

---

# 1️⃣ Rappel — Le modèle du Jour 12

Au Jour 12, on avait écrit ceci :

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
```

C'était un script standalone de **30 lignes**.

Au Jour 30, ce même modèle est devenu une **plateforme complète** avec API REST, dashboard React, et Docker.

---

# 2️⃣ Architecture du projet

```text
Frontend (React + Vite + Tailwind)
            ↓ HTTP
     FastAPI Backend
            ↓
ML Pipeline (StandardScaler + Logistic Regression)
            ↓
  Réponse JSON (score + verdict + conseil)
```

Structure complète :

```text
student-score-predictor/
├── backend/
│   ├── app/
│   │   ├── main.py        ← FastAPI entry point
│   │   └── routes.py      ← ML model + endpoints
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── PredictPage.jsx
│   │   │   ├── HistoryPage.jsx
│   │   │   └── ModelPage.jsx
│   │   └── lib/api.js
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 3️⃣ Le modèle ML — Pipeline Scikit-Learn

Par rapport au Jour 12, on ajoute un **StandardScaler** dans un **Pipeline** (Jour 17) :

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

model = Pipeline([
    ("scaler", StandardScaler()),
    ("clf",    LogisticRegression(random_state=42, max_iter=1000)),
])

model.fit(X_train, y_train)
```

Le **StandardScaler** normalise les features (mean=0, std=1) pour éviter que le modèle soit biaisé par l'échelle des variables.

---

# 4️⃣ Déploiement via FastAPI (Jour 25)

Le modèle est entraîné **directement au démarrage** de l'API :

```python
@router.post("/predict")
def predict(body: PredictRequest):
    features = np.array([[body.heures_etude, body.absences, body.moyenne]])
    proba    = model.predict_proba(features)[0]
    label    = int(model.predict(features)[0])

    return {
        "reussi":         label == 1,
        "reussite_proba": round(float(proba[1]) * 100, 1),
        "verdict":        "Excellent" if proba[1] >= 0.75 else "Encourageant",
        "conseil":        "Continue comme ça !" if label == 1 else "Plus d'efforts nécessaires.",
    }
```

---

# 5️⃣ API REST (Jour 26)

| Méthode | Route | Description |
| ------- | ----- | ----------- |
| POST | /predict | Prédire la réussite |
| GET | /history | Historique des prédictions |
| GET | /stats | Statistiques globales |
| GET | /model-info | Informations sur le modèle |
| GET | /health | Status de l'API |
| GET | /docs | Documentation Swagger |

---

# 6️⃣ Docker + Docker Compose (Jour 03)

```yaml
services:
  api:
    build: ./backend
    ports:
      - "8000:8000"

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - VITE_API_TARGET=http://api:8000
    depends_on:
      - api
```

Lancement en une commande :

```bash
docker-compose up --build
```

---

# 📊 Concepts du challenge utilisés dans ce projet

| Concept | Jour |
| ------- | ---- |
| Docker + Docker Compose | 03 |
| Machine Learning — Supervised Learning | 11 |
| Logistic Regression + premier modèle | 12 |
| Classification Algorithms | 13 |
| Model Evaluation — Accuracy, Precision, Recall | 14 |
| Overfitting vs Underfitting | 15 |
| Feature Engineering — StandardScaler | 16 |
| ML Pipelines — Scikit-Learn Pipeline | 17 |
| MLOps — déploiement FastAPI | 25 |
| REST API avancée | 26 |

---

# 🔄 La progression en 30 jours

```text
Jour 12 :  30 lignes Python · script standalone
    ↓
Jour 17 :  + StandardScaler · ML Pipeline propre
    ↓
Jour 25 :  + FastAPI · modèle en production
    ↓
Jour 30 :  + React · Docker · REST API · projet complet ✅
```

---

# 🚀 Projet complet

Le code source complet est disponible ici :

**👉 [github.com/loukratiabderrahmane/student-score-predictor](https://github.com/loukratiabderrahmane/student-score-predictor)**

```bash
git clone https://github.com/loukratiabderrahmane/student-score-predictor.git
cd student-score-predictor
docker-compose up --build
```

- Frontend → **http://localhost:3000**
- API Docs → **http://localhost:8000/docs**

---

# 🏁 Conclusion du Challenge

```text
Jour 01  →  Sécurité Backend
Jour 03  →  Docker
Jour 05  →  CI/CD
Jour 09  →  ORM
Jour 12  →  Premier modèle ML  ←  origine de ce projet
Jour 18  →  Deep Learning
Jour 24  →  RAG
Jour 25  →  MLOps
Jour 30  →  Projet en production ✅
```

30 jours. 30 concepts. 1 projet livré.

En un mois, tu es passé de "comment sécuriser une API" à "déployer un système ML complet en production".

C'est exactement la mentalité d'un ingénieur senior :

> **Comprendre les fondations. Assembler les briques. Livrer quelque chose de réel.**

---

Ramadan Tech Challenge 🌙  
Jour 30 — Projet Final : Student Score Predictor 🎓
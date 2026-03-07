# 📘 Day 16 — Feature Engineering

## 🎯 Objectif

Comprendre **Feature Engineering**, une étape fondamentale du Machine Learning.

Beaucoup de performances des modèles ne viennent pas seulement des algorithmes, mais de la **qualité des features (variables)** utilisées.

Concepts étudiés :

* Qu'est-ce qu'une feature
* Feature Engineering
* Feature Scaling
* Encoding des variables catégorielles
* Normalization / Standardization

Sources principales :

* Scikit-learn Documentation
  https://scikit-learn.org/stable/
* Géron, Aurélien — *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*

---

# 1️⃣ Qu’est-ce qu’une Feature ?

Une **feature** est une **variable utilisée par un modèle pour faire une prédiction**.

Exemple dataset :

| Age | Income | Buy Product |
| --- | ------ | ----------- |
| 25  | 2000   | No          |
| 40  | 6000   | Yes         |

Features :

```text
Age
Income
```

Target :

```text
Buy Product
```

Les features sont les **informations utilisées pour prédire la cible**.

---

# 2️⃣ Feature Engineering

Le **Feature Engineering** consiste à :

> transformer les données brutes en variables utiles pour le modèle.

Cela peut inclure :

* transformation
* création de nouvelles variables
* normalisation
* encodage

Source :
Aurélien Géron — *Hands-On Machine Learning*

---

# Exemple simple

Dataset :

| Birth Year | Current Year |
| ---------- | ------------ |
| 1998       | 2025         |

Feature créée :

```text
Age = Current Year - Birth Year
```

Nouvelle table :

| Age |
| --- |
| 27  |

On a créé **une meilleure feature**.

---

# 3️⃣ Feature Scaling

Certains modèles sont sensibles à l’échelle des données.

Exemple :

| Feature | Valeur |
| ------- | ------ |
| Age     | 25     |
| Salary  | 100000 |

Le salaire domine les calculs.

Solution :

**Feature Scaling**

---

# 4️⃣ Normalization

La **normalisation** transforme les valeurs entre **0 et 1**.

Formule :

[
X' = \frac{X - X_{min}}{X_{max} - X_{min}}
]

Exemple :

| Valeur | Normalisée |
| ------ | ---------- |
| 10     | 0          |
| 20     | 0.5        |
| 30     | 1          |

Documentation :

https://scikit-learn.org/stable/modules/preprocessing.html

---

# 5️⃣ Standardization

La **standardisation** transforme les données pour avoir :

```text
mean = 0
standard deviation = 1
```

Formule :

[
X' = \frac{X - \mu}{\sigma}
]

où :

* μ = moyenne
* σ = écart-type

---

# Exemple Python

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

Source :

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html

---

# 6️⃣ Encoding des variables catégorielles

Les modèles ML travaillent avec des **nombres**, pas du texte.

Exemple :

| City   |
| ------ |
| Paris  |
| London |
| Madrid |

On doit transformer ces valeurs.

---

# One-Hot Encoding

Transformation :

| City   | Paris | London | Madrid |
| ------ | ----- | ------ | ------ |
| Paris  | 1     | 0      | 0      |
| London | 0     | 1      | 0      |
| Madrid | 0     | 0      | 1      |

---

# Exemple Python

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()

X_encoded = encoder.fit_transform(X)
```

Documentation :

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html

---

# 📊 Pourquoi Feature Engineering est important ?

Dans beaucoup de projets ML :

```text
Performance du modèle
=
Qualité des features
+
Algorithme
```

Un bon feature engineering peut améliorer fortement les résultats.

Source :

Aurélien Géron — *Hands-On Machine Learning*

---

# ⚙️ Exemple pipeline simple

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X_train, y_train)
```

Documentation :

https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html

---

# 🧠 Mini exercice

Dataset :

| Age | Salary | City   |
| --- | ------ | ------ |
| 25  | 3000   | Paris  |
| 40  | 6000   | London |

Questions :

1️⃣ Quelle feature doit être **encodée** ?
2️⃣ Pourquoi faire **feature scaling** ?
3️⃣ Quelle technique utiliser pour transformer **City** ?

---

# 📚 Sources

Scikit-learn Documentation
https://scikit-learn.org/stable/

Aurélien Géron
*Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*

Ramadan Tech Challenge 🌙\
Jour 16 --  Feature Engineering

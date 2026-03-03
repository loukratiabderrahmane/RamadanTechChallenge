# 📘 Jour 13 — Classification Algorithms

## 🎯 Objectif

Comprendre les **algorithmes de classification** les plus utilisés en Machine Learning :

* Logistic Regression
* Decision Tree
* Random Forest

Ces modèles permettent de **prédire une catégorie (classe)** à partir de données.

---

# 1️⃣ Qu’est-ce qu’un problème de classification ?

Un problème de **classification** consiste à prédire **une catégorie**.

### Exemple 1 — Spam Email

| Email            | Classe   |
| ---------------- | -------- |
| Win money now    | Spam     |
| Meeting tomorrow | Not Spam |

Le modèle doit prédire :

```
Spam = 1
Not Spam = 0
```

---

### Exemple 2 — Achat produit

| Age | Income | Buy Product |
| --- | ------ | ----------- |
| 25  | 2000   | No          |
| 40  | 6000   | Yes         |

Le modèle doit prédire si la personne **achètera le produit**.

---

# 2️⃣ Logistic Regression

Malgré son nom, **Logistic Regression est utilisée pour la classification**.

### Principe

Le modèle calcule une **probabilité entre 0 et 1**.

Formule :

[
P(y=1|x)=\frac{1}{1+e^{-z}}
]

avec

[
z = w_0 + w_1x_1 + w_2x_2 + ...
]

Cette fonction s'appelle **Sigmoid Function**.

---

### Sigmoid Function

Elle transforme n’importe quel nombre en valeur entre **0 et 1**.

| z  | Sigmoid(z) |
| -- | ---------- |
| -3 | 0.04       |
| 0  | 0.5        |
| 3  | 0.95       |

Décision finale :

```
si P > 0.5  → classe 1
si P < 0.5  → classe 0
```

---

### Exemple Python

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

Documentation :
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

---

# 3️⃣ Decision Tree

Un **Decision Tree** fonctionne comme **un arbre de décision**.

Chaque nœud pose une question.

### Exemple

```
        Age < 30 ?
        /       \
      Yes       No
  Income < 3000 ?
    /         \
   No         Yes
```

---

### Comment l’arbre choisit les questions ?

Le modèle utilise une mesure appelée **impureté**.

Les plus utilisées :

* **Gini Impurity**
* **Entropy (Information Gain)**

Documentation :
https://scikit-learn.org/stable/modules/tree.html

---

### Exemple Python

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

---

# 4️⃣ Random Forest

Le problème des Decision Trees :

Ils peuvent **overfit** (mémoriser les données).

Solution :

**Random Forest**

Principe :

Créer **plusieurs arbres de décision** puis faire un vote.

```
Tree 1 → Yes
Tree 2 → Yes
Tree 3 → No
Tree 4 → Yes
Tree 5 → Yes

Résultat final = Yes
```

Cette technique s'appelle **Ensemble Learning**.

Source scientifique :

Breiman, L. (2001).
Random Forests. Machine Learning Journal.
https://link.springer.com/article/10.1023/A:1010933404324

---

### Exemple Python

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

Documentation :
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

---

# ⚖️ Comparaison des modèles

| Modèle              | Avantages       | Inconvénients   |
| ------------------- | --------------- | --------------- |
| Logistic Regression | Simple, rapide  | Modèle linéaire |
| Decision Tree       | Interprétable   | Overfitting     |
| Random Forest       | Très performant | Plus lourd      |

---

# 📌 Quand utiliser chaque modèle ?

### Logistic Regression

* Classification simple
* Relations linéaires

### Decision Tree

* Modèle interprétable
* Décisions logiques

### Random Forest

* Données complexes
* Meilleure précision

---


# 📚 Sources

Scikit-learn Documentation
https://scikit-learn.org/stable/

Breiman, L. (2001). Random Forests
Machine Learning Journal
https://link.springer.com/article/10.1023/A:1010933404324

Ramadan Tech Challenge 🌙\
Jour 13 -- Classification Algorithms

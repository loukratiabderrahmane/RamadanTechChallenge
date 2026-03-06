# 📘 Day 15 — Overfitting vs Underfitting

## 🎯 Objectif

Comprendre pourquoi un modèle de Machine Learning peut **mal généraliser** sur de nouvelles données.

Concepts étudiés :

* Underfitting
* Overfitting
* Bias vs Variance
* Train / Test Split
* Techniques pour éviter l’overfitting

Sources principales :

* Scikit-learn Documentation
  https://scikit-learn.org/stable/
* Hastie, Tibshirani, Friedman — *The Elements of Statistical Learning*
* Christopher M. Bishop — *Pattern Recognition and Machine Learning*

---

# 🧠 1️⃣ Le vrai objectif du Machine Learning

Quand on entraîne un modèle :

```
Données d'entraînement → modèle → prédictions
```

Mais l’objectif réel est :

👉 **Prédire correctement de nouvelles données**

Cela s'appelle :

**Generalization**

Un bon modèle doit fonctionner :

* sur **les données d'entraînement**
* sur **des données jamais vues**

---

# 2️⃣ Underfitting

## Définition

Un modèle est **underfitting** lorsqu’il est **trop simple pour capturer les patterns des données**.

Résultat :

* mauvaise performance sur **train**
* mauvaise performance sur **test**

---

## Exemple

Données réelles :

```
•      •
   •
      •
```

Modèle trop simple :

```
---------
```

Le modèle **ne comprend pas la structure des données**.

---

## Causes

Underfitting peut apparaître si :

* le modèle est trop simple
* pas assez de features
* pas assez d'entraînement
* trop de régularisation

---

# 3️⃣ Overfitting

## Définition

Un modèle est **overfitting** lorsqu’il **mémorise les données d’entraînement** au lieu d’apprendre les patterns.

Résultat :

* excellente performance sur **train**
* mauvaise performance sur **test**

---

## Exemple

Données :

```
•   •     •
   •
     •
```

Modèle trop complexe :

```
~^~~^~^~~^~
```

Le modèle **s’adapte exactement à chaque point**.

Mais il ne généralise pas.

---

# ⚖️ Comparaison

| Situation    | Train Error | Test Error |
| ------------ | ----------- | ---------- |
| Underfitting | élevé       | élevé      |
| Bon modèle   | faible      | faible     |
| Overfitting  | très faible | élevé      |

---

# 4️⃣ Bias vs Variance

Ces concepts expliquent l’underfitting et l’overfitting.

---

## Bias

Le **bias** correspond à l’erreur due à un modèle **trop simple**.

Caractéristiques :

* modèle rigide
* incapable d’apprendre la complexité des données

Lien :

```
High Bias → Underfitting
```

---

## Variance

La **variance** mesure la sensibilité du modèle aux données d'entraînement.

Caractéristiques :

* modèle très complexe
* s'adapte trop aux données

Lien :

```
High Variance → Overfitting
```

---

## Tableau résumé

| Concept       | Signification        |
| ------------- | -------------------- |
| High Bias     | modèle trop simple   |
| High Variance | modèle trop complexe |

---

# 5️⃣ Train / Test Split

Pour évaluer un modèle correctement, on sépare les données.

```
Dataset
   ↓
Train set
Test set
```

Exemple courant :

```
80% Train
20% Test
```

Le modèle apprend sur **Train** et est évalué sur **Test**.

---

## Exemple Python

Source : Scikit-learn documentation

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Documentation :

https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

---

# 6️⃣ Comment éviter Overfitting

### 1️⃣ Plus de données

Plus de données améliore la généralisation du modèle.

---

### 2️⃣ Simplifier le modèle

Exemple :

```
Random Forest → Decision Tree
```

---

### 3️⃣ Regularization

Limiter la complexité du modèle.

Exemples :

* L1 Regularization
* L2 Regularization

---

### 4️⃣ Cross Validation

Diviser les données plusieurs fois pour mieux évaluer le modèle.

Documentation :

https://scikit-learn.org/stable/modules/cross_validation.html

---

# 📊 Exemple réel

```
Train accuracy = 99%
Test accuracy = 60%
```

👉 Cela indique un **overfitting**.

---

# 🧠 Mini exercice

Un modèle donne :

```
Train accuracy = 55%
Test accuracy = 53%
```

Questions :

1. Est-ce Overfitting ou Underfitting ?
2. Pourquoi ?

---

# 📚 Sources

Scikit-learn Documentation
https://scikit-learn.org/stable/

Hastie, Tibshirani, Friedman
*The Elements of Statistical Learning*

Christopher M. Bishop
*Pattern Recognition and Machine Learning*

Ramadan Tech Challenge 🌙\
Jour 15 -- Overfitting vs Underfitting

# 📘 Jour 12 --- ML Model

------------------------------------------------------------------------

# 🧰 Les Outils Utilisés

## 🐍 1) Python

Langage de programmation utilisé pour écrire le modèle.

------------------------------------------------------------------------

## 📊 2) Pandas

Bibliothèque pour manipuler les données sous forme de tableau
(DataFrame).

Exemple :

``` python
import pandas as pd
df = pd.DataFrame(data)
```

Elle permet : - Structurer les données - Séparer les colonnes -
Manipuler les datasets facilement

------------------------------------------------------------------------

## 🤖 3) Scikit-Learn (sklearn)

Bibliothèque de Machine Learning en Python.

Elle contient : - Des modèles ML - Des outils de séparation train/test -
Des métriques d'évaluation

Modules utilisés :

``` python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
```

------------------------------------------------------------------------

# 📊 Le Problème

Prédire si un étudiant va :

-   Réussir (1)
-   Échouer (0)

C'est une classification binaire.

------------------------------------------------------------------------

# 🧠 Train / Test Split (Très Important)

Pourquoi séparer ?

Si on entraîne et teste sur les mêmes données : → Le modèle peut
mémoriser → Le score sera faux

Donc on fait :

-   80% → Train (apprentissage)
-   20% → Test (examen)

Code :

``` python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
```

### 📌 random_state = 42

Permet d'avoir toujours la même séparation. Sans lui, le résultat change
à chaque exécution.

------------------------------------------------------------------------

# 🤖 Logistic Regression (Explication Simple)

Le modèle calcule un score mathématique :

score = a*(heures) + b*(absences) + c\*(moyenne) + d

Les coefficients (a, b, c, d) sont appris pendant fit().

------------------------------------------------------------------------

## 🔵 La Fonction Sigmoid

Le score peut être n'importe quel nombre.

On applique donc la fonction Sigmoid pour obtenir :

Une valeur entre 0 et 1.

Cela devient une probabilité.

------------------------------------------------------------------------

## 🎯 Décision Finale

Si probabilité ≥ 0.5 → 1\
Sinon → 0

------------------------------------------------------------------------

# 🔵 fit() et predict()

## 1) fit()

``` python
model.fit(X_train, y_train)
```

Le modèle apprend les poids. C'est la phase d'apprentissage.

------------------------------------------------------------------------

## 2) predict()

``` python
predictions = model.predict(X_test)
```

Le modèle utilise ce qu'il a appris pour deviner.

------------------------------------------------------------------------

# 📈 Accuracy

``` python
accuracy = accuracy_score(y_test, predictions)
```

Accuracy = (Bonnes prédictions) / (Total)

Exemple :

3 bonnes réponses sur 4 → 75%

------------------------------------------------------------------------

# ⚠️ Pourquoi 100% Accuracy ne veut rien dire ici ?

Dans notre exemple :

-   Dataset très petit
-   Test set très petit

Accuracy = 1.0 signifie juste : → 2 bonnes réponses sur 2

Ce n'est pas représentatif d'un vrai modèle.

------------------------------------------------------------------------

# ⚠️ Overfitting

## 📌 Définition

Le modèle mémorise les données au lieu de comprendre le pattern général.

------------------------------------------------------------------------

## 🎯 Symptôme

Train accuracy = 100%\
Test accuracy = faible

------------------------------------------------------------------------

## 🧠 Causes

-   Peu de données
-   Modèle trop complexe
-   Trop de paramètres
-   Données bruitées

------------------------------------------------------------------------

## 🛠 Solutions

-   Utiliser un modèle plus simple
-   Ajouter plus de données
-   Nettoyer les données
-   Utiliser la régularisation

Exemple :

``` python
LogisticRegression(C=1.0)
```

C petit → modèle plus simple\
C grand → modèle plus flexible

------------------------------------------------------------------------

# 🏁 Résumé Final

Aujourd'hui tu comprends :

-   La logique complète d'un modèle ML
-   Le rôle de Scikit-Learn
-   Pourquoi séparer Train/Test
-   Comment fonctionne Logistic Regression
-   Ce qu'est l'Accuracy
-   Ce qu'est l'Overfitting

------------------------------------------------------------------------

Ramadan Tech Challenge 🌙\
Jour 12 -- Mon Premier Mode ML

# 📘 Jour 11 — Machine Learning

## 1️⃣ C’est quoi le Machine Learning ?

Le Machine Learning est une sous-partie de l’Intelligence Artificielle.

Au lieu de programmer des règles, on laisse la machine apprendre à partir des données.

---

## 2️⃣ Les 3 Types de Machine Learning

### 🔹 Supervised Learning
Données + réponses (labels).

Exemples :
- Classification (chat / chien)
- Régression (prix d’une maison)

### 🔹 Unsupervised Learning
Données sans réponses.

Exemple :
- Clustering (segmentation clients)

### 🔹 Reinforcement Learning
Apprentissage par récompense.

Exemple :
- IA qui joue aux jeux vidéo

---

## 3️⃣ Pipeline ML

1. Collecte des données  
2. Nettoyage  
3. Choix du modèle  
4. Entraînement  
5. Test  
6. Déploiement  

---

## 4️⃣ Concepts Importants

### 1️⃣ Dataset

#### 📌 Définition
Un Dataset est un ensemble de données utilisées pour entraîner un modèle.

C’est le carburant du Machine Learning.

Sans données → pas de Machine Learning.

#### 📊 Exemple

| Heures étude | Absences | Moyenne | Réussi |
|--------------|----------|---------|--------|
| 5            | 2        | 12      | 1      |
| 1            | 10       | 8       | 0      |
| 8            | 0        | 15      | 1      |

Ce tableau complet représente le Dataset.

---

### 2️⃣ Features

#### 📌 Définition
Les Features sont les variables d’entrée.  
Ce sont les informations utilisées pour faire la prédiction.

👉 Ce sont les colonnes explicatives.

#### 🎯 Dans notre exemple

Features :
- Heures étude  
- Absences  
- Moyenne  

En notation ML :

X = [heures, absences, moyenne]

---

### 3️⃣ Label

#### 📌 Définition
Le Label est la variable cible à prédire.

C’est la réponse que l’on veut obtenir.

#### 🎯 Dans notre exemple

Label = "Réussi"

- 1 = Oui  
- 0 = Non  

En notation ML :

y = [1, 0, 1]

---

### 4️⃣ Training Set

#### 📌 Définition
Le Training Set est la partie des données utilisée pour entraîner le modèle.

En général :  
70% à 80% des données.

#### 🎯 Exemple

Si on a 100 étudiants :

- 80 → Training  
- 20 → Test  

Le modèle apprend uniquement sur les 80.

---

### 5️⃣ Test Set

#### 📌 Définition
Le Test Set est utilisé pour évaluer les performances du modèle.

⚠️ Le modèle ne doit jamais voir ces données pendant l'entraînement.  
Sinon → Data Leakage (triche).

#### 🎯 Exemple

On entraîne sur 80 étudiants.  
On teste sur 20 étudiants inconnus.

---

### 6️⃣ Overfitting

#### 📌 Définition
Overfitting = quand le modèle apprend trop parfaitement les données d’entraînement.

Il mémorise au lieu de comprendre les patterns.

#### ⚠️ Résultat
- 100% accuracy en training  
- Mauvais résultat en test  

#### 🧠 Exemple simple

Un étudiant qui mémorise toutes les réponses exactes  
mais ne comprend pas la matière.

À l’examen avec nouvelles questions → il échoue.

C’est exactement l’overfitting.

---

### 7️⃣ Accuracy

#### 📌 Définition
Accuracy = pourcentage de bonnes prédictions.

Formule :

Accuracy = (nombre de bonnes prédictions) / (nombre total de prédictions)

#### 🎯 Exemple

Sur 20 étudiants testés :

- 16 corrects  
- 4 incorrects  

Accuracy = 16 / 20 = 0.8 = 80%

---

## 🧠 Résumé Global

| Concept        | Définition |
|---------------|------------|
| Dataset       | Ensemble complet des données |
| Features      | Variables d’entrée |
| Label         | Variable cible à prédire |
| Training Set  | Données pour entraîner |
| Test Set      | Données pour évaluer |
| Overfitting   | Mémorisation excessive |
| Accuracy      | Pourcentage de bonnes prédictions |

---

## 🎯 Objectif

Comprendre les bases du Machine Learning avant de passer aux algorithmes.

---

### ✅ Prochaine étape
Implémenter un modèle simple avec Scikit-Learn.
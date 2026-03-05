# 📘 Day 14 — Model Evaluation (Accuracy, Precision, Recall, F1 Score)

## 🎯 Objectif

Comprendre comment **évaluer la performance d’un modèle de Machine Learning**.

Après avoir entraîné un modèle, il est nécessaire de mesurer **la qualité de ses prédictions**.

Les métriques étudiées aujourd’hui :

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1 Score

Sources principales :
Scikit-learn Documentation
https://scikit-learn.org/stable/modules/model_evaluation.html

---

# 1️⃣ Pourquoi évaluer un modèle ?

Après l'entraînement d'un modèle :

```
Train Model → Predict → Evaluate
```

On doit répondre à la question :

**Le modèle fait-il de bonnes prédictions ?**

L’évaluation permet :

* mesurer la performance
* comparer plusieurs modèles
* améliorer le modèle

---

# 2️⃣ Confusion Matrix

La **Confusion Matrix** compare :

```
Prédictions du modèle
VS
Vraies valeurs
```

Structure :

|                 | Predicted Positive  | Predicted Negative  |
| --------------- | ------------------- | ------------------- |
| Actual Positive | True Positive (TP)  | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN)  |

---

## Signification

### True Positive (TP)

Le modèle prédit **positif** et c'est **correct**.

Exemple :

```
Email spam → prédit spam
```

---

### True Negative (TN)

Le modèle prédit **négatif** et c'est **correct**.

```
Email normal → prédit normal
```

---

### False Positive (FP)

Le modèle prédit **positif mais c'est faux**.

```
Email normal → prédit spam
```

---

### False Negative (FN)

Le modèle prédit **négatif mais c'est faux**.

```
Email spam → prédit normal
```

---

# 3️⃣ Accuracy

Accuracy mesure **le pourcentage de prédictions correctes**.

Formule :

Accuracy = (TP + TN) / (TP + TN + FP + FN)

---

### Exemple

```
TP = 40
TN = 50
FP = 5
FN = 5
```

Total :

```
100 observations
```

Accuracy :

```
(40 + 50) / 100 = 0.90
```

```
Accuracy = 90%
```

---

# ⚠️ Limite de l’Accuracy

Si les données sont **déséquilibrées**, l’accuracy peut être trompeuse.

Exemple :

```
1000 emails
950 non spam
50 spam
```

Un modèle qui prédit toujours **non spam** aura :

```
Accuracy = 95%
```

mais il ne détecte **aucun spam**.

---

# 4️⃣ Precision

Precision répond à la question :

> Quand le modèle prédit positif, a-t-il raison ?

Formule :

```
Precision = TP / (TP + FP)
```

---

### Exemple

```
TP = 40
FP = 10
```

```
Precision = 40 / 50 = 0.80
```

```
80% des prédictions positives sont correctes
```

---

# 5️⃣ Recall

Recall répond à la question :

> Combien de vrais positifs ont été détectés ?

Formule :

```
Recall = TP / (TP + FN)
```

---

### Exemple

```
TP = 40
FN = 10
```

```
Recall = 40 / 50 = 0.80
```

---

# 6️⃣ F1 Score

Le **F1 Score** combine **Precision et Recall**.

Formule :

```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

Le F1 Score est utile lorsque les **données sont déséquilibrées**.

---

# 📊 Comparaison des métriques

| Metric    | Question                                   |
| --------- | ------------------------------------------ |
| Accuracy  | Combien de prédictions sont correctes      |
| Precision | Quand le modèle dit positif, a-t-il raison |
| Recall    | Combien de positifs ont été détectés       |
| F1 Score  | Équilibre entre Precision et Recall        |

---

# 🧪 Exemple Python (scikit-learn)

Documentation :
https://scikit-learn.org/stable/modules/model_evaluation.html

```python
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

accuracy_score(y_test, y_pred)
precision_score(y_test, y_pred)
recall_score(y_test, y_pred)
f1_score(y_test, y_pred)
```

---

# Exemple complet

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

Sortie typique :

```
precision recall f1-score support

0 0.91 0.89 0.90
1 0.87 0.90 0.88
```

---

# 🧠 Mini exercice

Un modèle donne :

```
TP = 70
FP = 30
FN = 10
TN = 90
```

Calcule :

* Accuracy
* Precision
* Recall

---

# 📚 Sources

Scikit-learn Documentation
https://scikit-learn.org/stable/modules/model_evaluation.html

Powers, D. M. W. (2011).
Evaluation: From Precision, Recall and F-measure to ROC.
Journal of Machine Learning Technologies.

Ramadan Tech Challenge 🌙\
Jour 14 --  Model Evaluation


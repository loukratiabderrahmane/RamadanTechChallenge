# 📘 Day 20 — Backpropagation & Gradient Descent

## 🎯 Objectif

Comprendre **comment les réseaux neuronaux apprennent** grâce à deux concepts fondamentaux :

* Gradient Descent
* Backpropagation

Sources :

Goodfellow, Bengio, Courville — *Deep Learning* (MIT Press, 2016)
TensorFlow Documentation
https://www.tensorflow.org/

---

# 1️⃣ Le problème : comment entraîner un réseau ?

Quand un réseau neuronal fait une prédiction :

```text
Input → Neural Network → Prediction
```

La prédiction est comparée à la vraie valeur.

Exemple :

```text
Prediction = 0.8
True value = 1
```

On calcule alors **l’erreur du modèle**.

---

# 2️⃣ Loss Function

La **fonction de perte (loss function)** mesure l'erreur du modèle.

Exemple simple :

$$
Loss = (y - \hat{y})^2
$$

où :

* (y) = vraie valeur
* (\hat{y}) = prédiction

Objectif :

```text
Minimiser la loss
```

---

# 3️⃣ Gradient Descent

Le **Gradient Descent** est un algorithme d’optimisation utilisé pour **réduire la loss**.

Principe :

```text
calculer la pente de la fonction de perte
↓
ajuster les poids du réseau
↓
réduire l'erreur
```

Formule de mise à jour :

$$
w = w - \eta \frac{\partial L}{\partial w}
$$

où :

* (w) = poids du réseau
* (\eta) = learning rate
* (L) = fonction de perte

---

# 4️⃣ Learning Rate

Le **learning rate** contrôle la vitesse d’apprentissage.

| Valeur     | Effet                   |
| ---------- | ----------------------- |
| Trop petit | apprentissage très lent |
| Trop grand | divergence possible     |

Exemple :

```text
learning_rate = 0.01
```

---

# 5️⃣ Backpropagation

La **Backpropagation** permet de calculer les gradients pour chaque poids du réseau.

Processus :

```text
Forward propagation
↓
calcul de la loss
↓
Backpropagation
↓
mise à jour des poids
```

Elle utilise la **règle de la chaîne (chain rule)** du calcul différentiel.

---

# 6️⃣ Cycle d’entraînement d’un réseau

Chaque itération suit les étapes :

```text
Input
 ↓
Forward Propagation
 ↓
Compute Loss
 ↓
Backpropagation
 ↓
Update Weights
```

Ce cycle est répété plusieurs fois.

---

# 7️⃣ Epochs

Une **epoch** correspond à un passage complet sur tout le dataset.

Exemple :

```text
dataset = 1000 samples
epochs = 10
```

Le réseau voit les données **10 fois**.

---

# 8️⃣ Exemple simple avec TensorFlow / Keras

```python
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(X_train, y_train, epochs=10)
```

---

# 9️⃣ Schéma global

```text
Data
 ↓
Forward Propagation
 ↓
Prediction
 ↓
Loss
 ↓
Backpropagation
 ↓
Update Weights
```

---

# 🧠 Mini exercice

Un modèle a :

```text
Learning rate = 0.8
```

Questions :

1️⃣ Est-ce une bonne valeur ?
2️⃣ Pourquoi un learning rate trop grand peut poser problème ?

---

# 📚 Sources

Goodfellow, Bengio, Courville
*Deep Learning* — MIT Press

TensorFlow Documentation
https://www.tensorflow.org/

Ramadan Tech Challenge 🌙\
Jour 20 --  Backpropagation & Gradient Descent 

# 📘 Day 18 — Introduction to Deep Learning

## 🎯 Objectif

Comprendre les bases du **Deep Learning** et comment fonctionnent les **réseaux de neurones artificiels**.

Concepts étudiés :

* Deep Learning
* Artificial Neural Networks
* Neuron
* Layers
* Forward propagation


---

# 1️⃣ Qu’est-ce que le Deep Learning ?

Le **Deep Learning** est une sous-discipline du Machine Learning basée sur les **réseaux de neurones artificiels avec plusieurs couches**.

Ces modèles sont capables d’apprendre des patterns complexes dans les données.

Applications :

* reconnaissance d’images
* traduction automatique
* reconnaissance vocale
* systèmes de recommandation

---

# 2️⃣ Artificial Neural Networks

Les **réseaux de neurones artificiels (ANN)** sont inspirés du cerveau humain.

Structure :

```text
Input Layer
   ↓
Hidden Layer
   ↓
Hidden Layer
   ↓
Output Layer
```

Chaque couche contient plusieurs **neurones**.

---

# 3️⃣ Le neurone artificiel

Un neurone reçoit des **inputs**, applique des **poids**, puis produit une sortie.

Formule :

$$
z = w_1 x_1 + w_2 x_2 + ... + b
$$

où :

* x = inputs
* w = poids
* b = biais

Puis on applique une **fonction d’activation**.

---

# 4️⃣ Activation Function

Les fonctions d’activation introduisent de la **non-linéarité** dans le réseau.

Exemples :

* Sigmoid
* ReLU
* Tanh

ReLU :

$$
f(x) = max(0, x)
$$

---

# 5️⃣ Structure d’un réseau neuronal

Exemple simple :

```text
Input (2 features)
   ↓
Hidden Layer (4 neurons)
   ↓
Output Layer (1 neuron)
```

---

# 6️⃣ Forward Propagation

Le processus de calcul des prédictions s'appelle :

**Forward Propagation**

```text
Input
 ↓
Hidden Layer
 ↓
Output
```

Chaque couche transforme les données.

---

# 7️⃣ Exemple simple en Python

Avec la bibliothèque **TensorFlow / Keras** :

```python
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(4, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
```

Source :

TensorFlow Documentation
https://www.tensorflow.org/

---

# 📊 Applications du Deep Learning

| Domaine            | Exemple                 |
| ------------------ | ----------------------- |
| Computer Vision    | reconnaissance d’images |
| NLP                | traduction automatique  |
| Speech Recognition | assistants vocaux       |
| Recommandation     | Netflix / Amazon        |

---

# 🧠 Mini exercice

Un réseau contient :

* 3 couches cachées
* 1 couche d'entrée
* 1 couche de sortie

Combien de couches contient ce réseau au total ?

---

# 📚 Sources

Goodfellow, Bengio, Courville
*Deep Learning* (MIT Press)

TensorFlow Documentation
https://www.tensorflow.org/

IBM AI
https://www.ibm.com/topics/deep-learning

Ramadan Tech Challenge 🌙\
Jour 18 --  Introduction to Deep Learning 

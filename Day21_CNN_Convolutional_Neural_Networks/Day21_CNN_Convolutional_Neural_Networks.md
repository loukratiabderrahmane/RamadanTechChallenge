# 📘 Day 21 — Convolutional Neural Networks (CNN)

## 🎯 Objectif

Comprendre les **Convolutional Neural Networks (CNN)** et pourquoi ils sont utilisés pour la **vision par ordinateur**.

Concepts étudiés :

* Convolution
* Filters (kernels)
* Feature maps
* Pooling
* Architecture CNN

Sources :

Goodfellow, Bengio, Courville — *Deep Learning* (MIT Press, 2016)
TensorFlow Documentation
https://www.tensorflow.org/

---

# 1️⃣ Pourquoi utiliser les CNN ?

Les réseaux neuronaux classiques (MLP) fonctionnent mal avec les images.

Exemple :

Une image **28 × 28 pixels**

```text
28 × 28 = 784 inputs
```

Si on utilise un réseau dense :

* trop de paramètres
* perte de la structure spatiale

Les CNN résolvent ce problème en utilisant des **convolutions**.

---

# 2️⃣ Convolution

Une **convolution** applique un **filtre (kernel)** sur l'image pour détecter des motifs.

Exemple de filtre :

```text
[ 1  0 -1
  1  0 -1
  1  0 -1 ]
```

Ce filtre détecte les **bords verticaux**.

---

# 3️⃣ Feature Map

Après l'application d'un filtre, on obtient une **feature map**.

```text
Image
 ↓
Convolution
 ↓
Feature Map
```

Chaque filtre détecte un type de motif :

* edges
* textures
* shapes

---

# 4️⃣ Pooling

Le **pooling** réduit la taille des feature maps.

Exemple : **Max Pooling**

```text
[2 1
 0 3]
```

Résultat :

```text
3
```

Avantages :

* réduire la dimension
* réduire le calcul
* éviter l’overfitting

---

# 5️⃣ Architecture CNN

Structure typique :

```text
Image
 ↓
Convolution
 ↓
ReLU
 ↓
Pooling
 ↓
Convolution
 ↓
Pooling
 ↓
Fully Connected Layer
 ↓
Output
```

---

# 6️⃣ Exemple simple avec TensorFlow / Keras

```python
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Conv2D(32, (3,3), activation="relu"),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Conv2D(64, (3,3), activation="relu"),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])
```

Documentation :

https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D

---

# 7️⃣ Applications des CNN

| Domaine               | Exemple                     |
| --------------------- | --------------------------- |
| Vision par ordinateur | reconnaissance d’images     |
| Voitures autonomes    | détection d’objets          |
| Médecine              | analyse d’imagerie médicale |
| Sécurité              | reconnaissance faciale      |

---

# 8️⃣ Schéma simplifié

```text
Image
 ↓
Conv Layer
 ↓
Pooling
 ↓
Conv Layer
 ↓
Pooling
 ↓
Dense Layer
 ↓
Output
```

---

# 🧠 Mini exercice

Une image fait :

```text
64 × 64 pixels
```

On applique un filtre :

```text
3 × 3
```

Question :

1️⃣ Quel est le rôle du filtre ?
2️⃣ Pourquoi utilise-t-on le pooling ?

---

# 📚 Sources

Goodfellow, Bengio, Courville
*Deep Learning* — MIT Press

TensorFlow Documentation
https://www.tensorflow.org/

Ramadan Tech Challenge 🌙\
Jour 21 -- Convolutional Neural Networks (CNN)

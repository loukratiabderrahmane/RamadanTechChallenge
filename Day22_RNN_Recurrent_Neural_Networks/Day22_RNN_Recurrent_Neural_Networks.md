# 📘 Day 22 — Recurrent Neural Networks (RNN)

## 🎯 Objectif

Comprendre les **Recurrent Neural Networks (RNN)** et pourquoi ils sont utilisés pour les **données séquentielles**.

Concepts étudiés :

* données séquentielles
* mémoire dans les réseaux
* fonctionnement d’un RNN
* problème du vanishing gradient
* variantes modernes

Sources :

Goodfellow, Bengio, Courville — *Deep Learning* (MIT Press, 2016)
TensorFlow Documentation
https://www.tensorflow.org/

---

# 1️⃣ Pourquoi les RNN ?

Certaines données sont **séquentielles**, c’est-à-dire que l’ordre des éléments est important.

Exemples :

| Type de données | Exemple            |
| --------------- | ------------------ |
| Texte           | phrases            |
| Audio           | signal vocal       |
| Finance         | séries temporelles |
| NLP             | traduction         |

Exemple phrase :

```text
I love machine learning
```

Chaque mot dépend des mots précédents.

---

# 2️⃣ Problème des réseaux classiques

Les réseaux neuronaux classiques (MLP) ne gardent **aucune mémoire**.

Ils traitent chaque entrée indépendamment :

```text
Input → Network → Output
```

Mais pour le texte il faut se souvenir du **contexte précédent**.

---

# 3️⃣ Principe des RNN

Les RNN introduisent une **mémoire interne**.

Chaque sortie dépend :

* de l’entrée actuelle
* de l’état précédent

Schéma :

```text
x1 → h1 → y1
      ↓
x2 → h2 → y2
      ↓
x3 → h3 → y3
```

où :

* (x) = input
* (h) = hidden state
* (y) = output

---

# 4️⃣ Fonctionnement mathématique

À chaque étape :

$$
h_t = f(Wx_t + Uh_{t-1} + b)
$$

où :

* (x_t) = entrée actuelle
* (h_{t-1}) = état précédent
* (W, U) = matrices de poids
* (f) = fonction d’activation

---

# 5️⃣ Exemple simple

Phrase :

```text
I love AI
```

Traitement :

```text
Word 1 → I
Word 2 → love
Word 3 → AI
```

Le réseau garde l’information des mots précédents.

---

# 6️⃣ Problème du Vanishing Gradient

Les RNN simples souffrent d’un problème appelé :

**Vanishing Gradient**

Lors de l'entraînement :

```text
gradient → devient très petit
```

Conséquence :

* difficulté à apprendre des dépendances longues.

Source : Goodfellow et al., *Deep Learning*.

---

# 7️⃣ Solutions modernes

Pour résoudre ce problème, des architectures avancées ont été créées :

| Architecture | Description            |
| ------------ | ---------------------- |
| LSTM         | Long Short Term Memory |
| GRU          | Gated Recurrent Unit   |

Ces modèles permettent de mieux gérer la mémoire.

---

# 8️⃣ Exemple simple avec TensorFlow

```python
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.SimpleRNN(32, return_sequences=True),
    keras.layers.SimpleRNN(32),
    keras.layers.Dense(10, activation="softmax")
])
```

Documentation :

https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN

---

# 9️⃣ Applications des RNN

| Domaine  | Exemple                |
| -------- | ---------------------- |
| NLP      | traduction automatique |
| Chatbots | conversation           |
| Finance  | prévision des marchés  |
| Speech   | reconnaissance vocale  |

---

# 🔟 Schéma simplifié

```text
Input sequence
 ↓
RNN layer
 ↓
RNN layer
 ↓
Output
```

---

# 🧠 Mini exercice

Une phrase contient :

```text
5 mots
```

Questions :

1️⃣ Combien d’étapes le RNN doit-il traiter ?
2️⃣ Pourquoi la mémoire est-elle importante pour comprendre une phrase ?

---

# 📚 Sources

Goodfellow, Bengio, Courville
*Deep Learning* — MIT Press

TensorFlow Documentation
https://www.tensorflow.org/

Ramadan Tech Challenge 🌙\
Jour 22 --  Recurrent Neural Networks (RNN)

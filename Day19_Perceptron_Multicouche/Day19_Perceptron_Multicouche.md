# 📘 Day 19 — Perceptron Multicouche (PMC / MLP)

## 🎯 Objectif

Comprendre le **Perceptron Multicouche (PMC)**, appelé en anglais **Multilayer Perceptron (MLP)**.

Le PMC est un type de **réseau de neurones artificiel composé de plusieurs couches** qui permet d'apprendre des relations **non linéaires complexes**.

Sources :

* Goodfellow, Bengio, Courville — *Deep Learning* (MIT Press, 2016)
* Scikit-learn Documentation
  https://scikit-learn.org/stable/modules/neural_networks_supervised.html

---

# 1️⃣ Qu’est-ce que le Perceptron Multicouche ?

Le **Perceptron Multicouche (PMC)** est un réseau de neurones composé de :

* une couche d’entrée
* une ou plusieurs couches cachées
* une couche de sortie

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

Contrairement au **Perceptron simple**, le PMC peut modéliser des **relations non linéaires**.

---

# 2️⃣ Structure d’un PMC

Un réseau PMC est constitué de **neurones organisés en couches**.

Exemple :

```text
Input (3 neurones)
   ↓
Hidden Layer (5 neurones)
   ↓
Hidden Layer (4 neurones)
   ↓
Output (1 neurone)
```

Chaque neurone reçoit des entrées, applique des **poids**, puis produit une sortie.

---

# 3️⃣ Calcul dans un neurone

Chaque neurone calcule une combinaison linéaire :

$$
z = \sum_{i=1}^{n} w_i x_i + b
$$

où :

* (x_i) = inputs
* (w_i) = poids
* (b) = biais

Puis une **fonction d’activation** est appliquée.

---

# 4️⃣ Fonctions d’activation

Les fonctions d’activation introduisent de la **non-linéarité** dans le réseau.

### ReLU

$$
f(x) = \max(0, x)
$$

Très utilisée dans les réseaux modernes.

---

### Sigmoid

$$
f(x) = \frac{1}{1 + e^{-x}}
$$

Utilisée pour la **classification binaire**.

---

### Tanh

$$
f(x) = \tanh(x)
$$

Sortie entre **-1 et 1**.

---

# 5️⃣ Forward Propagation

Le calcul des prédictions dans un réseau de neurones s'appelle :

**Forward Propagation**

Processus :

```text
Input
 ↓
Hidden Layer
 ↓
Hidden Layer
 ↓
Output
```

Chaque couche effectue :

$$
z = W \cdot x + b
$$

Puis :

```text
activation(z)
```

---

# 6️⃣ Exemple de réseau simple

Supposons un réseau :

```text
2 neurones d'entrée
↓
3 neurones cachés
↓
1 neurone de sortie
```

Schéma :

```text
x1   x2
 \   /
  \ /
 [h1 h2 h3]
     ↓
   output
```

---

# 7️⃣ Exemple Python avec Scikit-Learn

La bibliothèque **scikit-learn** fournit une implémentation du MLP.

Documentation officielle :
https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html

```python
from sklearn.neural_network import MLPClassifier

model = MLPClassifier(
    hidden_layer_sizes=(10,5),
    activation="relu",
    max_iter=1000
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

---

# 8️⃣ Pourquoi le PMC est important ?

Le Perceptron Multicouche est la base de nombreux modèles de **Deep Learning**.

Applications :

* classification
* systèmes de recommandation
* prédiction de données complexes
* analyse d’images
* NLP (Natural Language Processing)

---

# 📊 Comparaison des modèles

| Modèle                 | Capacité                 |
| ---------------------- | ------------------------ |
| Perceptron simple      | relations linéaires      |
| Perceptron multicouche | relations non linéaires  |
| Deep Neural Networks   | relations très complexes |

---

# 🧠 Mini exercice

Un réseau contient :

* 4 neurones d’entrée
* 2 couches cachées (6 neurones chacune)
* 1 neurone de sortie

Questions :

1️⃣ Combien de **couches** contient ce réseau ?
2️⃣ Combien de **neurones cachés au total** ?

---

# 📚 Sources

Goodfellow, Bengio, Courville
*Deep Learning* — MIT Press
https://www.deeplearningbook.org/

Scikit-learn Documentation
https://scikit-learn.org/stable/modules/neural_networks_supervised.html

Ramadan Tech Challenge 🌙\
Jour 19 --  Perceptron Multicouche 

# 📘 Day 23 — Transformer & Attention Mechanism

## 🎯 Objectif

Comprendre l'architecture **Transformer** et le mécanisme **Attention**,
qui sont à la base des modèles modernes comme **ChatGPT**, **BERT**, et **GPT-4**.

Concepts étudiés :

* Limites des RNN
* Mécanisme d'Attention
* Self-Attention
* Architecture Transformer
* Encoder / Decoder

Sources :

* Vaswani et al. — *Attention Is All You Need* (2017)
* Goodfellow, Bengio, Courville — *Deep Learning* (MIT Press, 2016)
* Hugging Face Documentation
  https://huggingface.co/docs/transformers

---

# 1️⃣ Pourquoi les Transformers ?

Les **RNN** (vus au Day 22) ont deux problèmes majeurs :

| Problème | Description |
| -------- | ----------- |
| Vanishing Gradient | difficulté à apprendre des dépendances longues |
| Traitement séquentiel | lent, impossible à paralléliser |

Exemple :

```text
Phrase : "Le chat que j'ai vu hier dans le jardin mange."

RNN doit traiter mot par mot
→ difficulté à relier "chat" et "mange"
```

Les **Transformers** résolvent ces deux problèmes.

---

# 2️⃣ L'idée clé : Attention

Le mécanisme d'**Attention** permet au modèle de se concentrer sur
les mots les plus importants d'une phrase.

Exemple :

```text
"Le chat mange la souris."
```

Pour prédire le prochain mot après "mange" :

```text
→ le modèle prête attention à "chat" (sujet)
→ et à "souris" (objet)
```

Au lieu de lire séquentiellement, le modèle regarde **toute la phrase en même temps**.

---

# 3️⃣ Self-Attention (Attention propre)

Le **Self-Attention** permet à chaque mot de la phrase de regarder
tous les autres mots et de mesurer leur importance.

Schéma :

```text
"Je mange une pomme"

  Je    mange   une   pomme
  ↓       ↓      ↓      ↓
chaque mot regarde tous les autres
et calcule un score d'attention
```

---

# 4️⃣ Calcul du Self-Attention (simplifié)

Chaque mot est transformé en 3 vecteurs :

| Vecteur | Rôle |
| ------- | ---- |
| **Q** (Query) | Ce que je cherche |
| **K** (Key) | Ce que je contiens |
| **V** (Value) | Ce que j'apporte |

Formule :

```text
Attention(Q, K, V) = softmax( QK^T / √d_k ) × V
```

Étapes :

```text
1. Calculer les scores (Q × K)
2. Normaliser avec softmax
3. Multiplier par V pour obtenir la sortie
```

Source : Vaswani et al., *Attention Is All You Need*, 2017.

---

# 5️⃣ Multi-Head Attention

Au lieu d'un seul mécanisme d'attention,
les Transformers utilisent **plusieurs têtes d'attention en parallèle**.

```text
Head 1 → regarde la relation sujet/verbe
Head 2 → regarde la relation nom/adjectif
Head 3 → regarde le contexte général
...
```

Chaque tête apprend un aspect différent de la phrase.

---

# 6️⃣ Architecture Transformer

L'architecture Transformer originale (2017) est composée de :

```text
Input
 ↓
Embedding + Positional Encoding
 ↓
[Encoder Block × N]
 ↓
[Decoder Block × N]
 ↓
Output
```

---

## 🔵 Encoder

L'**Encoder** lit la phrase d'entrée et la comprend.

Composition :

```text
Multi-Head Attention
 ↓
Feed Forward Network
 ↓
Layer Normalization
```

---

## 🟢 Decoder

Le **Decoder** génère la sortie mot par mot.

Composition :

```text
Masked Multi-Head Attention
 ↓
Cross-Attention (avec l'Encoder)
 ↓
Feed Forward Network
 ↓
Layer Normalization
```

---

# 7️⃣ Positional Encoding

Les Transformers traitent tous les mots **en parallèle**.

Problème : ils ne savent pas l'ordre des mots.

Solution : **Positional Encoding**

On ajoute à chaque mot un vecteur qui encode sa position.

```text
mot[0] + position[0]
mot[1] + position[1]
mot[2] + position[2]
```

---

# 8️⃣ GPT vs BERT

Les deux modèles sont basés sur les Transformers mais diffèrent :

| Modèle | Type | Utilisation |
| ------ | ---- | ----------- |
| **BERT** | Encoder only | Compréhension du texte |
| **GPT** | Decoder only | Génération de texte |
| **T5** | Encoder + Decoder | Traduction, résumé |

---

## Comment ChatGPT fonctionne (simplifié)

```text
1. Input tokenisé
 ↓
2. Embedding
 ↓
3. Plusieurs couches Transformer (Decoder)
 ↓
4. Chaque couche applique Self-Attention
 ↓
5. Le modèle prédit le prochain token
 ↓
6. Répète jusqu'à la fin de la réponse
```

---

# 9️⃣ Exemple Python avec Hugging Face

La bibliothèque **Hugging Face Transformers** donne accès
aux modèles pré-entraînés.

```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

result = generator("Le machine learning est", max_length=50)

print(result[0]["generated_text"])
```

Documentation :
https://huggingface.co/docs/transformers

---

# 📊 Comparaison RNN vs Transformer

| Aspect | RNN | Transformer |
| ------ | --- | ----------- |
| Traitement | Séquentiel | Parallèle |
| Mémoire longue | Difficile | Facile (Attention) |
| Vitesse | Lent | Rapide |
| Scalabilité | Limité | Très bon |

---

# 🧠 Mini exercice

Une phrase contient :

```text
"L'étudiant qui a travaillé dur a réussi son examen."
```

Questions :

1️⃣ Quel mécanisme permet de relier "étudiant" et "réussi" malgré la distance ?
2️⃣ Pourquoi le RNN aurait du mal avec cette phrase ?
3️⃣ Quelle est la différence entre BERT et GPT ?

---

# 🏁 Résumé

| Concept | Définition |
| ------- | ---------- |
| Attention | Mécanisme pour pondérer l'importance des mots |
| Self-Attention | Chaque mot regarde tous les autres |
| Multi-Head Attention | Plusieurs mécanismes d'attention en parallèle |
| Positional Encoding | Encode l'ordre des mots |
| Encoder | Comprend l'entrée |
| Decoder | Génère la sortie |

---

# 📚 Sources

Vaswani et al.
*Attention Is All You Need* — 2017
https://arxiv.org/abs/1706.03762

Goodfellow, Bengio, Courville
*Deep Learning* — MIT Press

Hugging Face Documentation
https://huggingface.co/docs/transformers

---

Ramadan Tech Challenge 🌙\
Jour 23 — Transformer & Attention Mechanism 🚀
# 📘 Day 24 — RAG (Retrieval Augmented Generation)

## 🎯 Objectif

Comprendre le concept de **RAG (Retrieval Augmented Generation)** et pourquoi il est utilisé dans les applications AI modernes.

Concepts étudiés :

* Limites des LLM classiques
* Qu'est-ce que le RAG
* Architecture RAG
* Vector Search
* Exemple pratique

Sources :

* Lewis et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020)
  https://arxiv.org/abs/2005.11401
* Hugging Face Documentation
  https://huggingface.co/docs/transformers
* LangChain Documentation
  https://python.langchain.com/

---

# 1️⃣ Le problème des LLM classiques

Un modèle comme **GPT** a été entraîné sur des données jusqu'à une certaine date.

Problèmes :

| Problème | Description |
| -------- | ----------- |
| Knowledge cutoff | Le modèle ne connaît pas les événements récents |
| Hallucination | Le modèle invente des réponses |
| Données privées | Le modèle ne connaît pas vos documents internes |

Exemple :

```text
Question : "Quel est le contenu de mon contrat PDF ?"
GPT classique : ❌ Ne peut pas répondre
```

---

# 2️⃣ Solution : RAG

Le **RAG** permet de connecter un LLM à une **base de connaissances externe**.

Principe :

```text
Question utilisateur
 ↓
Recherche dans les documents
 ↓
Envoi du contexte au LLM
 ↓
Réponse basée sur les documents
```

---

# 3️⃣ Architecture RAG

L'architecture RAG se divise en deux phases :

## Phase 1 — Indexation (une seule fois)

```text
Documents (PDF, texte, web...)
 ↓
Chunking (découpage en morceaux)
 ↓
Embedding (transformation en vecteurs)
 ↓
Stockage dans Vector Database
```

## Phase 2 — Requête (à chaque question)

```text
Question utilisateur
 ↓
Embedding de la question
 ↓
Recherche des chunks similaires (Vector Search)
 ↓
Contexte envoyé au LLM
 ↓
Réponse finale
```

---

# 4️⃣ Qu'est-ce qu'un Embedding ?

Un **Embedding** transforme un texte en **vecteur numérique**.

Exemple :

```text
"Le chat mange"  →  [0.12, 0.87, 0.34, ...]
"Le chien court" →  [0.11, 0.23, 0.91, ...]
```

Des phrases similaires ont des vecteurs **proches** dans l'espace.

---

# 5️⃣ Vector Search

La **recherche vectorielle** trouve les documents les plus proches
d'une question donnée.

```text
Question : "Quels sont mes droits dans le contrat ?"
 ↓
Embedding de la question → vecteur Q
 ↓
Comparaison avec tous les vecteurs dans la DB
 ↓
Retourne les 3 chunks les plus similaires
```

La mesure utilisée : **Cosine Similarity**

```text
similarity = cos(angle entre les deux vecteurs)
→ 1 = identiques
→ 0 = complètement différents
```

---

# 6️⃣ Chunking

Avant d'indexer les documents, on les **découpe en morceaux (chunks)**.

Pourquoi ?

* Les LLM ont une limite de tokens
* On veut récupérer uniquement la partie pertinente

Exemple :

```text
Document PDF de 50 pages
 ↓
Découpage en chunks de 500 tokens
 ↓
200 chunks indexés dans la Vector DB
```

---

# 7️⃣ Exemple Python avec LangChain

```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# 1. Charger le document
loader = PyPDFLoader("contrat.pdf")
documents = loader.load()

# 2. Découper en chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)

# 3. Créer les embeddings et stocker
vectorstore = Chroma.from_documents(
    chunks,
    OpenAIEmbeddings()
)

# 4. Créer la chaîne RAG
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=vectorstore.as_retriever()
)

# 5. Poser une question
answer = qa_chain.run("Quels sont mes droits ?")
print(answer)
```

Documentation LangChain :
https://python.langchain.com/docs/use_cases/question_answering/

---

# 8️⃣ Vector Databases populaires

| Base | Description |
| ---- | ----------- |
| **ChromaDB** | Open source, simple, local |
| **Pinecone** | Cloud, scalable, managed |
| **Weaviate** | Open source, powerful |
| **FAISS** | Meta, très rapide, local |

---

# 9️⃣ RAG vs Fine-tuning

| Aspect | RAG | Fine-tuning |
| ------ | --- | ----------- |
| Mise à jour des données | Facile | Réentraînement nécessaire |
| Coût | Faible | Élevé |
| Données privées | ✅ Oui | ✅ Oui |
| Précision | Bonne | Très bonne |
| Cas d'usage | Documents dynamiques | Comportement spécifique |

---

# 🔟 Schéma global RAG

```text
[Documents]
     ↓
  Chunking
     ↓
  Embedding
     ↓
[Vector DB]
     ↑
  Question
     ↓
Vector Search
     ↓
  Context
     ↓
   [LLM]
     ↓
  Réponse
```

---

# 🧠 Mini exercice

Tu as un PDF de 100 pages.

Tu veux créer un chatbot qui répond aux questions sur ce PDF.

Questions :

1️⃣ Quelles sont les étapes pour indexer ce document ?
2️⃣ Pourquoi fait-on du chunking avant l'embedding ?
3️⃣ Quelle est la différence entre RAG et demander directement au LLM ?

---

# 📊 Résumé

| Concept | Définition |
| ------- | ---------- |
| RAG | Connecter un LLM à des documents externes |
| Embedding | Transformer du texte en vecteur |
| Chunking | Découper les documents en morceaux |
| Vector Search | Trouver les documents les plus pertinents |
| Vector DB | Base de données pour stocker les vecteurs |

---

# 📚 Sources

Lewis et al.
*Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*
https://arxiv.org/abs/2005.11401

LangChain Documentation
https://python.langchain.com/

Hugging Face Documentation
https://huggingface.co/docs/transformers

---

Ramadan Tech Challenge 🌙\
Jour 24 — RAG (Retrieval Augmented Generation) 🚀
# 📘 Day 26 — APIs REST Avancées & GraphQL

## 🎯 Objectif

Comprendre les **APIs REST avancées** et **GraphQL**, deux approches fondamentales pour concevoir des APIs modernes.

Concepts étudiés :

* Rappel REST & bonnes pratiques avancées
* Versioning d'API
* Pagination, Filtrage, Tri
* Introduction à GraphQL
* REST vs GraphQL
* Quand utiliser l'un ou l'autre

Sources :

* Roy Fielding — *Architectural Styles and the Design of Network-based Software Architectures* (2000)
* GraphQL Documentation — https://graphql.org/learn/
* RESTful API Design — https://restfulapi.net/

---

# 1️⃣ Rappel : Qu'est-ce qu'une API REST ?

Une **API REST (Representational State Transfer)** est un style architectural pour concevoir des APIs web basées sur HTTP.

Principes fondamentaux :

```text
Client → HTTP Request → Server → HTTP Response
```

Les méthodes HTTP principales :

| Méthode | Action          |
| ------- | --------------- |
| GET     | Lire            |
| POST    | Créer           |
| PUT     | Modifier (tout) |
| PATCH   | Modifier (partiel) |
| DELETE  | Supprimer       |

---

# 2️⃣ REST Avancé — Bonnes Pratiques

## Nommage des routes

Toujours utiliser des **noms**, jamais des verbes.

```text
✅ GET /users
✅ POST /users
✅ GET /users/:id
✅ DELETE /users/:id

❌ GET /getUsers
❌ POST /createUser
```

## Codes HTTP appropriés

| Code | Signification         |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 204  | No Content            |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 500  | Internal Server Error |

---

# 3️⃣ Versioning d'API

Le **versioning** permet de faire évoluer une API sans casser les clients existants.

## Approches courantes

### 1. URL versioning (la plus utilisée)

```text
GET /api/v1/users
GET /api/v2/users
```

### 2. Header versioning

```text
GET /api/users
Accept: application/vnd.myapp.v2+json
```

### 3. Query parameter

```text
GET /api/users?version=2
```

La méthode **URL versioning** est la plus lisible et la plus répandue.

---

# 4️⃣ Pagination

Sans pagination → une requête peut retourner **des millions de résultats**.

## Offset-based pagination (classique)

```text
GET /users?page=2&limit=10
```

Réponse :

```json
{
  "data": [...],
  "page": 2,
  "limit": 10,
  "total": 150
}
```

## Cursor-based pagination (moderne, performant)

```text
GET /users?cursor=eyJpZCI6MTB9&limit=10
```

Avantage : plus performant sur de très grandes tables.

---

# 5️⃣ Filtrage & Tri

## Filtrage

```text
GET /users?role=admin&status=active
```

## Tri

```text
GET /users?sort=createdAt&order=desc
```

## Sélection de champs

```text
GET /users?fields=id,name,email
```

Permet de réduire la taille des réponses.

---

# 6️⃣ Introduction à GraphQL

**GraphQL** est un langage de requête pour les APIs, développé par Facebook en 2015.

Au lieu d'avoir de multiples endpoints :

```text
REST :
GET /users
GET /users/:id/posts
GET /users/:id/followers
```

GraphQL utilise **un seul endpoint** :

```text
POST /graphql
```

Et le client demande **exactement** ce dont il a besoin.

---

# 7️⃣ Concepts GraphQL

## Schema

Le **schéma** définit les types de données disponibles.

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post]
}

type Post {
  id: ID!
  title: String!
  content: String!
}
```

## Query

Le client demande ce qu'il veut :

```graphql
query {
  user(id: "1") {
    name
    email
    posts {
      title
    }
  }
}
```

Réponse :

```json
{
  "data": {
    "user": {
      "name": "Alice",
      "email": "alice@example.com",
      "posts": [
        { "title": "Mon premier article" }
      ]
    }
  }
}
```

## Mutation

Pour créer ou modifier des données :

```graphql
mutation {
  createUser(name: "Bob", email: "bob@example.com") {
    id
    name
  }
}
```

## Subscription

Pour les données **temps réel** :

```graphql
subscription {
  newMessage(channelId: "1") {
    content
    author
  }
}
```

---

# 8️⃣ Avantages de GraphQL

### 1. No Over-fetching

REST :

```json
// GET /users/1
{
  "id": 1,
  "name": "Alice",
  "email": "...",
  "address": "...",
  "phone": "...",   ← données inutiles
  "createdAt": "..."  ← données inutiles
}
```

GraphQL :

```graphql
query {
  user(id: "1") {
    name   ← seulement ce dont on a besoin
  }
}
```

### 2. No Under-fetching

REST → plusieurs requêtes pour récupérer des données liées.

GraphQL → **une seule requête** pour tout.

---

# 9️⃣ Exemple Node.js — REST vs GraphQL

## REST (Express)

```javascript
// Routes multiples
app.get('/users', getUsers);
app.get('/users/:id', getUserById);
app.get('/users/:id/posts', getUserPosts);
```

## GraphQL (Apollo Server)

```javascript
const { ApolloServer, gql } = require('apollo-server');

const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    posts: [Post]
  }

  type Post {
    id: ID!
    title: String!
  }

  type Query {
    user(id: ID!): User
    users: [User]
  }
`;

const resolvers = {
  Query: {
    user: (_, { id }) => getUserById(id),
    users: () => getAllUsers(),
  },
  User: {
    posts: (user) => getPostsByUserId(user.id),
  },
};

const server = new ApolloServer({ typeDefs, resolvers });
```

Documentation : https://www.apollographql.com/docs/apollo-server/

---

# 📊 REST vs GraphQL

| Aspect             | REST                    | GraphQL                  |
| ------------------ | ----------------------- | ------------------------ |
| Endpoints          | Multiples               | Un seul                  |
| Over-fetching      | Possible                | Éliminé                  |
| Under-fetching     | Possible                | Éliminé                  |
| Typage             | Non natif               | Natif (Schema)           |
| Cache              | Facile (HTTP cache)     | Plus complexe            |
| Courbe d'apprentissage | Faible             | Moyenne                  |
| Idéal pour         | APIs simples, publiques | Apps complexes, mobiles  |

---

# 🔟 Quand utiliser REST vs GraphQL ?

## Utiliser REST si :

* API publique simple
* Cache HTTP important
* Équipe peu familière avec GraphQL
* Ressources bien définies

## Utiliser GraphQL si :

* Application mobile (économiser la bande passante)
* Besoins clients variés et complexes
* Relations entre données nombreuses
* Équipe frontend avec besoins flexibles

---

# 🎓 Bonnes pratiques Senior

✔ Toujours versionner les APIs REST  
✔ Implémenter la pagination sur toutes les listes  
✔ Utiliser les bons codes HTTP  
✔ Documenter avec Swagger/OpenAPI (REST) ou GraphiQL (GraphQL)  
✔ Sécuriser avec Authentication + Rate Limiting  
✔ Ne pas exposer les détails internes dans les messages d'erreur  

---

# 🧠 Mini exercice

Tu construis une app mobile qui affiche :
- Le nom de l'utilisateur
- Ses 3 derniers posts
- Le nombre de followers

Questions :

1️⃣ Combien de requêtes REST sont nécessaires ?  
2️⃣ Comment GraphQL résout-il ce problème en une seule requête ?  
3️⃣ Écris la query GraphQL correspondante.

---

# 📚 Sources

Roy Fielding — *Architectural Styles and the Design of Network-based Software Architectures*  
https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm

GraphQL Official Documentation  
https://graphql.org/learn/

Apollo Server Documentation  
https://www.apollographql.com/docs/apollo-server/

RESTful API Design  
https://restfulapi.net/

---

Ramadan Tech Challenge 🌙  
Jour 26 — APIs REST Avancées & GraphQL 🚀
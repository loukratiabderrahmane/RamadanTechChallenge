# 📘 Day 27 — Sécurité Avancée : OAuth2, JWT & Zero Trust

## 🎯 Objectif

Comprendre les mécanismes de **sécurité avancée** utilisés dans les applications modernes.

Concepts étudiés :

* OAuth2 — Délégation d'autorisation
* JWT (JSON Web Token) — Authentification stateless
* Refresh Tokens
* Zero Trust Architecture
* Bonnes pratiques sécurité senior

Sources :

* RFC 6749 — The OAuth 2.0 Authorization Framework
  https://datatracker.ietf.org/doc/html/rfc6749
* RFC 7519 — JSON Web Token (JWT)
  https://datatracker.ietf.org/doc/html/rfc7519
* NIST Special Publication 800-207 — Zero Trust Architecture
  https://csrc.nist.gov/publications/detail/sp/800-207/final

---

# 1️⃣ Rappel : Authentification vs Autorisation

Deux concepts souvent confondus :

| Concept        | Question                        | Exemple                     |
| -------------- | ------------------------------- | --------------------------- |
| Authentification | Qui es-tu ?                   | Login avec email/password   |
| Autorisation   | Qu'as-tu le droit de faire ?   | Accéder à /admin uniquement |

---

# 2️⃣ JWT — JSON Web Token

## Définition

Un **JWT** est un token compact et auto-suffisant qui contient des informations signées.

Il permet d'authentifier un utilisateur **sans stocker de session côté serveur** (stateless).

## Structure d'un JWT

Un JWT est composé de 3 parties séparées par des points `.` :

```text
header.payload.signature
```

### 1. Header

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

### 2. Payload (Claims)

```json
{
  "sub": "user_123",
  "name": "Alice",
  "role": "admin",
  "iat": 1710000000,
  "exp": 1710003600
}
```

Claims importants :

| Claim | Signification         |
| ----- | --------------------- |
| sub   | Subject (ID user)     |
| iat   | Issued At (création)  |
| exp   | Expiration            |
| role  | Rôle de l'utilisateur |

### 3. Signature

```text
HMACSHA256(
  base64(header) + "." + base64(payload),
  secret_key
)
```

La signature garantit que le token **n'a pas été modifié**.

---

## Flux JWT

```text
1. User → Login (email + password)
2. Server → Vérifie credentials
3. Server → Génère JWT signé
4. Client → Stocke le JWT
5. Client → Envoie JWT dans chaque requête (Header Authorization)
6. Server → Vérifie la signature → Autorise
```

## Exemple Node.js

```javascript
const jwt = require('jsonwebtoken');

// Générer un token
const token = jwt.sign(
  { sub: user.id, role: user.role },
  process.env.JWT_SECRET,
  { expiresIn: '1h' }
);

// Vérifier un token
const decoded = jwt.verify(token, process.env.JWT_SECRET);
```

---

# 3️⃣ Refresh Tokens

## Problème

Un Access Token avec une longue durée de vie est dangereux.

Si volé → l'attaquant a accès pendant des heures / jours.

## Solution : Refresh Token

```text
Access Token  → durée courte (15min - 1h)
Refresh Token → durée longue (7j - 30j)
```

## Flux

```text
1. Login → Access Token (15min) + Refresh Token (7j)
2. Client utilise Access Token pour les requêtes
3. Access Token expire
4. Client envoie Refresh Token → nouveau Access Token
5. Si Refresh Token expire → Re-login obligatoire
```

```javascript
// Renouveler l'access token
app.post('/auth/refresh', (req, res) => {
  const { refreshToken } = req.body;
  const decoded = jwt.verify(refreshToken, process.env.REFRESH_SECRET);
  const newAccessToken = jwt.sign(
    { sub: decoded.sub },
    process.env.JWT_SECRET,
    { expiresIn: '15m' }
  );
  res.json({ accessToken: newAccessToken });
});
```

---

# 4️⃣ OAuth2 — Délégation d'Autorisation

## Définition

**OAuth2** est un protocole d'autorisation qui permet à une application d'accéder aux ressources d'un utilisateur **sans connaître son mot de passe**.

Exemple concret :

```text
"Se connecter avec Google"
```

L'application ne connaît pas votre mot de passe Google. Elle reçoit uniquement un token d'accès limité.

Source : RFC 6749 — https://datatracker.ietf.org/doc/html/rfc6749

---

## Les 4 acteurs OAuth2

| Acteur            | Rôle                                        |
| ----------------- | ------------------------------------------- |
| Resource Owner    | L'utilisateur (vous)                        |
| Client            | L'application tierce                        |
| Authorization Server | Google, GitHub, Facebook...             |
| Resource Server   | L'API qui contient les données              |

---

## Authorization Code Flow (le plus sécurisé)

```text
1. User clique "Se connecter avec Google"
2. Client redirige vers Google (Authorization Server)
3. User se connecte sur Google et autorise
4. Google redirige vers le Client avec un code
5. Client échange le code contre un Access Token (côté serveur)
6. Client utilise l'Access Token pour appeler l'API Google
```

Schéma :

```text
User
 ↓ (1) clique
Client App
 ↓ (2) redirect
Authorization Server (Google)
 ↓ (3) user consent
Authorization Code → Client App
 ↓ (4) échange code
Access Token → Client App
 ↓ (5) appel API
Resource Server (Google API)
```

---

## Scopes OAuth2

Les **scopes** définissent les permissions accordées.

Exemples Google :

```text
openid          → Identité de base
email           → Adresse email
profile         → Nom, photo
https://www.googleapis.com/auth/drive → Google Drive
```

Le principe du **moindre privilège** : demander uniquement les scopes nécessaires.

---

# 5️⃣ OpenID Connect (OIDC)

**OpenID Connect** est une couche d'identité construite **au-dessus d'OAuth2**.

```text
OAuth2  →  Autorisation (accès aux ressources)
OIDC    →  Authentification (identité de l'utilisateur)
```

OIDC ajoute un **ID Token** (JWT) qui contient l'identité de l'utilisateur.

```json
{
  "sub": "user_google_123",
  "email": "alice@gmail.com",
  "name": "Alice",
  "iss": "https://accounts.google.com"
}
```

---

# 6️⃣ Zero Trust Architecture

## Définition

Le modèle traditionnel de sécurité :

```text
"Faire confiance à tout ce qui est dans le réseau interne"
```

Zero Trust repose sur un principe radicalement différent :

```text
"Ne jamais faire confiance, toujours vérifier"
Never Trust, Always Verify
```

Source : NIST SP 800-207 — https://csrc.nist.gov/publications/detail/sp/800-207/final

---

## Pourquoi Zero Trust ?

Avant :

```text
Réseau interne = Zone de confiance
Réseau externe = Zone dangereuse
```

Problème : Si un attaquant pénètre le réseau interne → accès total.

Avec Zero Trust :

```text
Chaque requête est authentifiée et autorisée
Même à l'intérieur du réseau
```

---

## Les 3 principes fondamentaux

### 1. Vérifier explicitement

Authentifier et autoriser **chaque requête**, peu importe l'origine.

### 2. Utiliser le moindre privilège

Donner uniquement les accès **strictement nécessaires**.

```text
Un service de paiement ne doit pas lire les emails.
```

### 3. Supposer une violation

Concevoir le système comme si l'attaquant était **déjà à l'intérieur**.

Segmenter, chiffrer, monitorer.

---

## Zero Trust en pratique

```text
✅ MFA (Multi-Factor Authentication) obligatoire
✅ JWT + expiration courte
✅ RBAC (Role-Based Access Control)
✅ mTLS entre microservices
✅ Logs & Monitoring de chaque accès
✅ Network segmentation
✅ Principe du moindre privilège
```

---

# 7️⃣ RBAC — Role-Based Access Control

**RBAC** (contrôle d'accès basé sur les rôles) est un modèle d'autorisation.

Exemple :

| Rôle    | Permissions                      |
| ------- | -------------------------------- |
| Admin   | Lire, Écrire, Supprimer          |
| Editor  | Lire, Écrire                     |
| Viewer  | Lire uniquement                  |

Middleware Node.js :

```javascript
const authorize = (...roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({ message: 'Forbidden' });
    }
    next();
  };
};

// Usage
app.delete('/users/:id', authenticate, authorize('admin'), deleteUser);
```

---

# 8️⃣ Checklist Sécurité Senior

```text
✅ JWT avec expiration courte (15min - 1h)
✅ Refresh Token stocké en HttpOnly Cookie
✅ HTTPS obligatoire (TLS)
✅ Variables d'environnement pour les secrets
✅ Ne jamais stocker de secrets dans le code
✅ OAuth2 pour l'authentification tierce
✅ RBAC pour les autorisations
✅ MFA pour les comptes sensibles
✅ Rate Limiting sur /login
✅ Logs de toutes les authentifications
✅ Rotation régulière des secrets
```

---

# 📊 Comparaison des approches

| Approche    | Type          | Usage                        |
| ----------- | ------------- | ---------------------------- |
| Sessions    | Stateful      | Apps web classiques          |
| JWT         | Stateless     | APIs, microservices           |
| OAuth2      | Délégation    | Login social, accès tiers     |
| OIDC        | Identité      | SSO, fédération d'identité    |
| Zero Trust  | Architecture  | Sécurité réseau enterprise    |

---

# 🧠 Mini exercice

Une application permet à des utilisateurs de se connecter via GitHub.

Questions :

1️⃣ Quel protocole utiliser ? OAuth2 ou JWT ?  
2️⃣ Qui est l'Authorization Server dans ce cas ?  
3️⃣ Après connexion, comment stocker le token côté client de manière sécurisée ?  
4️⃣ Quelle est la différence entre Access Token et Refresh Token ?

---

# 📚 Sources

RFC 6749 — The OAuth 2.0 Authorization Framework  
https://datatracker.ietf.org/doc/html/rfc6749

RFC 7519 — JSON Web Token (JWT)  
https://datatracker.ietf.org/doc/html/rfc7519

NIST Special Publication 800-207 — Zero Trust Architecture  
https://csrc.nist.gov/publications/detail/sp/800-207/final

Auth0 Documentation  
https://auth0.com/docs/

---

Ramadan Tech Challenge 🌙  
Jour 27 — Sécurité Avancée : OAuth2, JWT & Zero Trust 🔒
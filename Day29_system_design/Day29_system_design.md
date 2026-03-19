# 📘 Day 29 — System Design : Architecture à Grande Échelle

## 🎯 Objectif

Comprendre comment **concevoir des systèmes scalables, fiables et performants** comme le font les ingénieurs senior dans les grandes entreprises tech.

Concepts étudiés :

* Approche System Design
* Scalabilité horizontale vs verticale
* Load Balancing
* Caching
* CDN
* Message Queues
* Database Design à grande échelle
* Étude de cas : concevoir un système type Twitter/YouTube

Sources :

* Xu, Alex — *System Design Interview* (2020)
* Kleppmann, Martin — *Designing Data-Intensive Applications* (O'Reilly, 2017)
* AWS Architecture Center — https://aws.amazon.com/architecture/
* Google SRE Book — https://sre.google/sre-book/

---

# 1️⃣ C'est quoi le System Design ?

Le **System Design** est l'art de concevoir l'**architecture complète** d'un système logiciel à grande échelle.

Questions typiques en entretien senior :

```text
"Comment concevoir Twitter ?"
"Comment concevoir YouTube ?"
"Comment concevoir un système de notifications ?"
```

L'objectif : concevoir un système qui supporte **des millions d'utilisateurs** de manière **fiable, performante et maintenable**.

---

# 2️⃣ Scalabilité : Verticale vs Horizontale

## Scalabilité Verticale (Scale Up)

Augmenter les ressources d'une seule machine.

```text
Serveur 8 CPU → 32 CPU
RAM 16 GB → 128 GB
```

Limites :

```text
❌ Coûteux
❌ Limite physique
❌ Single point of failure
```

## Scalabilité Horizontale (Scale Out)

Ajouter plus de machines.

```text
1 serveur → 10 serveurs → 100 serveurs
```

Avantages :

```text
✅ Pas de limite théorique
✅ Tolérance aux pannes
✅ Utilisé par Google, Netflix, Amazon
```

---

# 3️⃣ Load Balancer

Un **Load Balancer** distribue le trafic entre plusieurs serveurs.

```text
Clients
   ↓
Load Balancer
   ↙    ↓    ↘
Server1 Server2 Server3
```

## Algorithmes de Load Balancing

| Algorithme        | Description                              |
| ----------------- | ---------------------------------------- |
| Round Robin       | Tour à tour                              |
| Least Connections | Vers le serveur le moins chargé          |
| IP Hash           | Même client → même serveur (sticky)      |
| Weighted          | Selon la capacité de chaque serveur      |

## Types

```text
Layer 4 (Transport) → basé sur IP/TCP
Layer 7 (Application) → basé sur HTTP (URL, headers)
```

Exemples : **Nginx, AWS ALB, HAProxy**

---

# 4️⃣ Caching

Le **cache** stocke temporairement des données en mémoire pour éviter des calculs ou requêtes répétées.

```text
Sans cache :
Client → Server → Base de données → réponse (lent)

Avec cache :
Client → Server → Cache (Redis) → réponse (rapide)
```

## Stratégies de Cache

### Cache-Aside (Lazy Loading)

```text
1. Chercher dans le cache
2. Si miss → chercher en base → stocker dans le cache
3. Retourner la donnée
```

```javascript
const getUser = async (id) => {
  const cached = await redis.get(`user:${id}`);
  if (cached) return JSON.parse(cached);

  const user = await db.findUser(id);
  await redis.set(`user:${id}`, JSON.stringify(user), 'EX', 3600);
  return user;
};
```

### Write-Through

Écriture simultanée dans le cache et la base.

### Write-Behind (Write-Back)

Écriture dans le cache d'abord, puis en base de manière asynchrone.

## Cache Invalidation

Le problème le plus difficile en cache :

```text
"Il y a deux choses difficiles en informatique :
l'invalidation de cache et nommer les choses."
— Phil Karlton
```

Stratégies :

```text
TTL (Time To Live) → expiration automatique
Event-based → invalider quand la donnée change
```

---

# 5️⃣ CDN — Content Delivery Network

Un **CDN** est un réseau de serveurs distribués géographiquement qui servent le contenu statique **depuis le point le plus proche de l'utilisateur**.

```text
Sans CDN :
Utilisateur (Maroc) → Serveur (USA) → latence élevée

Avec CDN :
Utilisateur (Maroc) → CDN Edge (Europe) → latence faible
```

Contenu mis en cache par le CDN :

```text
✅ Images
✅ Vidéos
✅ CSS / JavaScript
✅ Fichiers statiques
```

Exemples : **Cloudflare, AWS CloudFront, Akamai**

---

# 6️⃣ Message Queues

Les **message queues** permettent la communication **asynchrone** entre services.

```text
Sans Queue :
Service A → appelle directement → Service B (couplage fort)

Avec Queue :
Service A → Message Queue → Service B (découplage)
```

## Cas d'usage

```text
✅ Envoi d'emails (ne pas bloquer la requête principale)
✅ Traitement d'images (asynchrone)
✅ Notifications push
✅ Paiements (fiabilité garantie)
```

Exemples : **Kafka, RabbitMQ, AWS SQS**

---

# 7️⃣ Les composants clés d'un système à grande échelle

```text
DNS
 ↓
CDN (contenu statique)
 ↓
Load Balancer
 ↓
API Gateway
 ↙         ↘
Service A    Service B
   ↓              ↓
Cache (Redis)   Message Queue
   ↓              ↓
Base de données primaire
   ↓
Réplicas (lecture)
```

---

# 8️⃣ Étude de cas : Concevoir un système de partage de vidéos (type YouTube)

## Étape 1 — Clarifier les exigences

```text
Fonctionnel :
- Upload de vidéos
- Streaming de vidéos
- Recherche
- Commentaires / Likes

Non-fonctionnel :
- 500 millions d'utilisateurs actifs
- 100 heures de vidéo uploadées par minute
- Disponibilité : 99.99%
- Faible latence pour le streaming
```

## Étape 2 — Estimation de capacité

```text
Stockage :
100 heures/minute × 60 min × 1 GB/heure ≈ 6 TB/heure

Bande passante :
Si 5 millions d'utilisateurs regardent en même temps
à 2 Mbps → 10 Tbps
```

## Étape 3 — Architecture

```text
Upload Flow :
Client → API Gateway → Upload Service
                            ↓
                    Object Storage (S3)
                            ↓
                    Message Queue (Kafka)
                            ↓
                    Video Processing Service
                    (transcoding, compression)
                            ↓
                    CDN (distribution globale)

Streaming Flow :
Client → CDN → Vidéo encodée (multiple résolutions)
```

## Étape 4 — Base de données

```text
Metadata (titre, description, user_id) → PostgreSQL
Vidéos (fichiers) → Object Storage (S3, GCS)
Cache (vidéos populaires) → Redis
Recherche → Elasticsearch
```

## Étape 5 — Scalabilité

```text
Upload Service → scalé horizontalement
CDN → distribué globalement
Base de données → sharding par video_id
Cache → Redis Cluster
```

---

# 9️⃣ Availability & SLA

## Calcul de disponibilité

```text
99%    → 3.65 jours d'indisponibilité/an
99.9%  → 8.7 heures/an
99.99% → 52 minutes/an
99.999% → 5 minutes/an (Five Nines)
```

## Techniques pour améliorer la disponibilité

```text
✅ Redondance (plusieurs instances)
✅ Health checks automatiques
✅ Auto-scaling
✅ Circuit Breaker pattern
✅ Retry avec exponential backoff
✅ Graceful degradation
```

---

# 🔟 Design Patterns importants

## Circuit Breaker

Évite les appels répétés vers un service défaillant.

```text
CLOSED → Normal
OPEN   → Service en panne, réponse immédiate d'erreur
HALF-OPEN → Test si le service est revenu
```

## Rate Limiting

Limiter le nombre de requêtes par utilisateur / IP.

```text
100 requêtes/minute par utilisateur
```

## Retry avec Exponential Backoff

```text
Tentative 1 → attendre 1s
Tentative 2 → attendre 2s
Tentative 3 → attendre 4s
Tentative 4 → attendre 8s
```

## Idempotency

Une opération répétée plusieurs fois produit le **même résultat**.

```text
Paiement avec idempotency key → pas de double débit
```

---

# 📊 Framework de réponse en entretien System Design

```text
1️⃣  Clarifier les exigences (5 min)
    → Fonctionnelles + Non-fonctionnelles

2️⃣  Estimation de capacité (5 min)
    → Users, Storage, Bandwidth, QPS

3️⃣  High-level design (10 min)
    → Architecture globale, composants principaux

4️⃣  Deep dive (15 min)
    → Détailler les composants critiques

5️⃣  Identifier et résoudre les bottlenecks (5 min)
    → Single points of failure, scalabilité
```

---

# 🎓 Bonnes pratiques Senior

```text
✅ Toujours commencer par les exigences
✅ Penser aux cas d'échec dès le départ
✅ Préférer la simplicité à l'over-engineering
✅ Séparer les reads des writes (CQRS)
✅ Monitorer chaque composant
✅ Documenter les décisions architecturales (ADR)
✅ Concevoir pour la scalabilité dès le début
✅ Tester les pannes (Chaos Engineering)
```

---

# 🧠 Mini exercice

Tu dois concevoir un **système de notifications** (type WhatsApp / Instagram) pour **200 millions d'utilisateurs**.

Questions :

1️⃣ Quelle technologie utiliser pour envoyer des notifications en temps réel ?  
2️⃣ Pourquoi utiliser une Message Queue pour les notifications ?  
3️⃣ Comment stocker l'historique des notifications à grande échelle ?  
4️⃣ Comment garantir qu'une notification est envoyée **exactement une fois** ?

---

# 📚 Sources

Xu, Alex  
*System Design Interview — An Insider's Guide*

Kleppmann, Martin  
*Designing Data-Intensive Applications* — O'Reilly  
https://dataintensive.net/

Google SRE Book  
https://sre.google/sre-book/

AWS Architecture Center  
https://aws.amazon.com/architecture/

---

Ramadan Tech Challenge 🌙  
Jour 29 — System Design : Architecture à Grande Échelle 🌐
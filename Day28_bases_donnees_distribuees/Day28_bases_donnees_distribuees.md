# 📘 Day 28 — Bases de Données Distribuées

## 🎯 Objectif

Comprendre les **bases de données distribuées** et les concepts fondamentaux qui permettent de stocker et gérer des données à grande échelle.

Concepts étudiés :

* Pourquoi les bases distribuées ?
* Théorème CAP
* Sharding
* Réplication
* Consistency Models
* Types de bases distribuées
* Quand utiliser quoi ?

Sources :

* Kleppmann, Martin — *Designing Data-Intensive Applications* (O'Reilly, 2017)
* Brewer, Eric — *CAP Twelve Years Later* (IEEE Computer, 2012)
* Amazon DynamoDB Documentation — https://docs.aws.amazon.com/dynamodb/
* MongoDB Documentation — https://www.mongodb.com/docs/

---

# 1️⃣ Pourquoi les bases de données distribuées ?

Une base de données classique (single-node) atteint ses limites :

```text
Problèmes à grande échelle :
- Volume de données trop important (TB, PB)
- Trop de requêtes simultanées
- Risque de panne (single point of failure)
- Latence trop élevée pour des utilisateurs géographiquement distants
```

La solution : **distribuer les données sur plusieurs machines (nœuds)**.

```text
Avantages :
✅ Scalabilité horizontale
✅ Haute disponibilité
✅ Tolérance aux pannes
✅ Réduction de la latence (données proches de l'utilisateur)
```

---

# 2️⃣ Théorème CAP

Le **théorème CAP** (Brewer, 2000) est fondamental pour comprendre les bases distribuées.

Il stipule qu'un système distribué **ne peut garantir que 2 des 3 propriétés suivantes simultanément** :

## C — Consistency (Cohérence)

Tous les nœuds voient les **mêmes données au même moment**.

```text
Lecture après écriture → toujours la valeur la plus récente
```

## A — Availability (Disponibilité)

Le système répond **toujours**, même en cas de panne partielle.

```text
Chaque requête reçoit une réponse (pas forcément la plus récente)
```

## P — Partition Tolerance (Tolérance aux partitions)

Le système **continue de fonctionner** même si des nœuds ne peuvent plus communiquer entre eux.

```text
Réseau coupé entre 2 nœuds → le système continue
```

---

## Les 3 combinaisons possibles

| Combinaison | Exemples               | Sacrifice              |
| ----------- | ---------------------- | ---------------------- |
| CP          | MongoDB, HBase, Redis  | Disponibilité          |
| AP          | Cassandra, DynamoDB    | Cohérence forte        |
| CA          | PostgreSQL (single)    | Tolérance aux pannes   |

⚠️ En pratique, **P est inévitable** dans un système distribué.  
Le vrai choix est donc entre **C et A**.

---

# 3️⃣ Sharding (Partitionnement horizontal)

Le **sharding** consiste à diviser les données en **partitions (shards)** réparties sur plusieurs nœuds.

```text
Sans sharding :
Nœud 1 → tous les utilisateurs (10 millions)

Avec sharding :
Shard 1 → utilisateurs A-H
Shard 2 → utilisateurs I-P
Shard 3 → utilisateurs Q-Z
```

## Stratégies de sharding

### 1. Range-based sharding

```text
Shard 1 → user_id 1 à 1 000 000
Shard 2 → user_id 1 000 001 à 2 000 000
```

Simple mais peut créer des **hot spots** (un shard surchargé).

### 2. Hash-based sharding

```text
shard = hash(user_id) % nombre_de_shards
```

Distribution plus uniforme.

### 3. Directory-based sharding

Un service central maintient une **table de correspondance** clé → shard.

Flexible mais ajoute un point de défaillance.

---

# 4️⃣ Réplication

La **réplication** consiste à copier les données sur plusieurs nœuds pour la **haute disponibilité** et la **tolérance aux pannes**.

## Master-Slave (Primary-Replica)

```text
Master (Primary)
   ↓ réplication
Replica 1    Replica 2    Replica 3
```

- **Master** : gère les écritures
- **Replicas** : servent les lectures

Avantage : scalabilité en lecture.  
Inconvénient : si le master tombe → failover nécessaire.

## Multi-Master

```text
Master 1  ←→  Master 2  ←→  Master 3
```

Tous les nœuds acceptent les écritures.  
Problème : **conflits d'écriture** à gérer.

---

# 5️⃣ Consistency Models

## Strong Consistency (Cohérence forte)

```text
Après une écriture → toute lecture retourne la valeur écrite
```

Exemple : bases relationnelles (PostgreSQL).

## Eventual Consistency (Cohérence éventuelle)

```text
Après une écriture → les données seront cohérentes... éventuellement
```

Les nœuds se synchronisent avec un léger délai.

Exemple : DNS, Cassandra, DynamoDB.

## Read-Your-Writes Consistency

```text
Un utilisateur voit toujours ses propres écritures
```

Exemple : après avoir posté un tweet, vous le voyez immédiatement.

---

# 6️⃣ Types de bases distribuées

## SQL Distribué (NewSQL)

Bases relationnelles distribuées qui conservent les propriétés ACID.

| Base          | Description                     |
| ------------- | ------------------------------- |
| CockroachDB   | SQL distribué, CP               |
| Google Spanner| SQL distribué global            |
| TiDB          | Compatible MySQL, distribué     |

---

## NoSQL Distribué

### Clé-Valeur

```text
Redis Cluster, DynamoDB, Riak
```

Usage : cache, sessions, compteurs.

### Document

```text
MongoDB, CouchDB
```

Usage : données JSON flexibles.

### Colonne large (Wide-Column)

```text
Apache Cassandra, HBase
```

Usage : séries temporelles, logs massifs.

```sql
-- Cassandra CQL
CREATE TABLE events (
  user_id UUID,
  timestamp TIMESTAMP,
  event TEXT,
  PRIMARY KEY (user_id, timestamp)
);
```

### Graphe

```text
Neo4j, Amazon Neptune
```

Usage : réseaux sociaux, recommandations.

---

# 7️⃣ Focus : Apache Cassandra

Cassandra est un exemple emblématique de base distribuée **AP**.

Caractéristiques :

```text
✅ Aucun master (architecture peer-to-peer)
✅ Scalabilité linéaire
✅ Haute disponibilité
✅ Eventual consistency (configurable)
```

## Concept clé : Replication Factor

```text
Replication Factor = 3
→ chaque donnée est copiée sur 3 nœuds
```

## Concept clé : Consistency Level

```text
QUORUM = majorité des nœuds doivent confirmer
ONE    = un seul nœud suffit (plus rapide, moins sûr)
ALL    = tous les nœuds (plus lent, plus sûr)
```

---

# 8️⃣ Focus : MongoDB Distribué

MongoDB supporte le sharding natif via **Replica Sets** et **Sharded Clusters**.

```text
Mongos (Router)
     ↓
Config Servers (métadonnées)
     ↓
Shard 1    Shard 2    Shard 3
(Replica Set) (Replica Set) (Replica Set)
```

Définir une shard key :

```javascript
sh.shardCollection("mydb.users", { country: 1 });
```

---

# 9️⃣ ACID vs BASE

| Propriété | ACID (SQL)           | BASE (NoSQL distribué)         |
| --------- | -------------------- | ------------------------------ |
| Cohérence | Forte                | Éventuelle                     |
| Dispo     | Limitée              | Haute                          |
| Modèle    | Transactions strictes| Disponibilité prioritaire      |
| Usage     | Finance, santé       | Réseaux sociaux, IoT, logs     |

**BASE** signifie :
- **B**asically **A**vailable
- **S**oft state
- **E**ventually consistent

---

# 📊 Quand utiliser quoi ?

| Besoin                         | Solution recommandée         |
| ------------------------------ | ---------------------------- |
| Transactions financières       | PostgreSQL / CockroachDB     |
| Cache haute performance        | Redis Cluster                |
| Logs / séries temporelles      | Cassandra / InfluxDB         |
| Données JSON flexibles         | MongoDB                      |
| Réseau social / graphe         | Neo4j                        |
| Données massives clé-valeur    | DynamoDB                     |
| SQL distribué global           | Google Spanner               |

---

# 🎓 Bonnes pratiques Senior

```text
✅ Choisir la base en fonction des besoins (pas de la mode)
✅ Comprendre le théorème CAP avant de choisir
✅ Toujours planifier la shard key avec soin
✅ Surveiller les hot spots
✅ Tester le comportement en cas de partition réseau
✅ Définir une stratégie de backup et de recovery
✅ Monitorer la latence de réplication
✅ Ne pas over-engineer si une base simple suffit
```

---

# 🧠 Mini exercice

Tu construis une plateforme de **streaming musical** (type Spotify) avec :

- 100 millions d'utilisateurs
- Des playlists, des écoutes, des recommandations
- Besoin de données en temps réel

Questions :

1️⃣ Quelle propriété du CAP est prioritaire pour l'historique d'écoute ?  
2️⃣ Quelle base choisirais-tu pour stocker les événements d'écoute (logs) ?  
3️⃣ Pourquoi le sharding est-il nécessaire à cette échelle ?  
4️⃣ Quelle stratégie de réplication garantit la haute disponibilité ?

---

# 📚 Sources

Kleppmann, Martin  
*Designing Data-Intensive Applications* — O'Reilly Media  
https://dataintensive.net/

Brewer, Eric  
*CAP Twelve Years Later: How the Rules Have Changed*  
IEEE Computer, 2012

Apache Cassandra Documentation  
https://cassandra.apache.org/doc/

MongoDB Documentation  
https://www.mongodb.com/docs/

Amazon DynamoDB Documentation  
https://docs.aws.amazon.com/dynamodb/

---

Ramadan Tech Challenge 🌙  
Jour 28 — Bases de Données Distribuées 🗃️
# 🔥 Day 07 -- Apache Kafka (Niveau Ingénieur)

## 📌 1. C'est quoi Apache Kafka ?

Apache Kafka est une plateforme distribuée de streaming d'événements.

Il permet : - De transmettre des données en temps réel - De connecter
des microservices - De traiter des flux massifs de données - De
construire des architectures event-driven

Kafka est utilisé par : - Netflix - Uber - LinkedIn - Airbnb

------------------------------------------------------------------------

# 🧠 2. Pourquoi Kafka ?

Problème sans Kafka : - Couplage fort entre services - Appels synchrones
(REST) - Faible scalabilité - Risque de blocage

Kafka permet : - Communication asynchrone - Haute performance -
Résilience - Scalabilité horizontale

------------------------------------------------------------------------

# 🏗 3. Architecture Kafka

Un cluster Kafka contient :

## 🔹 Producer

Envoie des messages.

## 🔹 Broker

Serveur Kafka qui stocke les messages.

## 🔹 Topic

Catégorie de messages.

## 🔹 Partition

Division d'un topic pour permettre la scalabilité.

## 🔹 Consumer

Lit les messages.

## 🔹 Zookeeper (ou KRaft mode moderne)

Gère la coordination du cluster.

------------------------------------------------------------------------

# 📦 4. Comment ça fonctionne ?

1.  Le Producer envoie un message dans un Topic.
2.  Le Broker stocke le message.
3.  Le Consumer lit le message quand il veut.
4.  Le message reste stocké selon une politique de rétention.

Kafka ne supprime pas immédiatement les messages.

------------------------------------------------------------------------

# ⚡ 5. Exemple Microservices

Exemple e-commerce :

Order Service → envoie événement "OrderCreated" Kafka → stocke
l'événement Payment Service → consomme l'événement Notification Service
→ consomme aussi l'événement

Les services ne se parlent pas directement.

------------------------------------------------------------------------

# 📊 6. Pourquoi Kafka est rapide ?

-   Écriture séquentielle sur disque
-   Utilisation du Page Cache
-   Architecture distribuée
-   Partitions parallèles

Kafka peut traiter des millions de messages par seconde.

------------------------------------------------------------------------

# 🔄 7. Consumer Groups

Plusieurs consommateurs peuvent lire un topic.

Chaque groupe reçoit chaque message une seule fois.

Permet : - Scalabilité - Load balancing - Haute disponibilité

------------------------------------------------------------------------

# 🛡 8. Garanties Kafka

-   At least once
-   At most once
-   Exactly once (avec configuration avancée)

------------------------------------------------------------------------

# 🌍 9. Kafka dans le Cloud

Disponible sur : - AWS MSK - Azure Event Hubs - Confluent Cloud

------------------------------------------------------------------------

# 🧠 10. Quand utiliser Kafka ?

Utiliser Kafka si : - Architecture microservices - Besoin temps réel -
Gros volume de données - Event sourcing - Streaming analytics

Ne pas utiliser Kafka si : - Petite application simple - Peu
d'utilisateurs - Pas besoin d'asynchrone

------------------------------------------------------------------------

# 🏁 Conclusion

Kafka est le cœur des architectures modernes orientées événements.

Il permet : - Découplage - Scalabilité - Résilience - Traitement temps
réel

------------------------------------------------------------------------

Ramadan Tech Challenge 🌙\
Jour 07 -- Apache Kafka 🚀

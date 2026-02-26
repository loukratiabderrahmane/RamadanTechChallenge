# 🏗 Day 06 -- Architecture Microservices 

## 📌 1. C'est quoi l'Architecture Microservices ?

L'architecture microservices est un style architectural où une
application est divisée en plusieurs petits services indépendants.

Chaque service : - A une responsabilité unique - Possède sa propre base
de données (idéalement) - Peut être déployé indépendamment - Communique
via API (REST, gRPC, message queue)

------------------------------------------------------------------------

# 🧠 2. Pourquoi Microservices ?

Problème du Monolithe :

-   Code centralisé
-   Déploiement unique
-   Difficile à scaler partiellement
-   Risque élevé en cas de crash

Microservices permettent : - Scalabilité indépendante - Déploiement
indépendant - Meilleure résilience - Équipes autonomes

------------------------------------------------------------------------

# 🧱 3. Monolithe vs Microservices

## Monolithe

Frontend + Backend + DB = une seule application.

## Microservices

Exemple : - Auth Service - User Service - Payment Service - Order
Service - Notification Service

Chaque service est isolé.

------------------------------------------------------------------------

# 🔄 4. Communication entre Services

## 🔹 REST API

Service A appelle Service B via HTTP.

## 🔹 gRPC

Communication rapide via protocole binaire.

## 🔹 Message Queue

Exemple : Kafka, RabbitMQ. Communication asynchrone.

------------------------------------------------------------------------

# 📦 5. Base de Données

Bonne pratique : Chaque microservice a sa propre base.

Pourquoi ? Éviter le couplage fort entre services.

------------------------------------------------------------------------

# 🌐 6. API Gateway

Une API Gateway : - Point d'entrée unique - Gère authentification - Rate
limiting - Logging

Architecture : Client → API Gateway → Microservices

------------------------------------------------------------------------

# ⚖️ 7. Scalabilité

On peut scaler uniquement :

-   Le service Payment si charge élevée
-   Le service Auth si beaucoup de logins

Pas besoin de scaler toute l'application.

------------------------------------------------------------------------

# 🔐 8. Sécurité en Microservices

-   JWT partagé
-   Mutual TLS
-   Service Mesh (Istio)
-   RBAC
-   Network policies

------------------------------------------------------------------------

# 🐳 9. Microservices + Docker + Kubernetes

Chaque service : - Dockerisé - Déployé dans Kubernetes - Scalé
automatiquement - Monitoré

C'est l'architecture cloud moderne.

------------------------------------------------------------------------

# 📊 10. Observabilité

Important : - Logs centralisés - Monitoring (Prometheus) - Tracing
distribué (Jaeger) - Alerting

Sans observabilité → impossible de debuguer.

------------------------------------------------------------------------

# ⚠️ 11. Inconvénients

-   Complexité élevée
-   Debugging difficile
-   Gestion réseau complexe
-   Plus de DevOps nécessaire

Microservices ≠ toujours la meilleure solution.

------------------------------------------------------------------------

# 🧠 12. Mentalité Ingénieur

Toujours se demander :

-   Mon application est-elle assez grande pour microservices ?
-   Ai-je une équipe capable de gérer la complexité ?
-   Est-ce que le monolithe modulaire suffit ?

------------------------------------------------------------------------

# 🏁 Conclusion

Microservices = Scalabilité + Indépendance + Résilience

Mais demandent : - Infrastructure solide - DevOps mature - Monitoring
avancé

C'est l'architecture utilisée par les grandes entreprises tech.

------------------------------------------------------------------------

Ramadan Tech Challenge 🌙\
Jour 06 -- Architecture Microservices 🚀

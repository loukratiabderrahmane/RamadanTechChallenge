# ☸️ Day 04 -- Kubernetes en Profondeur 

## 📌 1. C'est quoi Kubernetes ?

Kubernetes (K8s) est un orchestrateur de conteneurs.

Il permet de : - Déployer des applications conteneurisées - Les scaler
automatiquement - Gérer la haute disponibilité - Redémarrer les
conteneurs en cas de crash

Docker lance des conteneurs. Kubernetes les orchestre à grande échelle.

------------------------------------------------------------------------

# 🧠 2. Pourquoi Kubernetes existe ?

Quand on a : - 1 conteneur → Docker suffit. - 100 conteneurs → Il faut
les gérer automatiquement.

Problèmes sans Kubernetes : - Crash d'un conteneur - Scalabilité
manuelle - Gestion réseau complexe - Déploiement difficile

Kubernetes automatise tout cela.

------------------------------------------------------------------------

# 🏗 3. Architecture Kubernetes

Un cluster Kubernetes contient :

## 🔹 Master Node (Control Plane)

-   API Server
-   Scheduler
-   Controller Manager
-   etcd (base de données du cluster)

## 🔹 Worker Nodes

-   Kubelet
-   Kube-proxy
-   Conteneurs (via container runtime)

------------------------------------------------------------------------

# 📦 4. Les Objets Principaux

## 🐳 Pod

Un Pod est l'unité minimale. Il contient un ou plusieurs conteneurs.

## 📊 Deployment

Gère : - Le nombre de replicas - Les mises à jour progressives - Le
rollback

## 🌐 Service

Expose les Pods via : - ClusterIP - NodePort - LoadBalancer

## 📈 ReplicaSet

Maintient un nombre défini de Pods actifs.

------------------------------------------------------------------------

# 📝 5. Exemple simple Deployment

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        ports:
        - containerPort: 3000
```

Commande :

kubectl apply -f deployment.yaml

------------------------------------------------------------------------

# ⚖️ 6. Scalabilité Automatique

Kubernetes peut : - Augmenter les replicas - Diminuer les replicas -
Basé sur CPU / mémoire

HPA (Horizontal Pod Autoscaler).

------------------------------------------------------------------------

# 🔄 7. Rolling Updates

Kubernetes met à jour : - Progressivement - Sans downtime - Avec
possibilité de rollback

------------------------------------------------------------------------

# 🔐 8. Sécurité Kubernetes

-   RBAC
-   Network Policies
-   Secrets
-   Isolation namespaces
-   TLS interne

------------------------------------------------------------------------

# 🌍 9. Kubernetes dans le Cloud

Disponible sur :

-   AWS (EKS)
-   Azure (AKS)
-   Google Cloud (GKE)

Les fournisseurs gèrent le Control Plane.

------------------------------------------------------------------------

# 🧠 10. Mentalité Ingénieur Kubernetes

Toujours : - Déclaratif (YAML) - Automatisation - Monitoring -
Observabilité - Résilience

------------------------------------------------------------------------

# 🏁 Conclusion

Docker standardise l'exécution. Kubernetes standardise l'orchestration.

C'est une compétence clé pour : - DevOps Engineer - Cloud Engineer -
Backend Scalabilité

------------------------------------------------------------------------

Ramadan Tech Challenge 🌙\
Jour 04 -- Kubernetes ☸️

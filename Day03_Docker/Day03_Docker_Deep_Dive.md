# 🐳 Day 03 -- Docker en Profondeur 

## 📌 1. C'est quoi Docker ?

Docker est une technologie de conteneurisation qui permet d'exécuter une
application dans un environnement isolé appelé conteneur.

Un conteneur contient : - Le code - Les dépendances - Les librairies -
Le runtime - Les variables d'environnement

Objectif : "It works on my machine" ne doit plus jamais être un
problème.

------------------------------------------------------------------------

# 🧠 2. Différence entre VM et Docker

## Machine Virtuelle (VM)

-   Contient un OS complet
-   Plus lourde
-   Plus lente à démarrer

## Docker (Container)

-   Partage le noyau du système hôte
-   Plus léger
-   Démarre en quelques secondes

Docker utilise : - Namespaces (isolation) - Cgroups (limitation
ressources) - Union File System

------------------------------------------------------------------------

# 🏗 3. Architecture Docker

Docker comprend :

-   Docker Client (CLI)
-   Docker Daemon (dockerd)
-   Docker Images
-   Docker Containers
-   Docker Registry (Docker Hub)

------------------------------------------------------------------------

# 📦 4. Image vs Container

## Image

Modèle en lecture seule (template).

Exemple : node:18

## Container

Instance en exécution d'une image.

------------------------------------------------------------------------

# 🐳 5. Dockerfile (Exemple Node.js)

``` dockerfile
FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
```

Construction :

docker build -t myapp .

Exécution :

docker run -p 3000:3000 myapp

------------------------------------------------------------------------

# 🌐 6. Docker Networking

Types de réseaux : - Bridge (par défaut) - Host - Overlay
(multi-machines)

Permet aux conteneurs de communiquer entre eux.

------------------------------------------------------------------------

# 💾 7. Volumes

Les conteneurs sont éphémères.

Pour conserver les données :

docker volume create myvolume

docker run -v myvolume:/data myapp

------------------------------------------------------------------------

# 🚀 8. Docker Compose

Permet de lancer plusieurs services.

Exemple :

``` yaml
version: "3"
services:
  app:
    build: .
    ports:
      - "3000:3000"
  db:
    image: mongo
```

Commande :

docker-compose up

------------------------------------------------------------------------

# 🔥 9. Pourquoi Docker est essentiel en DevOps ?

-   Environnement reproductible
-   Déploiement rapide
-   Scalabilité
-   Compatible Kubernetes
-   Standard industriel

------------------------------------------------------------------------

# 🧠 10. Mentalité Ingénieur Docker

Toujours : - Minimiser la taille des images - Utiliser .dockerignore -
Ne pas exposer de secrets - Utiliser multi-stage builds - Scanner les
vulnérabilités

------------------------------------------------------------------------

# 🏁 Conclusion

Docker permet de standardiser l'exécution des applications.

C'est une compétence clé pour : - Backend Engineer - DevOps Engineer -
Cloud Engineer

------------------------------------------------------------------------

Ramadan Tech Challenge 🌙\
Jour 03 -- Docker 🐳

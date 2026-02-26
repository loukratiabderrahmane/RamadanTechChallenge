# 🔄 Day 05 -- CI/CD Complet (Docker + GitHub Actions + Kubernetes)

## 📌 1. C'est quoi CI/CD ?

CI/CD signifie :

-   CI → Continuous Integration
-   CD → Continuous Delivery / Deployment

Objectif : Automatiser le processus entre : Code → Test → Build → Deploy
→ Production

------------------------------------------------------------------------

# 🧠 2. Continuous Integration (CI)

À chaque push Git :

1.  Le code est récupéré
2.  Les dépendances sont installées
3.  Les tests sont exécutés
4.  Le build est généré

Si une erreur existe → le pipeline échoue.

------------------------------------------------------------------------

# 🚀 3. Continuous Deployment (CD)

Après succès de la CI :

1.  L'image Docker est construite
2.  Elle est envoyée vers un Registry (Docker Hub)
3.  Kubernetes déploie la nouvelle version

Tout est automatique.

------------------------------------------------------------------------

# 🐳 4. Étape 1 -- Dockerisation de l'application

Dockerfile :

``` dockerfile
FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
```

Build local :

docker build -t myapp .

------------------------------------------------------------------------

# 🏗 5. Étape 2 -- GitHub Actions (CI Pipeline)

Créer :

.github/workflows/ci.yml

``` yaml
name: CI Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Setup Node
      uses: actions/setup-node@v3
      with:
        node-version: 18

    - run: npm install
    - run: npm test
```

À chaque push → tests automatiques.

------------------------------------------------------------------------

# 🐳 6. Étape 3 -- Build & Push Docker Image

Ajouter dans le workflow :

``` yaml
- name: Build Docker Image
  run: docker build -t username/myapp:latest .

- name: Login Docker Hub
  run: echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u username --password-stdin

- name: Push Image
  run: docker push username/myapp:latest
```

Utiliser GitHub Secrets pour protéger les credentials.

------------------------------------------------------------------------

# ☸️ 7. Étape 4 -- Déploiement Kubernetes

Deployment.yaml :

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
        image: username/myapp:latest
        ports:
        - containerPort: 3000
```

Déploiement :

kubectl apply -f deployment.yaml

------------------------------------------------------------------------

# 🔄 8. Pipeline Complet Résumé

1.  Push code
2.  GitHub Actions lance les tests
3.  Image Docker construite
4.  Image envoyée vers Docker Hub
5.  Kubernetes met à jour les pods
6.  Rolling update sans downtime

------------------------------------------------------------------------

# 🔐 9. Bonnes Pratiques Sécurité

-   Utiliser GitHub Secrets
-   Ne jamais exposer mots de passe
-   Scanner les images Docker
-   Limiter les permissions Kubernetes (RBAC)

------------------------------------------------------------------------

# 🧠 10. Mentalité DevOps Avancée

Automatiser tout. Réduire les erreurs humaines. Déployer sans
interruption. Monitorer en continu.

------------------------------------------------------------------------

# 🏁 Conclusion

Un pipeline CI/CD moderne combine :

-   Git
-   GitHub Actions
-   Docker
-   Kubernetes
-   Cloud

C'est l'architecture standard des entreprises tech modernes.

------------------------------------------------------------------------

Ramadan Tech Challenge 🌙\
Jour 05 -- CI/CD Complet 🚀

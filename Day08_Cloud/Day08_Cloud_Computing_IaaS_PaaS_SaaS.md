# ☁️ Day 07 -- Cloud Computing -- IaaS vs PaaS vs SaaS

## 📌 1. Définition du Cloud

Le Cloud Computing est un modèle qui permet d'utiliser des ressources
informatiques (serveurs, stockage, réseau, bases de données) via
Internet au lieu d'acheter et gérer son propre matériel.

Au lieu d'avoir un serveur physique chez toi, tu loues une machine dans
un Data Center distant.

------------------------------------------------------------------------

# 🏢 2. Que se passe-t-il en arrière-plan ?

Quand tu crées une machine virtuelle sur un cloud provider (ex: AWS EC2)
:

1.  Un serveur physique dans un data center est sélectionné.
2.  Un hyperviseur divise ce serveur en plusieurs machines virtuelles.
3.  Une portion de CPU et RAM est réservée pour ta VM.
4.  Un disque virtuel est créé.
5.  Une configuration réseau virtuelle est attachée.
6.  Une image système (Linux/Windows) est installée.

Tout cela est virtualisé et isolé des autres clients.

------------------------------------------------------------------------

# 🧱 3. IaaS (Infrastructure as a Service)

## Tu reçois :

-   Machine virtuelle
-   CPU
-   RAM
-   Stockage
-   Réseau

## Tu gères :

-   Système d'exploitation
-   Installation des logiciels
-   Sécurité serveur
-   Base de données
-   Maintenance

Niveau de contrôle : Élevé\
Niveau de responsabilité : Élevé

------------------------------------------------------------------------

# 🧩 4. PaaS (Platform as a Service)

## Tu reçois :

-   Serveur configuré
-   Runtime (Node.js, Python...)
-   Environnement prêt

## Tu gères :

-   Ton code
-   Ta logique métier

Contrôle : Moyen\
Complexité : Faible

------------------------------------------------------------------------

# 💻 5. SaaS (Software as a Service)

## Tu reçois :

-   Application complète
-   Base de données
-   Sécurité
-   Scalabilité

## Tu gères :

-   Ton compte utilisateur

Contrôle : Aucun\
Simplicité : Totale

------------------------------------------------------------------------

# 📊 6. Comparaison

| Élément            | IaaS       | PaaS               | SaaS              |
|--------------------|------------|--------------------|-------------------|
| Serveur physique   | Cloud      | Cloud              | Cloud             |
| OS                 | Toi        | Fournisseur        | Fournisseur       |
| Runtime            | Toi        | Fournisseur        | Fournisseur       |
| Application        | Toi        | Toi                | Fournisseur       |
| Maintenance        | Toi        | Partagée           | Fournisseur       |
| Scalabilité        | Manuelle   | Semi-automatique   | Automatique       |
------------------------------------------------------------------------

# 🧠 7. Architecture cachée derrière SaaS

Un SaaS utilise :

-   IaaS (machines virtuelles)
-   Containers (Docker)
-   Orchestrateur (Kubernetes)
-   Load Balancer
-   CDN
-   Base de données distribuée
-   Monitoring
-   Sécurité multi-niveau

SaaS repose donc sur IaaS.

------------------------------------------------------------------------

# 🏁 Conclusion

Le Cloud est une abstraction de l'infrastructure physique.

IaaS = Infrastructure\
PaaS = Plateforme\
SaaS = Application

Plus tu montes dans la pyramide, moins tu as de contrôle, mais plus
c'est simple.

Ramadan Tech Challenge 🌙\
Jour 08 -- Cloud Computing  ☁️

# 🔐 Sécurité Backend -- Types d'Attaques Web

## 📌 Introduction

La sécurité backend consiste à protéger : - Les utilisateurs - Les
données - Les APIs - Les serveurs - Les bases de données

Comprendre les attaques permet de concevoir des systèmes sécurisés.

------------------------------------------------------------------------

# 1️⃣ SQL Injection (SQLi)

## 🧠 Description

Injection de code SQL malveillant dans un champ utilisateur.

## 💣 Exemple vulnérable

``` js
const query = "SELECT * FROM users WHERE email = '" + email + "'";
```

## 🛡 Protection

-   Requêtes préparées
-   ORM (Prisma, Sequelize)
-   Validation stricte des entrées

------------------------------------------------------------------------

# 2️⃣ NoSQL Injection

## 🧠 Description

Injection malveillante dans une base MongoDB ou NoSQL.

## 💣 Exemple

``` json
{ "$ne": null }
```

## 🛡 Protection

-   Validation stricte
-   Sanitization
-   Ne jamais utiliser directement req.body

------------------------------------------------------------------------

# 3️⃣ XSS (Cross-Site Scripting)

## 🧠 Description

Injection de JavaScript malveillant dans une page web.

## 💣 Exemple

``` html
<script>alert("Hacked")</script>
```

## 🛡 Protection

-   Échapper le HTML
-   Sanitization
-   Helmet
-   Content Security Policy

------------------------------------------------------------------------

# 4️⃣ CSRF (Cross-Site Request Forgery)

## 🧠 Description

Un utilisateur connecté exécute une action sans le savoir.

## 🛡 Protection

-   CSRF Token
-   SameSite Cookies
-   Vérification Origin / Referer

------------------------------------------------------------------------

# 5️⃣ Brute Force

## 🧠 Description

Tentatives massives de mots de passe.

## 🛡 Protection

-   Rate limiting
-   Blocage après X tentatives
-   Captcha
-   2FA

------------------------------------------------------------------------

# 6️⃣ DDoS (Denial of Service)

## 🧠 Description

Surcharge du serveur avec des milliers de requêtes.

## 🛡 Protection

-   Load balancer
-   Rate limiting
-   Cloudflare
-   Firewall

------------------------------------------------------------------------

# 7️⃣ Man-In-The-Middle (MITM)

## 🧠 Description

Interception de communication entre client et serveur.

## 🛡 Protection

-   HTTPS (TLS)
-   Certificats SSL
-   HSTS

------------------------------------------------------------------------

# 8️⃣ Broken Authentication

## 🧠 Description

Mauvaise gestion des sessions ou tokens.

## 🛡 Protection

-   JWT signé
-   Expiration des tokens
-   HttpOnly cookies
-   Rotation des tokens

------------------------------------------------------------------------

# 🧠 Checklist Sécurité Backend

✅ HTTPS activé\
✅ Validation des entrées\
✅ Hashing des mots de passe (bcrypt)\
✅ Rate limiting\
✅ Helmet middleware\
✅ Variables d'environnement protégées\
✅ Logs & Monitoring\
✅ Principe du moindre privilège

------------------------------------------------------------------------

# 🎯 Conclusion

La sécurité backend n'est pas une option.\
Elle doit être intégrée dès la conception de l'application.

Penser toujours comme un attaquant : "Comment pourrais-je casser ce
système ?"

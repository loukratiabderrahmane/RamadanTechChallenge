# 🚀 Jour 9 --- ORM Advanced Concepts

------------------------------------------------------------------------

# 📌 1️⃣ Introduction aux ORM

Un **ORM (Object Relational Mapping)** est une technique permettant de
manipuler une base de données relationnelle (MySQL, PostgreSQL...) à
travers des objets du langage (JavaScript, Java, Python).

Au lieu d'écrire :

``` sql
SELECT * FROM users WHERE id = 1;
```

On écrit :

``` js
User.findByPk(1);
```

L'ORM génère automatiquement la requête SQL.

------------------------------------------------------------------------

# 🧠 2️⃣ Mapping Objet ↔ Relationnel

  Base de données   Code
  ----------------- -------------
  Table             Classe
  Ligne             Objet
  Colonne           Attribut
  Foreign Key       Association

------------------------------------------------------------------------

# ⚡ 3️⃣ Index

## Définition

Un index est une structure de données (souvent B-Tree) permettant
d'accélérer les recherches.

Sans index → Scan complet\
Avec index → Recherche rapide

## Exemple

``` sql
CREATE INDEX idx_email ON users(email);
```

## Bonnes pratiques

-   Indexer les colonnes utilisées dans WHERE, JOIN, ORDER BY.
-   Éviter trop d'index (ralentit INSERT/UPDATE).
-   Utiliser EXPLAIN pour analyser les requêtes.

------------------------------------------------------------------------

# 🔐 4️⃣ Transactions

Une transaction garantit que plusieurs opérations sont exécutées
totalement ou annulées totalement.

## Principe ACID

-   Atomicité
-   Cohérence
-   Isolation
-   Durabilité

## Exemple Sequelize

``` js
const t = await sequelize.transaction();

try {
   await User.update(..., { transaction: t });
   await Account.update(..., { transaction: t });

   await t.commit();
} catch (error) {
   await t.rollback();
}
```

------------------------------------------------------------------------

# 💤 5️⃣ Lazy vs Eager Loading

## Lazy Loading

Charge les relations seulement quand nécessaire.

``` js
const posts = await user.getPosts();
```

## Eager Loading

Charge les relations directement avec JOIN.

``` js
User.findAll({
   include: Post
});
```

------------------------------------------------------------------------

# 🚨 6️⃣ N+1 Query Problem

## Problème

1 requête pour récupérer les users\
+ N requêtes pour récupérer les relations

Total = N+1 requêtes

## Solution

Utiliser Eager Loading :

``` js
User.findAll({
   include: Post
});
```

------------------------------------------------------------------------

# ⚙️ 7️⃣ Optimisation ORM

## 1. Sélectionner uniquement les colonnes nécessaires

``` js
User.findAll({
   attributes: ['id', 'name']
});
```

## 2. Pagination obligatoire

``` js
User.findAll({
   limit: 10,
   offset: 0
});
```

## 3. Indexer intelligemment

Indexer les colonnes souvent filtrées.

## 4. Comprendre le SQL généré

Toujours analyser les requêtes et surveiller les performances.

------------------------------------------------------------------------

# 🎓 8️⃣ Bonnes pratiques Senior

✔ Comprendre le SQL généré\
✔ Utiliser des transactions pour opérations critiques\
✔ Surveiller les requêtes lentes\
✔ Éviter le N+1\
✔ Mélanger ORM + SQL brut si nécessaire

------------------------------------------------------------------------

# 🏆 Conclusion

Un ORM est un outil puissant, mais il ne remplace pas la compréhension
des bases de données.

Un développeur senior :

-   Comprend la base relationnelle
-   Sait optimiser
-   Sait quand utiliser SQL brut
-   Analyse la performance




Ramadan Tech Challenge 🌙\
Jour 09 -- ORM Advanced Concepts 🚀

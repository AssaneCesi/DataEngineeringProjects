# Projet d'Analyse YouTube de Données par Assane Thiaw

## Introduction
Ce projet vise à collecter, rationaliser et stocker des données structurées et semi-structurées de vidéos YouTube afin d'effectuer des analyses pertinentes. L'objectif est de répondre à des questions comme : **qu'est-ce qui rend une vidéo populaire ?**

---

## Métriques Clés
### Métriques liées aux vidéos
Voici les métriques que nous souhaitons analyser sur notre dataset :

- **Vues moyennes par vidéo** : Moyenne des vues obtenues par chaque vidéo.
- **Taux d'engagement** : Calculé comme ceci : `(likes + commentaires) / vues`. Permet de mesurer l'interaction des utilisateurs avec le contenu.
- **Top vidéos par région** : Vidéos ayant le plus grand nombre de vues dans chaque région.
- **Durée moyenne en tendance** : Nombre moyen de jours où une vidéo reste dans la liste des tendances.
- **Distribution des catégories** : Nombre et pourcentage de vidéos dans chaque catégorie.
- **Ratio likes/dislikes** : Permet de comprendre la réception du contenu par les utilisateurs.

---

## Objectifs du Projet
1. **Ingestion des Données** : Construire un mécanisme pour ingérer des données provenant de différentes sources.
2. **Évolutivité** : Garantir que notre système puisse évoluer avec l'augmentation de la taille des données.
3. **Utilisation du Cloud** : Exploiter les services AWS pour traiter de grandes quantités de données.
4. **Reporting** : Construire un tableau de bord pour visualiser les insights identifiés.

---

## Services Utilisés
1. **Amazon S3** : Stockage des données de manière scalable et sécurisée.
2. **AWS IAM** : Gestion sécurisée des accès aux services AWS.
3. **QuickSight** : Création de tableaux de bord interactifs pour l'analyse des données.
4. **AWS Glue** : Préparation et transformation des données via des workflows ETL.
5. **AWS Lambda** : Automatisation de traitements sans gestion de serveur.
6. **AWS Athena** : Interrogation interactive des données directement sur S3.

---

## Jeu de Données Utilisé
Le dataset utilisé provient de [Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new) et contient des statistiques sur les vidéos YouTube populaires quotidiennement pour plusieurs régions. Les données incluent :

- **Colonnes principales** : titre de la vidéo, nom de la chaîne, heure de publication, tags, vues, likes, dislikes, description, et commentaires.
- **Fichiers JSON associés** : contiennent des informations supplémentaires comme `category_id`.

**Séparation des Données :**
- Les fichiers JSON et CSV sont stockés séparément dans des buckets S3 à l'aide de commandes adaptées.

---

## Diagramme d'Architecture
Voici l'architecture générale utilisée pour ce projet :

![Diagramme d'Architecture](architecture.jpeg)

### Étapes Clés :
1. Stockage des datasets bruts sur S3.
2. Préparation des données via des workflows ETL sur AWS Glue.
3. Création de tables et d'un catalogue de données avec AWS Glue Crawlers.
4. Requêtage des tables avec AWS Athena pour effectuer des analyses.
5. Création d'un deuxième ETL pour optimiser les performances et éviter les jointures coûteuses à long terme.
6. Analyse finale et visualisation des données avec Amazon QuickSight.

---

## Résultats de l'Analyse

### **Graphique 1 : Nombre de Likes par Catégorie**
Ce graphique met en évidence les catégories de vidéos qui génèrent le plus d'engagement :

- **"People & Blogs"** domine largement, reflétant une forte popularité.
- **"Entertainment" et "Music"** suivent avec un engagement important.
- Catégories moins populaires : "How-to & Style" et "Gaming".

![Nombre de Likes par Catégorie](count-of-likes-by-snt.jpg)

---

### **Graphique 2 : Somme des Vues par Catégorie**
Ce graphique en camembert illustre la répartition des vues par catégorie :

- **"Music"** attire l’audience la plus massive.
- **"Entertainment"** arrive en deuxième position.
- Les catégories "Science & Technology" et "Film & Animation" ont une présence notable.

![Somme des Vues par Catégorie](sum_of_view_by_sn.jpg)

---

### **Graphique 3 : Somme des Vues par Région**
Ce graphique montre la répartition des vues entre trois régions (États-Unis, Royaume-Uni, Canada) :

- **Royaume-Uni** : Représente la majorité des vues.
- **États-Unis** : Arrive en deuxième position.
- **Canada** : A la plus petite part des vues parmi les trois régions.

![Somme des Vues par Région](sumofview_by_rg.jpg)

---

## Synthèse

Ces analyses permettent de tirer des conclusions clés sur les préférences des spectateurs :

1. **Catégories dominantes** : "People & Blogs" et "Music" génèrent le plus d'engagement.
2. **Répartition régionale** : Le Royaume-Uni domine en termes de vues, suivi des États-Unis et du Canada.
3. **Opportunités pour les créateurs** : Focalisez-vous sur les catégories populaires tout en explorant des niches comme "Science & Technology".

Ces insights offrent une base solide pour maximiser l'impact des vidéos sur YouTube selon les préférences des spectateurs et leur localisation.

---

**Notes :** Retrouvez les scripts ETL et les codes AWS Lambda associés dans les fichiers mentionnés pour plus de détails.


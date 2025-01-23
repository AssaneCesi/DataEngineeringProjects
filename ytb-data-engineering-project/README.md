# Projet d'Analyse YouTube de Données par Assane Thiaw

## Introduction
Ce projet vise à gérer en toute sécurité, rationaliser et effectuer des analyses sur les données structurées et semi-structurées des vidéos YouTube, en se basant sur les catégories de vidéos et les métriques de tendance.

## Métriques
### Métriques liéees aux videos
    - Vues moyennes par vidéo : Moyenne des vues obtenues par chaque vidéo.
    - Taux d'engagement :
    Calculé comme ceci : (likes + commentaires) / vues.
    Permet de mesurer l'interaction des utilisateurs avec le contenu.
    - Top vidéos par région :
    Vidéos ayant le plus grand nombre de vues dans chaque région.
    - Durée moyenne en tendance :
    Nombre moyen de jours où une vidéo reste dans la liste des tendances.
    - Distribution des catégories :
    Nombre et pourcentage de vidéos dans chaque catégorie.
    - Ratio likes/dislikes :
    Permet de comprendre la réception du contenu par les utilisateurs.

### Métriques liées aux chaînes
    - Top chaînes par nombre de vidéos tendances :Les chaînes ayant le plus grand nombre de vidéos apparaissant dans les tendances.
    - Popularité moyenne par chaîne :Moyenne des vues, likes et commentaires par vidéo pour chaque chaîne.
    - Diversité des catégories par chaîne :Nombre de catégories dans lesquelles une chaîne publie des vidéos.

### Métriques liées aux catégories
    - Catégorie la plus populaire par région :Basée sur le total des vues ou du temps passé en tendance.
    - Taux d'engagement par catégorie :(likes + commentaires) / vues pour chaque catégorie.
    - Croissance des tendances par catégorie :Analyse des catégories qui deviennent plus fréquentes dans les tendances au fil du temps.

### Métriques temporelles
    - Heure optimale de publication :Heures où les vidéos publiées reçoivent le plus de vues ou d'engagement.
    - Jour de la semaine avec le plus d'engagement :Identifier les jours où les vidéos tendances génèrent le plus d'interactions.
    - Saisonnalité des tendances :Analyse des variations dans les vues ou les engagements selon les mois ou saisons.

### Métriques temporelles
    - Comparaison des tendances par région :Vidéos, catégories ou chaînes populaires par région.
    - Taux d'engagement par région : Mesurer l'interaction moyenne des utilisateurs dans différentes régions.

## Objectifs du Projet
1. **Ingestion des Données** — Construire un mécanisme pour ingérer des données provenant de différentes sources.
2. **Système ETL** — Nous recevons des données brutes, qu'il faut transformer en un format approprié.
3. **Lac de Données** — Comme nous recevrons des données de multiples sources, nous avons besoin d'un référentiel centralisé pour les stocker.
4. **Évolutivité** — Au fur et à mesure que la taille des données augmente, nous devons nous assurer que notre système évolue en conséquence.
5. **Cloud** — Nous ne pouvons pas traiter de vastes quantités de données sur un ordinateur local, nous devons donc utiliser le cloud, dans ce cas, AWS.
6. **Reporting** — Construire un tableau de bord pour répondre aux questions posées précédemment.

## Services Utilisés
1. **Amazon S3** : Amazon S3 est un service de stockage d'objets offrant une évolutivité, une disponibilité des données, une sécurité et des performances élevées.
2. **AWS IAM** : AWS Identity and Access Management (IAM) permet de gérer de manière sécurisée l'accès aux services et ressources AWS.
3. **QuickSight** : Amazon QuickSight est un service de business intelligence (BI) évolutif, sans serveur, et alimenté par le machine learning, conçu pour le cloud.
4. **AWS Glue** : Un service d'intégration de données sans serveur qui facilite la découverte, la préparation et la combinaison de données pour l'analyse, le machine learning et le développement d'applications.
5. **AWS Lambda** : Lambda est un service de calcul permettant d'exécuter du code sans créer ni gérer de serveurs.
6. **AWS Athena** : Athena est un service de requête interactive pour S3, dans lequel il n'est pas nécessaire de charger les données puisqu'elles restent dans S3.

## Jeu de Données Utilisé
Ce jeu de données Kaggle contient des statistiques (fichiers CSV) sur les vidéos YouTube populaires quotidiennes sur plusieurs mois. Jusqu'à 200 vidéos tendance sont publiées chaque jour pour plusieurs régions. Les données pour chaque région sont dans un fichier distinct. Les informations incluent le titre de la vidéo, le nom de la chaîne, l'heure de publication, les tags, les vues, les likes, les dislikes, la description et le nombre de commentaires. Un champ **category_id**, qui varie selon la région, est également inclus dans le fichier JSON associé.

[Jeu de données Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new)

## Diagramme d'Architecture
![Diagramme d'Architecture](architecture.jpeg)

## Résultats


## **Graphique 1 : Nombre de Likes par Catégorie**
Ce graphique montre le nombre total de likes reçus par les vidéos dans différentes catégories. Voici les points clés :
- **Catégorie "People & Blogs"** : Cette catégorie domine largement avec le plus grand nombre de likes, ce qui reflète une forte popularité et un engagement élevé des spectateurs pour les contenus personnels ou informels.
- **Catégories "Entertainment" et "Music"** : Elles occupent respectivement la deuxième et la troisième place, confirmant l'attrait des contenus de divertissement et musicaux auprès du public.
- **Catégories moins populaires** : Les catégories telles que "How-to & Style" et "Gaming" reçoivent relativement peu de likes, indiquant un engagement moindre ou une audience plus ciblée.

![Nombre de Likes par Catégorie](count-of-likes-by-snt.jpg) 

---

## **Graphique 2 : Somme des Vues par Catégorie**
Ce graphique en camembert illustre la répartition des vues par catégorie. Voici les principales observations :
- **Catégorie "Music"** : Elle représente la plus grande part des vues, confirmant que les vidéos musicales attirent une audience massive.
- **Catégorie "Entertainment"** : Elle se classe en deuxième position, montrant un attrait similaire à celui des vidéos musicales.
- **"Science & Technology" et "Film & Animation"** : Ces catégories ont une présence notable, montrant que le contenu éducatif et créatif suscite un intérêt considérable.
- **Autres catégories** : Les catégories comme "Sports" ou "Travel & Events" ont une part beaucoup plus petite, suggérant un public plus spécialisé.

![Somme des Vues par Catégorie](sum_of_view_by_sn.jpg)

---

## **Graphique 3 : Somme des Vues par Région**
Ce graphique montre la répartition des vues par région (États-Unis, Royaume-Uni, Canada). Voici ce qui en ressort :
- **Royaume-Uni (GB)** : Cette région représente la majorité des vues, ce qui pourrait être dû à un plus grand volume de contenu produit ou à une audience plus active sur YouTube.
- **États-Unis (US)** : Cette région se classe deuxième, avec une part importante, reflétant la large adoption de YouTube dans ce marché.
- **Canada (CA)** : Cette région a la plus petite part des vues parmi les trois, indiquant un public légèrement plus restreint ou une moindre activité sur la plateforme.

![Somme des Vues par Région](sumofview_by_rg.jpg)

---

## **Synthèse**
Ces graphiques offrent des informations clés sur les préférences des spectateurs en termes de catégories et leur répartition géographique :
1. **Préférences des catégories** :
   - "People & Blogs" et "Music" se démarquent par leur capacité à générer beaucoup d'engagement (likes) et d'audience (vues).
2. **Répartition géographique** :
   - Le Royaume-Uni domine en termes de vues, suivi par les États-Unis et le Canada.
3. **Insights pour les créateurs** :
   - Les créateurs devraient se concentrer sur les catégories populaires (comme "Music" et "Entertainment") tout en explorant des niches émergentes comme "Science & Technology".

Ces analyses mettent en lumière des opportunités pour maximiser l'impact des vidéos sur YouTube selon les préférences des spectateurs et leur localisation.

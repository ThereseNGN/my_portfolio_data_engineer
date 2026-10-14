# Portfolio — Projets Data Engineering

Ce portfolio présente une sélection de projets réalisés dans le cadre de ma reconversion vers le Data Engineering. Chaque fiche décrit le besoin, ma contribution, les choix techniques, les résultats et les limites du projet.

Les réalisations mettent en évidence des compétences en programmation, modélisation et gestion des données, avec une attention particulière à la fiabilité des traitements et à leur validation.

## Projets à découvrir

| Projet                                                  | Objectif                                                                              | Compétences illustrées                                               | Cadre                                                   |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------- |
| [Analyse ferroviaire avec Spark](projets/spark-trains)  | Analyser 7 200 trajets et produire des indicateurs de fréquentation et de ponctualité | PySpark DataFrame, Spark SQL, agrégations, règles métier             | TP individuel évalué Ingénieur Data & IA                |
| [Analyse des ventes avec Hadoop](projets/hadoop-ventes) | Agréger des quantités par ville et année et comparer plusieurs traitements            | HDFS, Hadoop Streaming, Python, HBase / HappyBase, Hive, Docker      | TP individuel évalué Ingénieur Data & IA                |
| [MyFamilyAppli](projets/myfamilyappli)                  | Centraliser l’organisation familiale dans une application web                         | Modélisation relationnelle, SQL / MySQL, API, développement et tests | Projet individuel Concepteur Développeur d'Applications |

## Analyse ferroviaire — PySpark et Spark SQL

TP individuel réalisé dans Databricks : chargement et exploration d’un CSV de 7 200 trajets, puis calcul d’indicateurs par gare, ligne, type de train et compagnie. Les 21 exercices illustrent l’usage de PySpark DataFrame et de Spark SQL, avec une attention au périmètre des indicateurs et à l’interprétation des résultats.

- [Consulter la fiche et les principaux résultats](projets/spark-trains/README.md)
- [Examiner le notebook avec ses résultats](projets/spark-trains/notebooks/TP-Trains-compte-rendu.ipynb)

Ce TP démontre une pratique de Spark sur des données tabulaires, sans revendiquer une expérience à grande échelle dû au volume pédagogique.

## Analyse des ventes — Hadoop, HBase et Hive

TP individuel réalisé dans un cluster Docker pédagogique : stockage HDFS, agrégations MapReduce en Python, stockage des totaux dans HBase et analyse SQL avec Hive. Le projet illustre la complémentarité des composants et le diagnostic d’une erreur de classement liée aux clés contenant des espaces.

- [Consulter la fiche et les résultats](projets/hadoop-ventes/README.md)
- [Examiner les preuves d’exécution](projets/hadoop-ventes/docs/compte-rendu-TP.pdf)
- [Lire les mappers et reducers](projets/hadoop-ventes/src/)

## MyFamilyAppli — du besoin à l’application

Application de gestion familiale développée avec React, Node.js / Express et MySQL. Le projet permet d’examiner la conception d’une base relationnelle, les échanges entre une interface et une API, ainsi que la validation du fonctionnement par des tests.

- [Consulter la fiche du projet](projets/myfamilyappli/README.md)
- [Consulter la présentation](projets/myfamilyappli/Presentation_MFA.pdf)
- [Accéder au code source](https://github.com/ThereseNGN/my_family_appli.git)

Ce projet apporte une preuve de réalisation applicative complète. Les compétences présentées constituent un socle pour le Data Engineering.

## Comment explorer les réalisations

Les fiches proposent une lecture en deux temps : une vue d’ensemble du besoin et du résultat, puis les éléments techniques permettant d’examiner la réalisation.

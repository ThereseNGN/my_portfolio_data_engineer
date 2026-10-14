# Résultats et contrôles

## Top 10 issu de HBase

| Rang | Ville                 | Articles commandés |
| ---- | --------------------- | -----------------: |
| 1    | LE MANS               |              3 019 |
| 2    | CAEN                  |              2 056 |
| 3    | FLERS                 |              1 480 |
| 4    | LAVAL                 |              1 422 |
| 5    | VIRE NORMANDIE        |              1 405 |
| 6    | CHERBOURG EN COTENTIN |              1 362 |
| 7    | ALENCON               |              1 166 |
| 8    | ARGENTAN              |                938 |
| 9    | RENNES                |                874 |
| 10   | ATHIS VAL DE ROUVRE   |                809 |

Valeurs retranscrites de la capture `top10.txt` du rapport, sans fichier original ni recalcul sur la source. Le classement montre des quantités d’articles, pas une mesure du chiffre d’affaires.

## Comparaison ciblée

| Ville          | MapReduce | HBase | Graphique | Observation |
| -------------- | --------: | ----: | --------: | ----------- |
| LE MANS        |     3 019 | 3 019 |     3 019 | Concordance |
| CAEN           |     2 056 | 2 056 |     2 056 | Concordance |
| FLERS          |     1 480 | 1 480 |     1 480 | Concordance |
| LAVAL          |     1 422 | 1 422 |     1 422 | Concordance |
| VIRE NORMANDIE |     1 405 | 1 405 |     1 405 | Concordance |

## Ville et année

Le Top 5 MapReduce corrigé contient BEAUFORT EN VALLEE#2012 et LE MANS#2010 à 305 articles, LE MANS#2006 à 267, LE MANS#2011 à 262 et LE MANS#2015 à 258. Hive retrouve ces cinq clés et quantités. L’ordre des deux premières peut varier parce qu’elles sont ex æquo.

## Nombre de lignes et rejets

Le rapport annonce 135 278 lignes dans la source, en-tête compris. La capture de préparation TSV affiche `lues : 135278`, `ecrites : 135277`, `ecartees : 3` et `annees absentes (NULL Hive) : 2`. Hive affiche 135 277 lignes.

Ces compteurs ne suffisent pas à expliquer une réconciliation exacte : il faut connaître la définition de chaque compteur et les lignes rejetées. La fiche ne présente donc pas les compteurs comme une preuve de complétude ou d’absence de perte.

## Conclusions permises

LE MANS arrive en tête des classements visibles. La chaîne produit des résultats consultables et combine traitements Python, stockage NoSQL et requêtes SQL.

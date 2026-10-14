-- Requêtes visibles dans le rapport ; fichier regroupé pour le portfolio.
-- Le TSV et le cluster pédagogique ne sont pas fournis dans ce pack.
CREATE DATABASE IF NOT EXISTS ventes_db;
USE ventes_db;
CREATE EXTERNAL TABLE IF NOT EXISTS ventes (
    ville STRING,
    annee INT,
    qte INT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
LOCATION '/user/root/input/TP-Q4';

-- Q1 : total d'articles par ville, et non nombre de commandes.
SELECT ville, SUM(qte) AS total_articles
FROM ventes
GROUP BY ville
ORDER BY total_articles DESC
LIMIT 10;

-- Q2 : total d'articles par ville et année.
SELECT CONCAT(ville, '#', CAST(annee AS STRING)) AS ville_annee,
       SUM(qte) AS total_articles
FROM ventes
WHERE annee IS NOT NULL
GROUP BY ville, annee
ORDER BY total_articles DESC
LIMIT 10;

-- Exploration du plan.
EXPLAIN SELECT ville, SUM(qte) AS total_articles
FROM ventes
GROUP BY ville
ORDER BY total_articles DESC
LIMIT 10;

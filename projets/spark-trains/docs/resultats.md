# Résultats et interprétation

## Périmètre

7 200 trajets, dont 6 943 non annulés et 257 annulés. Le CSV comporte 10 gares de départ, 3 compagnies, 3 types de trains et 90 lignes directionnelles. Les dates vont du 1er janvier au 31 décembre 2026 dans ce jeu pédagogique ; elles ne prouvent pas des observations réelles sur cette période.

## Résultats marquants

| Question | Résultat |
| --- | --- |
| Gare avec le plus de trajets non annulés | Lyon : 702 |
| Gare avec le plus de passagers au départ | Strasbourg : 246 226 |
| Ligne avec le plus de passagers | Lyon → Strasbourg : 30 115 |
| Taux de retards > 15 min le plus élevé par gare | Marseille : 42,17 % |
| Deuxième taux de retards > 15 min par gare | Strasbourg : 40,60 % |
| Retard moyen le plus élevé par ligne | Marseille → Rennes : 23,19 min sur 75 trajets |
| Retard moyen de l’ensemble des trajets non annulés | 14,84 min |

Les deux classements de gares ne répondent pas à la même question : Lyon a le plus de trajets, tandis que Strasbourg cumule le plus de passagers. Une ligne très fréquentée n’est pas nécessairement la plus retardée : Lyon → Strasbourg a un retard moyen de 12,17 minutes, inférieur à celui de Marseille → Rennes.

## Définition des indicateurs

- `numberTrips` : nombre de trajets du périmètre considéré.
- `totalPassengers` : somme des passagers par trajet ; les voyageurs ne sont pas dédupliqués.
- `avgDelay` : moyenne du retard des trajets non annulés, arrondie à deux décimales.
- `delayedTrips` : nombre de trajets non annulés avec `delay_min > 15`.
- `delayRate` : `100 × delayedTrips / numberTrips`, calculé sur les trajets non annulés.

Les exercices 17 et 18 comptent tous les trajets, tout en calculant le retard moyen sur les seuls trajets non annulés. Pour les gares et les lignes, les indicateurs présentés concernent les trajets non annulés.

## Classification des retards

| Catégorie | Règle | Trajets non annulés |
| --- | --- | ---: |
| On time | 0 à 5 min | 2 934 |
| Small delay | Plus de 5 à 15 min | 1 829 |
| Medium delay | Plus de 15 à 30 min | 1 424 |
| Large delay | Plus de 30 min | 756 |

Les catégories `Medium delay` et `Large delay` regroupent 2 180 trajets. La catégorie `On time` du sujet accepte jusqu’à 5 minutes de retard ; elle ne signifie pas une arrivée exactement à l’heure.

## Limites de l’interprétation

Le seuil de 30 trajets ne retire aucune ligne de ce jeu. Il ne constitue pas un test de significativité. Les agrégats seuls ne permettent pas de distinguer les effets de la période, du type de train, de la compagnie ou de la composition des trajets par gare. Il faudrait explorer ces dimensions avant d’attribuer des causes aux différences observées.

Voir les tables complètes : [gares](../resultats/indicateurs-gares.csv) et [lignes](../resultats/rapport-lignes.csv).

# Données du TP

`trains.csv` est le jeu fourni avec l’énoncé du TP évalué. Il contient 7 200 lignes et 11 colonnes. Aucune provenance opérationnelle ou licence de redistribution n’est précisée dans les fichiers fournis ; il est présenté ici comme un jeu pédagogique, sans l’attribuer à des données ouvertes SNCF.

| Colonne | Description |
| --- | --- |
| `trip_id` | Identifiant du trajet |
| `date` | Date du trajet |
| `departure_station` | Gare de départ |
| `arrival_station` | Gare d’arrivée |
| `company` | Compagnie |
| `train_type` | Type de train |
| `distance_km` | Distance en kilomètres |
| `duration_min` | Durée en minutes |
| `passengers` | Nombre de passagers du trajet |
| `delay_min` | Retard à l’arrivée en minutes |
| `cancelled` | Annulation : Yes ou No |

Le fichier utilise la virgule comme séparateur et possède un en-tête. Les annulations sont codées par `Yes` / `No`. Dans le CSV fourni, les trajets annulés ont zéro passager, zéro durée et zéro retard : inclure leurs retards dans une moyenne réduirait artificiellement celle-ci.

# Dictionnaire des données

Dictionnaire établi dans le rapport, avec des types logiques à valider avec le métier. Le CSV complet n’est pas inclus dans ce pack.

| Colonne   | Type logique  | Description                                  |
| --------- | ------------- | -------------------------------------------- |
| codcli    | Entier        | Identifiant du client                        |
| genrecli  | Texte         | Civilité du client                           |
| nomcli    | Texte Capital | Nom du client                                |
| prenomcli | Texte         | Prénom du client                             |
| cpcli     | Texte         | Code postal du client                        |
| villecli  | Texte Capital | Ville du client                              |
| codcde    | Entier        | Identifiant de la commande                   |
| datcde    | Date et heure | Date de la commande                          |
| timbrecli | Décimal       | Montant d'affranchissement associé au client |
| timbrecde | Décimal       | Montant d'affranchissement de la commande    |
| Nbcolis   | Entier        | Nombre de colis de la commande               |
| cheqcli   | Décimal       | Montant associé au règlement par chèque      |
| barchive  | Booléen       | Indicateur d'archivage                       |
| bstock    | Booléen       | Indicateur lié au stock                      |
| codobj    | Entier        | Identifiant de l'article                     |
| qte       | Entier        | Quantité commandée pour l'article            |
| Colis     | Entier        | Numéro ou indicateur du colis                |
| libobj    | Texte         | Libellé de l'article                         |
| Tailleobj | Texte         | Taille ou variante de l'article              |
| Poidsobj  | Entier        | Poids de l'article                           |
| points    | Entier        | Nombre de points associé à l'article         |
| indispobj | Booléen       | Indicateur d'indisponibilité                 |
| libcondit | Texte         | Libellé du conditionnement                   |
| prixcond  | Entier        | Prix du conditionnement                      |
| puobj     | Décimal       | Prix unitaire de l'article                   |

## Colonnes utilisées dans les calculs

- `villecli` : clé d’agrégation par ville.
- `datcde` : extraction de l’année pour la clé composite.
- `qte` : quantité d’articles à sommer.

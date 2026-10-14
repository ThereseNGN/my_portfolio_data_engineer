# mapper Q1, sans réexécution Hadoop.
import csv
import sys

csv_reader = csv.reader(sys.stdin, delimiter=",")
for row in csv_reader:
    # Ignorer les lignes incomplètes et l'en-tête
    if len(row) < 16 or row[0] == "codcli":
        continue

    ville = row[5].strip()  # colonne villecli
    quantite_str = row[15].strip()  # colonne qte
    try:
        quantite = int(quantite_str)
    except ValueError:
        continue

    if ville:
        print(f"{ville}\t{quantite}")

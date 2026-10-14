# Mapper Q2, sans réexécution Hadoop.
import csv
import sys

csv_reader = csv.reader(sys.stdin, delimiter=",")
for row in csv_reader:
    if len(row) < 16 or row[0] == "codcli":
        continue
    ville = row[5].strip()
    date_commande = row[7].strip()
    quantite_str = row[15].strip()
    annee = date_commande[:4]
    try:
        quantite = int(quantite_str)
    except ValueError:
        continue
    if ville and len(annee) == 4 and annee.isdigit():
        print(f"{ville}#{annee}\t{quantite}")

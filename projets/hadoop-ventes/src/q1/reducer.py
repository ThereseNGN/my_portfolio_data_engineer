# Reducer Q1.
# Entrée attendue : lignes triées par clé, au format clé TAB quantité.
import sys

current_city = None
total_quantity = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t", 1)

    if len(parts) < 2:
        continue

    city, quantity_str = parts

    try:
        quantity = int(quantity_str)
    except ValueError:
        continue

    if city == current_city:
        total_quantity += quantity
        
    else:
        if current_city is not None:
            print(f"{current_city}\t{total_quantity}")
        current_city = city
        total_quantity = quantity
if current_city is not None:
    print(f"{current_city}\t{total_quantity}")

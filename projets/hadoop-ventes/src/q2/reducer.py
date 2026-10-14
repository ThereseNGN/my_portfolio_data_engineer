# Reducer Q2.
# Entrée attendue : lignes triées par clé, au format clé TAB quantité.
import sys

current_composite_key = None
total_quantity = 0
for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t", 1)
    if len(parts) < 2:
        continue
    composite_key, quantity_str = parts
    try:
        quantity = int(quantity_str)
    except ValueError:
        continue
    if composite_key == current_composite_key:
        total_quantity += quantity
    else:
        if current_composite_key is not None:
            print(f"{current_composite_key}\t{total_quantity}")
        current_composite_key = composite_key
        total_quantity = quantity
if current_composite_key is not None:
    print(f"{current_composite_key}\t{total_quantity}")

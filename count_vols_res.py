import json 

with open("./db/json/data_final.json", "r") as f: data_json = json.load(f)

reservations_count = 0
no_reservations_count = 0
for vol in data_json.values():
  if len(vol["reservations"]) > 0:
    reservations_count += 1
  else:
    no_reservations_count += 1

print(f"Nombre de vols avec des réservations: {reservations_count}")
print(f"Nombre de vols sans réservations: {no_reservations_count}")
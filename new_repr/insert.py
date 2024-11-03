import json
from config.connectionRedis import connect_redis

with open("./db/json/data_final.json", "r") as f: data_json = json.load(f)

r = connect_redis()

# Insérer chaque vol comme une chaîne JSON dans Redis
for num_vol, vol_data in data_json.items():
  # Créer une clé unique pour chaque vol
  key = f"vol:{num_vol}"
  
  # Stocker le document JSON sous forme de chaîne
  try:
    r.set(key, json.dumps(vol_data))
    print(f"Données pour le vol {num_vol} insérées avec succès.")
  except Exception as e:
    print(f"Erreur lors de l'insertion des données pour le vol {num_vol}: {e}")

print("Insertion terminée.")
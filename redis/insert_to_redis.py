import json
from redis import Redis

# Charger le fichier JSON pour l'utiliser avec Redis
with open("./db/json/data_final.json", "r") as f: data_json = json.load(f)

r = Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Insérer chaque vol dans Redis en tant que document JSON unique
for num_vol, vol_data in data_json.items():
  # Créer une clé unique pour chaque vol
  key = f"vol:{num_vol}"
  
  # Insérer tout le document vol dans Redis comme un JSON unique
  r.execute_command('JSON.SET', key, '.', json.dumps(vol_data))
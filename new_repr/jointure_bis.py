import json
import sys
import os

# Ajouter le chemin du fichier jointure et des autres modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.divide_data import divide_data_in_2_parts as divide_data
from lib.jointure import my_join
from config.connectionRedis import connect_redis

# Connexion à Redis
r = connect_redis()

def parse_redis_data(keys):
  """Récupère et parse les données JSON depuis Redis en utilisant les clés données."""
  parsed_data = {}
  for key in keys:
    value = r.get(key)
    parsed_data[key] = json.loads(value) if value else {}
  return parsed_data

if __name__ == "__main__":
  # Récupérer tous les documents de Redis et parser
  keys = r.keys("vol:*")
  vols = parse_redis_data(keys)

  # Diviser les données
  doc1, doc2 = divide_data(vols, output=False)

  # Jointure sur l'attribut souhaité
  join_attr3 = "DateD"
  print(f"\nJoin on {join_attr3}:")
  my_join(doc1, doc2, join_attr3, "./db/json/join_dateD.json")
  print("\n--------------")

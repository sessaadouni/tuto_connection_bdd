import json
import sys
import os

# Ajouter le chemin du fichier jointure et des autres modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.connectionRedis import connect_redis

# Connexion à Redis
r = connect_redis()

# Exemple : Fonction pour lister les villes d'arrivée des vols
def get_arrival_cities():
  keys = r.keys("vol:*")
  arrival_cities = {json.loads(r.get(key)).get('VilleA') for key in keys if r.get(key)}
  return list(filter(None, arrival_cities))

# Exemple : Fonction pour compter les pilotes dont le nom contient une lettre donnée
def count_pilots_by_letter(letter):
  keys = r.keys("vol:*")
  count = sum(
    1 for key in keys
    if (pilot_name := json.loads(r.get(key)).get('pilote', {}).get('NomPil')) and letter.lower() in pilot_name.lower()
  )
  return count

# Appel des fonctions de manipulation
print("Villes d'arrivée des vols :", get_arrival_cities())
print("Nombre de pilotes avec la lettre 'A' dans leur nom :", count_pilots_by_letter("A"))

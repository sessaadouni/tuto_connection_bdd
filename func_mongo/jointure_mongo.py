import json
import sys
import os

# Ajouter le chemin du fichier jointure et des autres modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.divide_data import divide_data_in_2_parts as divide_data
from lib.jointure import my_join
from config.connectionMongo import connect_mongodb

client = connect_mongodb()

# Nom de la base de données
db = client["FlightDB"]  

# Nom de la collection
collection = db["vols"]  

def parse_mongo_data(raw_data):
  parsed_data = {}
  for doc in raw_data:
    doc_id = doc.pop("_id")  # Utilise l'ID du document comme clé
    parsed_data[doc_id] = doc
  return parsed_data

if __name__ == "__main__":
  # Récupérer tous les documents de MongoDB et les parser
  vols_raw = list(collection.find({}))
  vols = parse_mongo_data(vols_raw)

  # Diviser les données
  doc1, doc2 = divide_data(vols, output=False)

  # Afficher les documents pour vérification
  # print("Document 1:", json.dumps(doc1, indent=2))
  # print("Document 2:", json.dumps(doc2, indent=2))

  # Jointure sur l'attribut souhaité
  join_attr3 = "VilleD"
  print(f"\nJoin on {join_attr3}:")
  my_join(doc1, doc2, join_attr3, "./db/json/join_villeD.json")
  print("\n--------------")
import json
from pymongo import MongoClient # type: ignore

# Charger le fichier JSON pour l'utiliser avec MongoDB
with open("./db/json/data_final.json", "r") as f: data_json = json.load(f)

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Nom de la base de données
db = client["FlightDB"]  

# Nom de la collection
collection = db["vols"]  

# Supprimer les anciens documents dans la collection (facultatif)
collection.delete_many({})

# Insérer chaque vol dans MongoDB en tant que document unique
for num_vol, vol_data in data_json.items():
  # Ajouter le numéro de vol comme un champ pour identifier chaque document
  vol_data["_id"] = num_vol
  
  # Insérer le document dans MongoDB
  collection.insert_one(vol_data)
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.connectionMongo import connect_mongodb

client = connect_mongodb()

# Nom de la base de données
db = client["FlightDB"]  

# Nom de la collection
collection = db["vols"]  

# Exemple : Fonction pour lister les villes d'arrivée des vols
def get_arrival_cities():
  # Utiliser une requête distincte pour obtenir les villes d'arrivée uniques
  arrival_cities = collection.distinct("VilleA")
  return list(filter(None, arrival_cities))

# Exemple : Fonction pour compter les pilotes dont le nom contient une lettre donnée
def count_pilots_by_letter(letter):
  # Rechercher les documents où le nom du pilote contient la lettre donnée
  query = {"pilote.NomPil": {"$regex": f".*{letter}.*", "$options": "i"}}
  count = collection.count_documents(query)
  return count

# Appel des fonctions de manipulation
print("Villes d'arrivée des vols :", get_arrival_cities())
print("Nombre de pilotes avec la lettre 'A' dans leur nom :", count_pilots_by_letter("A"))

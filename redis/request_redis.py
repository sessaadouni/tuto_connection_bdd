from redis import Redis

r = Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Exemple : Fonction pour lister les villes d'arrivée des vols
def get_arrival_cities():
  keys = r.keys("vol:*")
  arrival_cities = {r.execute_command('JSON.GET', key, '$.VilleA') for key in keys}
  return list(filter(None, arrival_cities))

# Exemple : Fonction pour compter les pilotes dont le nom contient une lettre donnée
def count_pilots_by_letter(letter):
  keys = r.keys("vol:*")
  count = sum(
    1 for key in keys
    if (pilot_name := r.execute_command('JSON.GET', key, '$.pilote.NomPil')) and letter.lower() in pilot_name.lower()
  )
  return count

# Appel des fonctions de manipulation
print("Villes d'arrivée des vols :", get_arrival_cities())
print("Nombre de pilotes avec la lettre 'A' dans leur nom :", count_pilots_by_letter("A"))

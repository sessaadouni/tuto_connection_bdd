from pandas import read_csv, merge # type: ignore
from json import dump

# Fonction pour charger un fichier TXT en DataFrame pandas
def load_txt_file(filepath, column_names):
  return read_csv(filepath, delimiter="\t", names=column_names)

# Charger les différents fichiers en DataFrames avec les colonnes spécifiées
avions_df = load_txt_file("./db/txt/AVIONS.txt", ["NumAv", "NomAv", "CapAv", "VilleAv"])
clients_df = load_txt_file("./db/txt/CLIENTS.txt", ["NumCl", "NomCl", "NumRuelCl", "NomRueCl", "CodePosteCl", "VileCl"])
defclasses_df = load_txt_file("./db/txt/DEFCLASSES.txt", ["NumVol", "Classe", "CoefPrix"])
pilotes_df = load_txt_file("./db/txt/PILOTES.txt", ["Numpil", "NomPil", "NaisPil", "VillePil"])
reservations_df = load_txt_file("./db/txt/RESERVATIONS.txt", ["NumCl", "NumVol", "Classe", "NbPlaces"])
vols_df = load_txt_file("./db/txt/VOLS.txt", ["NumVol", "VilleD", "VilleA", "DateD", "HD time", "DateA", "HA time", "NumPil", "NumAv"])

# Fusionner les données
vols_pilotes_df = merge(vols_df, pilotes_df, left_on="NumPil", right_on="Numpil", how="left")
vols_pilotes_avions_df = merge(vols_pilotes_df, avions_df, on="NumAv", how="left").drop(columns=["Numpil"])

# Fusion des réservations et des clients
reservations_clients_df = merge(reservations_df, clients_df, on="NumCl", how="left")

# Groupement des réservations par vol et transformation en liste
reservations_grouped = reservations_clients_df.groupby("NumVol", group_keys=False).apply(lambda x: x.to_dict(orient="records"), include_groups=False).to_dict()

# Ajout des réservations regroupées dans le DataFrame des vols
vols_pilotes_avions_df["reservations"] = vols_pilotes_avions_df["NumVol"].map(reservations_grouped)

# Remplir les valeurs NaN de "reservations" avec des dictionnaires vides
vols_pilotes_avions_df["reservations"] = vols_pilotes_avions_df["reservations"].apply(lambda x: x if isinstance(x, list) else {})

# Création de sous-structures pour avions et pilotes
vols_pilotes_avions_df["avion"] = vols_pilotes_avions_df[["NomAv", "CapAv", "VilleAv"]].to_dict(orient="records")
vols_pilotes_avions_df["pilote"] = vols_pilotes_avions_df[["NomPil", "NaisPil", "VillePil"]].to_dict(orient="records")

# Sélection des colonnes pertinentes et suppression des colonnes superflues
final_df = vols_pilotes_avions_df[["NumVol", "VilleD", "VilleA", "DateD", "HD time", "DateA", "HA time", "avion", "pilote", "reservations"]]

# Conversion en dictionnaire puis en JSON
result = final_df.set_index("NumVol").to_dict(orient="index")
with open("./db/json/data_final.json", "w") as f: dump(result, f, indent=2)

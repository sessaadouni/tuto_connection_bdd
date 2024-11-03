import json

def divide_data_in_2_parts(data, output=True):
  # Découpage des données en deux parties
  data_keys = list(data.keys())
  mid_index = len(data_keys) // 2
  data1 = {key: data[key] for key in data_keys[:mid_index]}
  data2 = {key: data[key] for key in data_keys[mid_index:]}
  
  # Sauvegarde des deux parties dans deux fichiers JSON distincts
  if output:
    with open("./db/json/data_part1.json", "w") as f: json.dump(data1, f, indent=2)
    with open("./db/json/data_part2.json", "w") as f: json.dump(data2, f, indent=2)
  
  return data1, data2

if __name__ == "__main__":
  with open("./db/json/data_final.json", "r") as f: data_json = json.load(f)
  divide_data_in_2_parts(data_json)
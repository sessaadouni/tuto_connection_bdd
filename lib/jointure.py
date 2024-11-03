import json

def my_join(doc1, doc2, join_attr, output_file=None):
  jointure_result = []
  count = 1
  for key1, record1 in doc1.items():
    for key2, record2 in doc2.items():
      if record1.get(join_attr) == record2.get(join_attr):
        # jointure_item = {**record1, **record2}
        # jointure_result.append(jointure_item)
        jointure_result.append((record1, record2))
        
        # optionnel : affichage les résultats dans le terminal
        print(f"Join #{count}:\nbetween {record1}\nand\t{record2}")
        count += 1
        print()
        
  if output_file is not None:
    with open(output_file, "w") as f: json.dump(jointure_result, f, indent=2)
  return jointure_result

if __name__ == "__main__":
  with open("./db/json/data_part1.json", "r") as file: doc1 = json.load(file)
  with open("./db/json/data_part2.json", "r") as file: doc2 = json.load(file)
  
  join_attr1 = "VilleAv"
  print(f"\nJoin on {join_attr1}:")
  my_join(doc1, doc2, join_attr1, "./db/json/join_villeAv.json")
  print("\n--------------")

  print()

  join_attr2 = "NomPil"
  print(f"\nJoin on {join_attr2}:")
  my_join(doc1, doc2, join_attr2, "./db/json/join_nomPil.json")
  print("\n--------------")
  
  print()
  
  join_attr3 = "DateA"
  print(f"\nJoin on {join_attr3}:")
  my_join(doc1, doc2, join_attr3, "./db/json/join_dateA.json")
  print("\n--------------")
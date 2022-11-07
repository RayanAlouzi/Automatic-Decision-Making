import json

def json_reader(file_name):
           with open(file_name) as f:
                  data = json.load(f)

           return data

print(json_reader("anime.json"))
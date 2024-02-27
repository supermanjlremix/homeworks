import json

with open("database.json", "r") as json_file:
    data = json.load(json_file)
print(data)
data['mass'][1]['bar']=10
data_json = json.dumps(data)
print(data_json)
data = json.loads(data_json)
print(data)
with open("database.json", "w") as json_file:
    json.dump(data, json_file)

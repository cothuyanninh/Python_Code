import json

with open("minh.json") as f:
	data = json.load(f)

for people in data["people"] :
	print(people["name"], people["age"])

with open("new_json.json", "w") as f:
	json.dump(data, f, indent =2)
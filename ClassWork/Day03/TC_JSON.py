import json

data = {
    "Name": "Prashant",
    "Age": "23",
    "Location": "Delhi",
    "Skills": ['Java', 'Python']
}

with open("data.json", 'w') as file:
    json.dump(data, file, indent=10)
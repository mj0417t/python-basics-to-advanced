import json
try:
    with open('07_File_Handling/data.json', 'r') as file:
        data=json.load(file)
    print(json.dumps(data, indent=4))
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")

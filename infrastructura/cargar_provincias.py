import json

def obtener_provincias():
    with open("provincias.json", "r") as file:
        return json.load(file)
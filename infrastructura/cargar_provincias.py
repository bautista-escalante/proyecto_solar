import json

def obtener_provincias():
    with open("infrastructura/provincias.json", "r") as file:
        return json.load(file)
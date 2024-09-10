# encoding=utf8
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6f4d01a955e2b2194eff5381a30275a1'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_add_pokemon = {
    "name": "Покемон",
    "photo_id": 5
}

response_add_pokemon = requests.post(url = URL+'/pokemons', headers = HEADER, json = body_add_pokemon)
print(response_add_pokemon.text.encode('utf-8'))

body_rename_pokemon = {
    "pokemon_id": response_add_pokemon.json()['id'],
    "name": "Бульбазавр",
    "photo_id": 5
}

response_rename_pokemon = requests.put(url = URL+'/pokemons', headers = HEADER, json = body_rename_pokemon)
print(response_rename_pokemon.text.encode('utf-8'))

body_catch_pokemon = {
    "pokemon_id": response_rename_pokemon.json()['id']
}

response_catch_pokemon = requests.post(url = URL+'/trainers/add_pokeball', headers = HEADER, json = body_catch_pokemon)
print(response_catch_pokemon.text.encode('utf-8'))
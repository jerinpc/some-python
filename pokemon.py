import requests
base_url='https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url=f'{base_url}/pokemon/{name}'
    response = requests.get(url)

    if response.status_code==200:
        pokemon_data=response.json()
        return pokemon_data
    else:
        print('something went wrong!')


pokemon_name='Wyrdeer'.lower()

pokemon_info=get_pokemon_info(pokemon_name)
if pokemon_info:
    print(f"Name : {pokemon_info['name'].capitalize()}")
    print(f"Order : {pokemon_info['order']}")
    print(f"Id : {pokemon_info['id']}")
    print(f"Height : {pokemon_info['height']}")
    print(f"Weight : {pokemon_info['weight']}")
    print("___Abilities___")
    for ability in pokemon_info["abilities"]:
        print(ability["ability"]["name"])

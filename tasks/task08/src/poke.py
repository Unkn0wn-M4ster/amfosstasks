import requests
from PIL import Image
from io import BytesIO

def fetch_pokemon_data(pokemon_name):
    base_url = 'https://pokeapi.co/api/v2/'
    pokemon_url = f'{base_url}pokemon/{pokemon_name.lower()}/'

    response = requests.get(pokemon_url)

    if response.status_code == 200:
        pokemon_data = response.json()

        image_url = pokemon_data['sprites']['other']['official-artwork']['front_default']
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image_data = BytesIO(image_response.content)
            image = Image.open(image_data)
            image.show()  

        return pokemon_data
    else:
        print(f"Failed to fetch data for {pokemon_name}.")
        return None

# Example usage
pokemon_name = 'pikachu'
pokemon_data = fetch_pokemon_data(pokemon_name)
if pokemon_data:
    print(f"Name: {pokemon_data['name']}")
    print(f"Abilities: {[ability['ability']['name'] for ability in pokemon_data['abilities']]}")
    print(f"Types: {[type['type']['name'] for type in pokemon_data['types']]}")
    # Add more details as needed

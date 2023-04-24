import requests
data_pok = {
    "name": "лллддп",
    "photo": "https://dolnikov.ru/pokemons/albums/003.png"
}
reponse = requests.post("https://pokemonbattle.me:9104/pokemons", json = data_pok,
                        headers={"User-Agent": "PostmanRuntime/7.32.2", "trainer_token": "44bd26d10103621c9bf469f5bc851232"})
print(reponse.text)
data_pok = {
    "pokemon_id": 9507,
    "name": "маапп",
    "photo": "https://dolnikov.ru/pokemons/albums/003.png"
}

reponse = requests.put("https://pokemonbattle.me:9104/pokemons", json = data_pok,
                        headers={"User-Agent": "PostmanRuntime/7.32.2", "trainer_token": "44bd26d10103621c9bf469f5bc851232"})
print(reponse.text)

data_pok1 = {
    "pokemon_id": 9507
}

reponse = requests.post("https://pokemonbattle.me:9104/trainers/add_pokeball", json = data_pok1,
                        headers={"User-Agent": "PostmanRuntime/7.32.2", "trainer_token": "44bd26d10103621c9bf469f5bc851232"})
print(reponse.text)

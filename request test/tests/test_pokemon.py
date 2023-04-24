import pytest
import requests

def test_status_code():
 url="https://pokemonbattle.me:9104/trainers"
 response=requests.get(url)
 assert response.status_code == 200

def test_check_responce():
 url="https://pokemonbattle.me:9104/trainers?trainer_id=4117"
 response=requests.get(url)
 response=response.json()
 assert response["trainer_name"] == "Лопух"
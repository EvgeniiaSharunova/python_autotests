# encoding=utf8
import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6f4d01a955e2b2194eff5381a30275a1'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '4900'

def test_get_trainers_status_code():
    response = requests.get(url = URL+'/trainers')
    assert response.status_code == 200

def test_get_trainer():
    response_trainer = requests.get(url = URL+'/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_trainer.json()['status'] == 'success'
    assert response_trainer.json()['data'][0]['trainer_name'] == 'Серена'
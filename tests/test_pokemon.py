# encoding=utf8
import requests
import data
import pytest

URL = data.URL
TOKEN = data.TOKEN
HEADER = data.HEADER
TRAINER_ID = data.TRAINER_ID

def test_get_trainers_status_code():
    response = requests.get(url = URL+'/trainers')
    assert response.status_code == 200

def test_get_trainer():
    response_trainer = requests.get(url = URL+'/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_trainer.json()['status'] == 'success'
    assert response_trainer.json()['data'][0]['trainer_name'] == 'Серена'
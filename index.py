import requests
import json

url = 'https://swapi.dev/api/films/1/'
resposta = requests.get(url)
data = resposta.json()

print(data)





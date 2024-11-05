import requests

api_key = '04327c0b-3963-4e92-bcc3-65e3e1551574'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
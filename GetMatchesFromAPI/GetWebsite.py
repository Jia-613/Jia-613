import requests

response = requests.get(url='https://api.football-data.org/v4/matches?dateFrom=2024-06-01&dateTo=2024-06-10', headers={'X-Auh-Token': '946313671e5e48689ace41e1e822c3a3'})

text = response.text

print(text)

#token 946313671e5e48689ace41e1e822c3a3



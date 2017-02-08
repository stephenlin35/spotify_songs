import requests

artist_id = input('Artist id: ')

url = 'https://api.spotify.com/v1/artists/' + artist_id
res = requests.get(url)
res_json = res.json()

print(res_json)

import requests, json
import urllib.parse

api_url = "https://data.geopf.fr/geocodage/search/?q="

adr = "2, boulevard Blaise Pascal, 93160 Noisy le Grand"

r = requests.get(api_url + urllib.parse.quote(adr))

print(r.content.decode('unicode_escape'))

data = json.loads(r.content)

print(data)

coord = data["features"][0]["geometry"]["coordinates"]

print(coord)
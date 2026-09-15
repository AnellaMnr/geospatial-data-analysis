import requests
import json

api_url = "https://data.geopf.fr/geocodage/reverse?"

longitude = 2.583538
latitude = 48.838173

params = {
    "lon": longitude,
    "lat": latitude
}

r = requests.get(api_url, params=params)

data = r.json()

print(data)

adresse = data["features"][0]["properties"]["label"]

print(adresse)
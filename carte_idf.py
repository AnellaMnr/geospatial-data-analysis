import folium

coords = (48.85, 2.35)

map = folium.Map(
    location=coords,
    tiles="OpenStreetMap",
    zoom_start=9
)

folium.GeoJson(
    "idf.geojson"
).add_to(map)

map.save(outfile="carte_idf.html")
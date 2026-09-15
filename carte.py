import folium

coords = (48.8398094, 2.5840685)

map = folium.Map(
    location=coords,
    tiles="OpenStreetMap",
    zoom_start=15
)

coords = [48.8490591, 2.577023]
folium.Marker(location=coords, popup="ESIEE Paris").add_to(map)

map.save(outfile="map.html")
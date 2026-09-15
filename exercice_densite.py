import pandas as pd
import folium

data_surface = pd.read_csv(
    "correspondance-code-insee-code-postal.csv",
    sep=";"
)

data_surface["Densite"] = (
    data_surface["Population"] * 100000
    / data_surface["Superficie"]
)

DEPS = ["75", "77", "78", "91", "92", "93", "94", "95"]

data_surface = data_surface[
    data_surface["Code Département"].astype(str).isin(DEPS)
]

coords = (48.7190835, 2.4609723)

map = folium.Map(
    location=coords,
    tiles="OpenStreetMap",
    zoom_start=9
)

folium.Choropleth(
    geo_data="idf.geojson",
    data=data_surface,
    columns=["Code INSEE", "Densite"],
    key_on="feature.properties.code_commune",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Densité de population (habitants/km²)"
).add_to(map)

map.save(outfile="densite.html")
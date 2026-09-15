import geojson
import geopandas
import pandas

france = geopandas.read_file("datagouv-communes.geojson")



DEPS = ["75", "77", "78", "91", "92", "93", "94", "95"]

idf = []

for dep in DEPS:
    idf.append(france[france["code_departement"] == dep])

idf = pandas.concat(idf)



arrondissements = geopandas.read_file("arrondissements.geojson")
arrondissements["code_commune"] = arrondissements["c_arinsee"]
idf = idf[idf["code_commune"] != "75056"]
idf = pandas.concat([idf, arrondissements], ignore_index=True)

idf.to_file("idf.geojson", driver="GeoJSON")



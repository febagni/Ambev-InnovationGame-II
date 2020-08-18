import pandas as pd
import folium
import json
import os
import subprocess
import numpy as np
import geojson


arquivo = pd.read_csv("data.csv")
count = arquivo.groupby('location')['location'].transform('count')
df = arquivo['location'].value_counts()
df = pd.DataFrame(df)
df.index.name = 'estado'
df.reset_index(inplace=True)
df['estado'] = df['estado'].astype(str)
df['location'] = df['location'].astype(np.float16)

mapa = folium.Map(width='100%', height='100%', location=[-15.77972, -47.92972], zoom_start=4)
geo_json_data=json.load(open("br_states.json"))

folium.Choropleth(geo_data=geo_json_data, name="nome do mapa", data=df, columns=["estado", "location"],
                  key_on='feature.id', fill_color="Reds", fill_opacity=0.8, line_opacity=0.8,
                  line_color= 'white', show=True,legend_name="Exemplo de distribuição por estados").add_to(mapa)
mapa.save("mapa.html")
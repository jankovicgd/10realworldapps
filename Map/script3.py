import folium
import pandas

def colorfelev(elev):
    if elev < 1000:
        col = 'green'
    elif 1000 <= elev < 3000:
        col = 'orange'
    else:
        col = 'red'
    return col

df = pandas.read_csv("Volcanoes-USA.txt")

avglat = df['LAT'].mean()
avglon = df['LON'].mean()

map = folium.Map(location = [avglat, avglon], zoom_start = 5
, tiles = 'Mapbox Bright')
fg = folium.FeatureGroup(name = "Volcano Locations")

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    marker = folium.Marker([lat, lon],
                           popup = folium.Popup(name),
                           icon = folium.Icon(color = colorfelev(elev)))
    fg.add_child(marker)


map.add_child(fg)
map.add_child(folium.GeoJson(data = open('Dataset.geojson'),
                             name = 'World Population',
                             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save('map2.html')

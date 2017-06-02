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
, tiles = 'Stamen Terrain')

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    marker = folium.Marker([lat, lon],
                           popup = folium.Popup(name))

    icon = folium.Icon(color = colorfelev(elev))

    icon.add_to(marker)
    marker.add_to(map)
map.save('volcanoesmap.html')

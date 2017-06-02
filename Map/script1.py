import folium

map = folium.Map(location = [45.372, -121.697], zoom_start = 12, tiles = 'Stamen Terrain')

marker1 = folium.Marker([45.372, -121.6972],
                        popup = folium.Popup('Mt. Hood Meadows'))

marker2 = folium.Marker([45.3311, -121.7311],
                        popup = folium.Popup('Timberlake Lodge'))

marker1.add_to(map)
marker2.add_to(map)

map.save('test.html')

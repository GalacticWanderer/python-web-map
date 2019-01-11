import folium  # used for building web maps
import pandas

data = pandas.read_csv("cdnates.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])


def chooseColor(elev):
    if elev in range(0, 1000):
        return "green"
    elif elev in range(1001, 2000):
        return "purple"
    elif elev in range(2001, 3000):
        return "orange"
    elif elev in range(3001, 4000):
        return "blue"
    elif elev in range(4001, 5000):
        return "red"


# init a map variable with folium.Map and pass in loc, zoom and tile
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
# fg is feature group which is used to add elemsnts such as markers to the map

fg = folium.FeatureGroup(name="My Map")

# a simple for loop to add three markers to the FeatureGroup var fg
for lt, ln, nm, el in zip(lat, lon, name, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup="%s" % nm,
                               icon=folium.Icon(color=chooseColor(el))))
#  adding fg to map and then saving map as html file
map.add_child(fg)
map.save("map1.html")

import folium  # used for building web maps
import pandas

# loading the txt file and converting to dataframe, and oython lists
data = pandas.read_csv("cdnates.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])


# helper func to return a certain color based on the range of elecvation
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

# a loop to zip our lists of lat, lon, name and elevation and add to fg
for lt, ln, nm, el in zip(lat, lon, name, elev):
    # adding a circle marker on each loop to fg
    fg.add_child(folium.CircleMarker(location=[lt, ln],
                                     radius=6, popup="%s" % nm,
                                     fill_color=chooseColor(el), color="gray"))
#  adding fg to map and then saving map as html file
map.add_child(fg)
map.save("map1.html")

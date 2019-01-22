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

# fgv is feature group which is used to add elemsnts such as markers to the map
# in this instance fgv stands is specifically for Volcanoes
fgv = folium.FeatureGroup(name="Volcanoes")

# a loop to zip our lists of lat, lon, name and elevation and add to fg
for lt, ln, nm, el in zip(lat, lon, name, elev):
    # adding a circle marker on each loop to fgv
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                      radius=6, popup="%s" % nm,
                                      fill_color=chooseColor(el), color="gray"))

# fgp is a feature group specifically for population and polugonal colors
fgp = folium.FeatureGroup(name="Population")
# added a new child to the feature group, it displays polygonal shapes based
# on external input from world.json
# using a lambda func and if/else statement, chnage the colors of polygons
fgp.add_child(folium.GeoJson(data=open(
    'world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green'
                              # if less than 10 mil
                              if x['properties']['POP2005'] < 10000000
                              # if less than or equal to 10 mil and less than 20 mil
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                              # otherwise just red
                              else 'red'}))
# the values POP2005 is stored on the world.json file as a child of 'properties'
# hence x['properties']['POP2005']

#  adding fgv and fgp to map and then saving map as html file
map.add_child(fgv)
map.add_child(fgp)
# using folium.LayerControl(), the user can toggle between different fgv and fgp
map.add_child(folium.LayerControl())
map.save("map1.html")

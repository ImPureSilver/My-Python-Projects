"""
Made by: Andy Hernandez

This is a web map that I have made under the online intructor Ardit on Udemy on his Mega Python Course
"""
import folium
import pandas

#the file that contains all of the information needed to make the map.
data = pandas.read_csv("Volcanoes.txt")
#Segment the data in the appropiate variables for sorting out the data in the text file.
lat = list(data["LAT"])#Grabbing the lattitudes from the text file and storing them as a list.
lon = list(data["LON"])#Grabbing the longitudes from the text file and storing them as a list.
ele = list(data["ELEV"])#Grabbing the elevations from the text file and storing them as a list.
name = list(data["NAME"])#Grabbing the names from the text file and sotring them as a list.

#This funstions serves to make colored points based on the elevation of the volcanoes.
def color_producer(elevation):
    if elevation < 1000:#If the elevation is less than the value 1000, that the color will be green.
        return 'green'
    elif 1000 <= elevation < 3000:# If the elevation is less than or equal to the value 1000 but its also less than 3000, then assign the color orange.
        return 'orange'
    else:# If the elevation value exceeds 3000, the the color assigned will be red.
        return 'red'
#Making a location in which when the map is loaded, the starting point wil be at the given coordinate and the zoom will be how far away from the map you will be.
map = folium.Map(location=[38.58, -99.89], zoom_start=6, tiles="Mapbox Bright")
fgv = folium.FeatureGroup(name="Volcanoes")


# the zip function distrubuted data one by one to have it match its intended pair pair in a seperate list.
for lt, ln, el, nam in zip(lat, lon, ele, name):#This is to make the data of the coordinates of the data above to line up to one another they way they should in order to have properly placed  points
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6 , popup = str(el) + "m, " + nam, fill_color=color_producer(el), color = 'grey', fill_opacity = 0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))#Adding in the json file to make some polygonial shapes to the map.



#Keeping the child objects in place

map.add_child(fgv)#adding in the child objects to the map
map.add_child(fgp)# feature group for the layering of the map
map.add_child(folium.LayerControl())# What will be in control of adding and removing the layres from the map.

map.save("Map1.html")# This is to save the program and have the Map1.html file be udapted if anything from above changes.






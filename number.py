
import phonenumbers
import opencage
import geocoder
import webbrowser
import folium

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
key = "3379652dc73446eda09df1dcc1ddc287"
numb = input("Enter Number :_")

from phonenumbers import geocoder

sannumber = phonenumbers.parse(numb)

#for country
Location = geocoder.description_for_number(sannumber, 'en')
print("Country:_")
print(Location)

# for service provider
from phonenumbers import carrier

serprov = phonenumbers.parse(numb)
#print("Service Provided by:_")
#print(carrier.name_for_number(serprov, 'en'))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(Location)

results = geocoder.geocode(query)
#print(results)

lat =results[0]['geometry']['lat']
lng =results[0]['geometry']['lng']

print(lat,lng)


#google = str('https://www.google.com/maps/@') 
#gog1 = google + str(lat) +","+ str(lng)
#webbrowser.get('firefox').open(gog1, new=1)

mymap = folium.Map(Location=[lat,lng], zoom_start=9)
folium.Marker([lat, lng],popup=Location).add_to((mymap))
mymap.save("mylocation.html")
import phonenumbers
import folium
import opencage
from phonenumbers import geocoder
#from test import number

number = input("Enter phone number with country code: ")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")

print(number_location)

# Now we have got the phone Number's country , now we want the carrier or The SERVICE provider 
# -> like jio , airtel etc...
# we want carrier class 
from phonenumbers import carrier 

service_provider =  phonenumbers.parse(number)
service_provider_name = carrier.name_for_number(service_provider,"en")
print(service_provider_name)


# Now we will show the location on map , for that we have to know the latitude and longitude 

# Finding the Latitude and longitude

from opencage.geocoder import OpenCageGeocode

# we need the api key of opencage

geocoder = OpenCageGeocode("0a2bf478fb2b4f3fa7397f9aa1eb5e33")

# Now we want the number location in a string 

query = str(number_location)
results = geocoder.geocode(query)

# Now for map we will be needing the latitude and longitude 

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)
# Now we want to get a pointer on the map
# and for that we will use folium module


map_location = folium.Map(location = [lat,lng],zoom_start = 9)

folium.Marker([lat,lng],popup = number_location).add_to(map_location)

map_location.save("mylocation.html")





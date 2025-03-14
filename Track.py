import phonenumbers
import folium
# import opencage
from phonenumbers import geocoder
from yarl import Query
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

import requests 

# we need the api key of opencage

google_api_key = "" 
geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={Query}&key={google_api_key}"
# Now we want the number location in a string 

query = str(number_location)
# results = geocoder.geocode(query)
response = requests.get(geocode_url).json()
# Now for map we will be needing the latitude and longitude 
if response['status'] == "OK":

  lat = response['results'][0]['geometry']['location']['lat']
  lng = response['results'][0]['geometry']['location']['lng']
  print(f"Latitude: {lat}, Longitude: {lng}")
else:
    print("Error fetching location data from Google API")
# Now we want to get a pointer on the map
# and for that we will use folium module

# Now fetching nearby mobile towers using google places API

places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=5000&type=point_of_interest&keyword=mobile%20tower&key={google_api_key}"
places_response = requests.get(places_url).json()

if places_response['status'] == "OK":
    towers = places_response['results']
else:
    towers = []


# Now modifying maps to display towers ->


# map_location = folium.Map(location = [lat,lng],zoom_start = 9)
# Now replacing the above line due to using the google's api

map_location = folium.Map(location=[lat, lng], zoom_start=12)

# Plot main location (User’s number location)
folium.Marker(
    [lat, lng], popup=number_location, icon=folium.Icon(color="blue")
).add_to(map_location)

# Plot towers found by Google Places API
for tower in towers:
    tower_lat = tower["geometry"]["location"]["lat"]
    tower_lng = tower["geometry"]["location"]["lng"]
    tower_name = tower["name"]
    
    folium.Marker(
        [tower_lat, tower_lng],
        popup=f"{tower_name}\nLat: {tower_lat}, Lon: {tower_lng}",
        icon=folium.Icon(color="red")
    ).add_to(map_location)

print(f"Added {len(towers)} mobile towers to map.")







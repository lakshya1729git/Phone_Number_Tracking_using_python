# Phone_Number_Tracking_using_python
A Python-based tool that identifies the geographical location (state/city), service provider (Jio, Airtel, etc.), and nearby mobile towers of a phone number. The project uses phonenumbers, Google Geocoding API, and Folium to fetch details and visualize the location on an interactive map.


-> Features
Identify the country, state, and city of a phone number.
Detect the service provider (e.g., Jio, Airtel, Vodafone).
Fetch latitude and longitude coordinates of the location.
Display the location on an interactive Folium map.
Find and mark nearby mobile towers using the Google Places API.

-> Technologies Used
Python
phonenumbers (for number parsing & location)
Folium (for interactive map visualization)
Google Geocoding API (for latitude/longitude)
Google Places API (for finding mobile towers)
Requests (for API integration)

>How It Works
1️) Enter a phone number (with country code).
2️) The script extracts the location & carrier details.
3️) It fetches latitude & longitude from the Google Geocoding API.
4️) An interactive Folium map is generated.
5️) Nearby mobile towers (within 5 km) are fetched and marked on the map.

There are two files ->
1.) Track.py -
It consists of code which uses Google's Geocoding API for better and more precise location , it gives the name of the state and the city , and folium shows it on map that from where the number is originated  

2.) try.py - 
this was initial code with Opencage's geocoding API , which only gave the latitude and longitude of the centre of the country. For example my number is of Maharshtra , Mumbai , but still the coordinates will be of Madhyapradesh , since it is the centre of india . So it is not precise . I prefer to use your Google geocoding API.
In these documents I have removed my API key , you can use your generated one. 


Some demo insights ![image](https://github.com/user-attachments/assets/38fb6542-893e-4a75-a27a-992efd27d419)
![image](https://github.com/user-attachments/assets/5be8624f-4910-4393-9e5f-a3e7152a73ab


import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='googlemapskey')

# Geocoding an address
geocode_result = gmaps.geolocate()

lat = geocode_result['location']['lat']
lng = geocode_result['location']['lng']

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.timezone((lat, lng))

timezoneID = reverse_geocode_result['timeZoneId']

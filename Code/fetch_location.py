from requests import post, get
import json
from pprint import pprint

import googlemaps
import datetime
from dateutil import tz

gmaps = googlemaps.Client(key='googlemapskey')

# Geocoding an address
geocode_result = gmaps.geolocate()

lat = geocode_result['location']['lat']
lng = geocode_result['location']['lng']

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.timezone((lat, lng))

timezoneID = reverse_geocode_result['timeZoneId']

url = "https://api.sunrise-sunset.org/json?lat="+str(lat)+"&lng="+str(lng)+"&formatted=0"

sunrise_set = get(url).json()['results']

sunriseT = sunrise_set['sunrise']
sunsetT = sunrise_set['sunset']

d=datetime.datetime.strptime(sunriseT, "%Y-%m-%dT%H:%M:%S+00:00") #Get your naive datetime object
d=d.replace(tzinfo=datetime.timezone.utc) #Convert it to an aware datetime object in UTC time.
d=d.astimezone() #Convert it to your local timezone (still aware)

sunriseT = d

d=datetime.datetime.strptime(sunsetT, "%Y-%m-%dT%H:%M:%S+00:00") #Get your naive datetime object
d=d.replace(tzinfo=datetime.timezone.utc) #Convert it to an aware datetime object in UTC time.
d=d.astimezone() #Convert it to your local timezone (still aware)

sunsetT = d

print("Sunrise : "+sunriseT.strftime("%I:%M:%S %p %Z")) #Print it with a directive of choice
print("Sunset  : "+sunsetT.strftime("%I:%M:%S %p %Z")) #Print it with a directive of choice

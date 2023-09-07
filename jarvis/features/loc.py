import webbrowser, requests
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder
from jarvis.features.speech import speak
from jarvis.features.listen import takecommand
def loc(place):
    webbrowser.open("http://www.google.com/maps/place/" + place + "")
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place, addressdetails=True)
    target_latlng = location.latitude, location.longitude
    location = location.raw['address']
    target_loc = {'city': location.get('city', ''),
                   'state': location.get('state', ''),
                   'country': location.get('country', '')}

    current_loc = geocoder.ip('me')
    current_latlng = current_loc.latlng

    distance = str(great_circle(current_latlng, target_latlng))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance), 1)

    return current_loc, target_loc, distance

def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']
    try:
        
        print(city, state, country)
        speak(f"You are currently in {city} city which is in {state} state and country {country}")
    except Exception as e:
        speak("Sorry sir, I coundn't fetch your current location. Please try again")
    speak('Sir, do you want to see your location on map ?')
    res = takecommand().lower()
    if 'yes' in res or 'show me' in res:
        webbrowser.open("http://www.google.com/maps/place/" + city + "")
        speak('sir, your location is displayed to map.')
    else:
        return city, state, country
    
    return city, state,country




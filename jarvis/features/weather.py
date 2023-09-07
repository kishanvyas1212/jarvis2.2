import requests
from jarvis.features.listen import takecommand
from jarvis.features.speech import speak
import json
from jarvis.config.configuration import weather_api as api_key

def get_weather(command):
    
    if 'my location' in command:
        city = 'rajkot'
        
    else:     
        speak('Which city weather would you like to know sir? ')
        city = takecommand().lower()
    
    
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    if city is None:
        speak('Which city weather would you like to know sir? ')
        city = takecommand().lower()
    else:
        print(city)
        
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)
    # print(weather_data)
    speak(f"Sir, temparature of city {city} is {weather_data['main']['temp']} celsius")
    speak(f" the pressure in {city} is {weather_data['main']['pressure']} pascal")
    speak(f" the humidity in {city} is {weather_data['main']['humidity']} percentage")
    speak('sir do you want to see it ?')
    query = takecommand().lower()
    if 'yes' in query:
        speak('sir please check the terminal the result is printed')
        print(weather_data)

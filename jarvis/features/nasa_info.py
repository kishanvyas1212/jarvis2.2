import requests
from jarvis.config.configuration import nasa_api as api_key
# api_key = ''
# Replace 'YOUR_API_KEY' with your actual NASA API key
base_url = 'https://api.nasa.gov/planetary/apod'

# Request parameters
params = {
    'api_key': api_key,
    'count': 5  # Number of images to retrieve (you can adjust this as needed)
}

# Make the API request
response = requests.get(base_url, params=params)

if response.status_code == 200:
    # API call successful
    data = response.json()
    for entry in data:
        date = entry['date']
        title = entry['title']
        explanation = entry['explanation']
        url = entry['url']
        print(f"Date: {date}")
        print(f"Title: {title}")
        print(f"Explanation: {explanation}")
        print(f"URL: {url}")
        print("-----------------------")
else:
    # API call failed
    print(f"Failed to retrieve data. Status code: {response.status_code}")

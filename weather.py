
import argparse

# API URL and key
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = 'your_api_key_here'

# Create a command-line argument parser
parser = argparse.ArgumentParser(description='Get current weather conditions of a city.')
parser.add_argument('city', metavar='C', type=str, help='Name of the city')
args = parser.parse_args()

# Send a GET request to the API with the city name and API key
response = requests.get(API_URL, params={'q': args.city, 'appid': API_KEY})

# If the response is successful (status code 200), print the weather conditions
if response.status_code == 200:
    data = response.json()
    print(f"Current weather in {args.city}:")
    print(f"Description: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']} K")
    print(f"Humidity: {data['main']['humidity']}%")
else:
    print(f"Error getting weather data: {response.status_code}")

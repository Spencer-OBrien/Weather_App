import requests
import json

API_KEY = r"21354f52bec7021538a451e50d85f404"
KELVIN = 273.15

def city_weather(city_name):
    city_name = city_name.capitalize()
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

    response = requests.get(url)
    data = json.loads(response.text)
    temp = int(data["main"]["temp"] - KELVIN)

    return f"{city_name} {temp}°"

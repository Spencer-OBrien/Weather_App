import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")
KELVIN = 273.15


def city_weather(city_name):
    city_name = city_name.capitalize()

    url = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}")

    response = requests.get(url)
    data = json.loads(response.text)

    temp = int(data["main"]["temp"] - KELVIN)
    sunrise = datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"]).strftime("%H:%M")
    sunset = datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"]).strftime("%H:%M")
    current_time = datetime.utcfromtimestamp(data["dt"] + data["timezone"]).strftime("%H:%M")
    description = data["weather"][0]["description"]
    country = data["sys"]["country"]

    weather_data = {
        "city": city_name,
        "temp": temp,
        "sunrise": sunrise,
        "sunset": sunset,
        "current_time": current_time,
        "description": description.capitalize(),
        "country": country,
    }

    return weather_data

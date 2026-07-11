# weather_api.py

import requests
from config import API_KEY, CITY


def get_weather():

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    temperature = data["main"]["temp"]

    return temperature

if __name__ == "__main__":
    print(get_weather())
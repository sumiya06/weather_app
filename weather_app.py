import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
    else:
        print("City not found. Please check the name.")
except requests.exceptions.RequestException as e:
    print("Error while connecting to the weather service:", e)

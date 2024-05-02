from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")
KEY = os.getenv("APIKEY")

def get_data(place, days, option):
    url = f"api.openweathermap.org/data/2.5/forecast?q={place}&appid={KEY}"
    response = requests.get(url)
    data = response.json()
    return data
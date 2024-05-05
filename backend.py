from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")
KEY = os.getenv("API_KEY")

def get_data(place, days=None, option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))

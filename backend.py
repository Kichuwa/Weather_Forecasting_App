from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")
KEY = os.getenv("API_KEY")


def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    date_value = 8 * days
    filtered_data = filtered_data[:date_value]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3))

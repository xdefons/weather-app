import requests
from datetime import datetime
from utils.kelvcelc_conv import kelvcelcconv
from utils.speed_conv import ms_to_kmh


def fetch_weather(token: str,city: str):

    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}"

    try:
        response = requests.get(url)
        data = response.json()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        weather = {
            "timestamp":timestamp,
            "name": data["name"],
            "temp": kelvcelcconv(data["main"]["temp"]),
            "feels_like": kelvcelcconv(data["main"]["feels_like"]),
            "humidity": data["main"]["humidity"],
            "wind_speed": ms_to_kmh(data["wind"]["speed"])
        }

        return weather


    except Exception as e:
        print(e)

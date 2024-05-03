import os
import requests



WEATHER_APP_API_KEY = "WEATHER_APP_API_KEY"
WEATHER_APP_API_KEY = os.getenv(WEATHER_APP_API_KEY)

def get_data(place, forecast_Days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={WEATHER_APP_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    print(get_data(place="Tokyo"))



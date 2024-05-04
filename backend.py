import os
import requests



WEATHER_APP_API_KEY = "WEATHER_APP_API_KEY"
WEATHER_APP_API_KEY = os.getenv(WEATHER_APP_API_KEY)

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={WEATHER_APP_API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    forecast_days = forecast_days
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]        
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=5))



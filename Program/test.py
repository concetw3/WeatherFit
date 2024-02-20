import requests
import json
from random import choice
from datetime import datetime

def load_data(file_path, key):
    with open(file_path) as f:
        data = json.load(f)
        return data.get(key)

def get_weather_forecast(latitude, longitude):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    response = requests.get(f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={latitude}&lon={longitude}", headers=headers)
    return json.loads(response.text)['properties']['timeseries']

def get_next_hour_precipitation(timeseries):
    next_hour_data = timeseries[0]['data']['next_1_hours']
    return next_hour_data['details']['precipitation_amount'] if next_hour_data else 0



def get_current_temperature(timeseries):
    return timeseries[0]['data']['instant']['details']['air_temperature']

def get_outfit_data(category):
    return choice(load_data(f'Json/{category}.json', category))

def choose_outfit(timeseries):
    return [get_outfit_data(category) for category in ['bukser']]

def main():
    latitude = 55.67
    longitude = 12.56
    timeseries = get_weather_forecast(latitude, longitude)
    current_temperature = get_current_temperature(timeseries)
    next_hour_precipitation = get_next_hour_precipitation(timeseries)

    print(f"The date and time is {datetime.now().replace(microsecond=0)}")
    print(f"The temperature is {current_temperature} degrees Celsius outside right now")

    if next_hour_precipitation >= 1:
        print("It's going to rain within the next hour.")
    else:
        print("It's not going to rain within the next hour.")

    outfit = choose_outfit(timeseries)
    print(json.dumps(outfit, indent=4))

if __name__ == "__main__":
    main()

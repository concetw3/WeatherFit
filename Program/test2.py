import requests
import json
import random
from datetime import datetime

  
def get_weather_forecast(latitude, longitude):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    response = requests.get(f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={latitude}&lon={longitude}", headers=headers)
    return json.loads(response.text)['properties']['timeseries']

def get_next_hour_precipitation(timeseries):
    next_hour_data = timeseries[0]['data']['next_1_hours']
    return next_hour_data['details']['precipitation_amount'] if next_hour_data else 0



def get_current_temperature(timeseries):
    return timeseries[0]['data']['instant']['details']['air_temperature']

def findkeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
               yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                yield x
                


def jakker():
    latitude = 55.67
    longitude = 12.56
    timeseries = get_weather_forecast(latitude, longitude)
    next_hour_precipitation = get_next_hour_precipitation(timeseries)
    temperatur = get_current_temperature(timeseries)
    with open('Json\\jakker.json') as f:
        jakker_data = json.load(f)
        
        vinterjakke = 8  

        find_varme_keys = list(findkeys(jakker_data, 'varme'))
        #print(find_varme_keys)
        sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if num >= vinterjakke]
       #print(sorter_varme_keys)
        tilfaeldige_keys = random.choice(sorter_varme_keys) 
       #print(tilfaeldige_keys)
        jakke_data_varme = jakker_data['jakker'][tilfaeldige_keys]
        #print(jakke_data_varme)
    


jakker()
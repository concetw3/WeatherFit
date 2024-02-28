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


def bukser():
    with open('Json\\bukser.json') as f:
        bukser_data = json.load(f)
        bukser_data = random.choice(bukser_data['bukser'])
        return bukser_data
    
def hovedbeklaedning():
     with open('Json\\hovedbeklaedning.json') as f:
        hovedbeklaedning_data = json.load(f)
        hovedbeklaedning_data = random.choice(hovedbeklaedning_data['kasketter'])
        return hovedbeklaedning_data

    
def sko():
    latitude = 55.67
    longitude = 12.56
    timeseries = get_weather_forecast(latitude, longitude)
    next_hour_precipitation = get_next_hour_precipitation(timeseries)
    current_temperature = get_current_temperature(timeseries)
    with open('Json\\sko.json') as f:
        sko_data = json.load(f)
        sko_data = sko_data['sko']
    if next_hour_precipitation >= 1:
        find_vandtaette_keys = list(findkeys(sko_data, 'vandtaette'))
        sorter_vandtaette_keys = [i for i, x in enumerate(find_vandtaette_keys) if x]
        tilfaeldige_keys = random.choice(sorter_vandtaette_keys)   
        sko_data_vandtaette = sko_data[tilfaeldige_keys]
        return sko_data_vandtaette
    else:
        sko_data = random.choice(sko_data)
    return sko_data
        
 

def jakker():
    latitude = 55.67
    longitude = 12.56
    timeseries = get_weather_forecast(latitude, longitude)
    next_hour_precipitation = get_next_hour_precipitation(timeseries)
    temperatur = get_current_temperature(timeseries)
    with open('Json\\jakker.json') as f:
        jakker_data = json.load(f)
        find_varme_keys = list(findkeys(jakker_data, 'varme'))
    if next_hour_precipitation >= 1:
        find_vandtaette_keys = list(findkeys(jakker_data, 'vandtaette'))
        sorter_vandtaette_keys = [i for i, x in enumerate(find_vandtaette_keys) if x]
        tilfaeldige_keys = random.choice(sorter_vandtaette_keys)   
        jakke_data = jakker_data[tilfaeldige_keys]
        jakke_data
    else:
        if temperatur < -5:
            vinterjakke_min_varme = 8  
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if num >= vinterjakke_min_varme]
            tilfaeldige_keys = random.choice(sorter_varme_keys) 
            jakke_data_varme = jakker_data['jakker'][tilfaeldige_keys]
            return jakke_data_varme
        elif 0 <= temperatur <= 10:
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if 4 <= num <= 7]
            tilfaeldige_keys = random.choice(sorter_varme_keys) 
            jakke_data_varme = jakker_data['jakker'][tilfaeldige_keys]
            return jakke_data_varme
        else:
            if 10 <= temperatur <= 40:
                sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if  0 <= num <= 4]
                tilfaeldige_keys = random.choice(sorter_varme_keys) 
                jakke_data_varme = jakker_data['jakker'][tilfaeldige_keys]
                return jakke_data_varme

    

def troejer():
     with open('Json\\troejer.json') as f:
        troejer_data = json.load(f)
        latitude = 55.67
        longitude = 12.56
        timeseries = get_weather_forecast(latitude, longitude)
        current_temperature = get_current_temperature(timeseries)
        
        if current_temperature >= 3:
            troejer_data_rnd = random.choice(troejer_data['troejer'])
            return troejer_data_rnd
        else:
            if current_temperature <= 2:
                troejer_data_sweater = random.choice(troejer_data['sweater'])
                return troejer_data_sweater,troejer_data_rnd


def tshirt():
    with open('Json\\t-shirts.json') as f:
        t_shirt_data = json.load(f)
        t_shirt_data2 = random.choice(t_shirt_data['t-shirts'])
        skjorte_data = random.choice(t_shirt_data['skjorter'])
        return t_shirt_data2, skjorte_data


def load_data(file_path, key):
    with open(file_path) as f:
        data = json.load(f)
        return data.get(key)



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

def kl12(timeseries):
    iso_date_kl12 = datetime.now().replace(hour=23,minute=0,second=0,microsecond=0,).isoformat()
    iso_date_kl12z ='Z'
    iso_date_kl12_kombineret = ''.join([iso_date_kl12,iso_date_kl12z])

    time = list(findkeys(timeseries, 'time'))
    Klokken18 = time.index(iso_date_kl12_kombineret)
    Access_timeseries = timeseries
    data_klokken_12 = Access_timeseries[Klokken18]['data']['instant']['details']['air_temperature']
    return data_klokken_12


def zeroto10degrees(timeseries):
    outfit = []   
    kategorier = [hovedbeklaedning, tshirt, troejer, jakker, bukser, sko]
    for i in kategorier:
        outfit.append(i())
    print(json.dumps(outfit, indent=4))
        
            
            
 

    
    


def main():
    latitude = 55.67
    longitude = 12.56
    timeseries = get_weather_forecast(latitude, longitude)
    current_temperature = get_current_temperature(timeseries)
    next_hour_precipitation = get_next_hour_precipitation(timeseries)

    data_klokken_12 = kl12(timeseries)
    outfit10 = zeroto10degrees(timeseries)
    print(f"temperatur er lige nu {data_klokken_12}")
    
    
    ##print(f"The date and time is {datetime.now().replace(microsecond=0)}")
    #print(f"The temperature is {current_temperature} degrees Celsius outside right now")
    #print(f"The temperature at 12 will be {data_klokken_12} degrees Celsius outside ")
    


if __name__ == "__main__":
    main()

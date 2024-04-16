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

def get_next_hour_symbol_code(timeseries):
    next_hour_data = timeseries[0]['data']['next_1_hours']
    return next_hour_data['summary']['symbol_code']
    

latitude = 55.67
longitude = 12.56
timeseries = get_weather_forecast(latitude, longitude)
current_temperature = get_current_temperature(timeseries)
timeseries = get_weather_forecast(latitude, longitude)
next_hour_precipitation = get_next_hour_precipitation(timeseries)

def baelter():
   with open('Json\\accessories.json') as f:
        accessories_data = json.load(f)
        return random.choice(accessories_data['baelter'])


def handsker():
   with open('Json\\accessories.json') as f:
        accessories_data = json.load(f)
        find_varme_keys = list(findkeys(accessories_data, 'varme'))
        if -10 <= current_temperature <= 4:
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if num >= 8]
            tilfaeldige_keys = random.choice(sorter_varme_keys) 
            return accessories_data['handsker'][tilfaeldige_keys]
        elif 5 <= current_temperature <= 10:
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if 3 <= num <= 6]
            tilfaeldige_keys = random.choice(sorter_varme_keys)
            return accessories_data['handsker'][tilfaeldige_keys]
        else:
            return None

def slips():
   with open('Json\\accessories.json') as f:
        accessories_data = json.load(f)
        return random.choice(accessories_data['slips'])
                    

def accessories():
    with open('Json\\accessories.json') as f:
        accessories_data = json.load(f)
    symbol_code = get_next_hour_symbol_code(timeseries) 
    if symbol_code == 'clearsky_day':
        return accessories_data['solbriller']

def bukser():
    with open('Json\\bukser.json') as f:
        bukser_data = json.load(f)
        find_varme_keys = list(findkeys(bukser_data, 'varme'))
        if -10 <= current_temperature -1:
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if num >= 6]
            tilfaeldige_keys = random.choice(sorter_varme_keys) 
            bukser_info = bukser_data['bukser'][tilfaeldige_keys]
            if bukser_info.get('baelte', False):  
                 return bukser_info, baelter()
            else:
                 return bukser_info, None
        elif 0 <= current_temperature <= 10:
             sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if 3 <= num <= 6]
             tilfaeldige_keys = random.choice(sorter_varme_keys)
             bukser_info = bukser_data['bukser'][tilfaeldige_keys]
             if bukser_info.get('baelte', False):  
                 return bukser_info, baelter()
             else:
                 return bukser_info, None
        elif 18 <= current_temperature <= 40:
            return random.choice(bukser_data['shorts'])

def overtraeksbukser():
    with open('Json\\bukser.json') as f:
        bukser_data = json.load(f)
        find_vandtaette_keys = list(findkeys(bukser_data['overtraeksbukser'], 'vandtaette'))
        if next_hour_precipitation >= 1:                         
              sorter_vandtaette_keys = [i for i, x in enumerate(find_vandtaette_keys) if x]
              tilfaeldige_keys = random.choice(sorter_vandtaette_keys)   
              return bukser_data['overtraeksbukser'][tilfaeldige_keys]

def hovedbeklaedning(): 
     with open('Json\\hovedbeklaedning.json') as f:
        hovedbeklaedning_data = json.load(f)
        find_varme_keys = list(findkeys(hovedbeklaedning_data['huer'], 'varme'))
        if current_temperature -20 <= current_temperature <= 2:
            min_varme = 6  
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if num >= min_varme]
            tilfaeldige_keys = random.choice(sorter_varme_keys) 
            hovedbeklaedning_data_varme = hovedbeklaedning_data['huer'][tilfaeldige_keys]
            return hovedbeklaedning_data_varme
        else:
            hovedbeklaedning_data = random.choice(hovedbeklaedning_data['kasketter'])
            return hovedbeklaedning_data
   
def sko():
    with open('Json\\sko.json') as f:
        sko_data = json.load(f)
        find_varme_keys = list(findkeys(sko_data, 'varme'))
    if next_hour_precipitation >= 1:
        find_vandtaette_keys = list(findkeys(sko_data, 'vandtaette'))
        sorter_vandtaette_keys = [i for i, x in enumerate(find_vandtaette_keys) if x]
        tilfaeldige_keys = random.choice(sorter_vandtaette_keys)   
        sko_data_vandtaette = sko_data[tilfaeldige_keys]
        return sko_data_vandtaette
    else:
        if current_temperature -20 <= current_temperature <= 2:
            min_varme = 8  
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if num >= min_varme]
            tilfaeldige_keys = random.choice(sorter_varme_keys) 
            sko_data_varme = sko_data['sko'][tilfaeldige_keys]
            return sko_data_varme
        elif 2 <= current_temperature <= 15:
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if 4 <= num <= 7]
            tilfaeldige_keys = random.choice(sorter_varme_keys) 
            sko_data_varme = sko_data['sko'][tilfaeldige_keys]
            return sko_data_varme
        elif 15 <= current_temperature <= 40:
                sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if  0 <= num <= 2]
                tilfaeldige_keys = random.choice(sorter_varme_keys) 
                sko_data_varme = sko_data['sko'][tilfaeldige_keys]
                return sko_data_varme

def troejer():
     with open('Json\\troejer.json') as f:
        troejer_data = json.load(f)
        if 3 <= current_temperature  <= 15:
            troejer_data_rnd = random.choice(troejer_data['troejer'])
            return troejer_data_rnd
        elif -20 <= current_temperature <= 2:    
             troejer_data_sweater = random.choice(troejer_data['sweater'])
             return troejer_data_sweater
        elif current_temperature > 18:
            return None
                    

def jakker():
    with open('Json\\jakker.json') as f:
        jakker_data = json.load(f)
        troejer_data = troejer()
        find_varme_keys = list(findkeys(jakker_data, 'varme'))
        find_lang_jakke = list(findkeys(jakker_data, 'lang'))
        find_vandtaette_keys = list(findkeys(jakker_data, 'vandtaette'))
    if next_hour_precipitation >= 1:                   
        sorter_vandtaette_keys = [i for i, x in enumerate(find_vandtaette_keys) if x]
        tilfaeldige_keys = random.choice(sorter_vandtaette_keys)   
        return jakker_data[tilfaeldige_keys]
    elif -20 <= current_temperature <= 3:
        sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if num >= 8]
        tilfaeldige_keys = random.choice(sorter_varme_keys) 
        return jakker_data['jakker'][tilfaeldige_keys]
    elif 4 <= current_temperature <= 10:
        sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if 4 <= num <= 7]
        tilfaeldige_keys = random.choice(sorter_varme_keys) 
        return jakker_data['jakker'][tilfaeldige_keys]
    elif 10 <= current_temperature <= 40:
        sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if  0 <= num <= 4]
        tilfaeldige_keys = random.choice(sorter_varme_keys) 
        return jakker_data['jakker'][tilfaeldige_keys]


def tshirt():
    with open('Json\\t-shirts.json') as f:
        t_shirt_og_skjorte_data = json.load(f)
        if 18 <= current_temperature <= 40:
            t_shirt_data = random.choice(t_shirt_og_skjorte_data['t-shirts'])
        else:
            skjorte_data = random.choice(t_shirt_og_skjorte_data['skjorter'])
            t_shirt_data = random.choice(t_shirt_og_skjorte_data['t-shirts'])
            return t_shirt_data, skjorte_data


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


def get_random_lang_jakke():
    with open('Json\\jakker.json') as f:
        jakker_data = json.load(f)
        find_lang_jakke_keys = list(findkeys(jakker_data, 'lang'))
        lange_jakke = [jakker_data['jakker'][i] for i, is_long in enumerate(find_lang_jakke_keys) if is_long]
        return random.choice(lange_jakke)

    
def outfit(timeseries):
    outfit = []   
    kategorier = [hovedbeklaedning,accessories, tshirt, troejer, jakker,handsker, bukser,overtraeksbukser, sko,]
    for category_function in kategorier:
        outfit.append(category_function())

    for index, item in enumerate(outfit):
        if item and 'blazer' in item and item['blazer']: 
            long_jacket = get_random_lang_jakke()
            outfit[4] = long_jacket
            break  
        
    print(json.dumps(outfit, indent=4))
      
def main():
    outfit1 = outfit(timeseries)
    symbol_code = get_next_hour_symbol_code(timeseries)
    print(f"temperatur er lige nu {current_temperature} og vejrsituationen er {symbol_code}")
 
if __name__ == "__main__":
    main()

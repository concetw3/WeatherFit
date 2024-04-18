import requests
import json
import random
from datetime import datetime
import os
  
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
   with open('./Json/accessories.json') as f:
        accessories_data = json.load(f)
        return random.choice(accessories_data['baelter'])


def handsker():
   with open('./Json/accessories.json') as f:
        accessories_data = json.load(f)
        find_varme_keys = list(findkeys(accessories_data, 'varme'))
        if -20 <= current_temperature <= 4:
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if num >= 8]
            tilfaeldige_keys = random.choice(sorter_varme_keys) 
            return accessories_data['handsker'][tilfaeldige_keys]
        elif 5 <= current_temperature <= 7:
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if 3 <= num <= 6]
            tilfaeldige_keys = random.choice(sorter_varme_keys)
            return accessories_data['handsker'][tilfaeldige_keys]
        else:
            return None

def slips():
   with open('./Json/accessories.json') as f:
        accessories_data = json.load(f)
        return random.choice(accessories_data['slips'])
                    

def accessories():
    with open('./Json//accessories.json') as f:
        accessories_data = json.load(f)
    symbol_code = get_next_hour_symbol_code(timeseries) 
    if symbol_code == 'clearsky_day':
        return accessories_data['solbriller']

def bukser():
    with open('./Json/bukser.json') as f:
        bukser_data = json.load(f)
        find_varme_keys = list(findkeys(bukser_data, 'varme'))
        if 18 <= current_temperature <= 40:
            return random.choice(bukser_data['shorts'])
        elif 10 <= current_temperature <= 17:
             sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if 3 <= num <= 6]
             tilfaeldige_keys = random.choice(sorter_varme_keys)
             bukser_info = bukser_data['bukser'][tilfaeldige_keys]
             if bukser_info.get('baelte', False):  
                 return bukser_info, baelter()
             else:
                 return bukser_info, None
        elif -10 <= current_temperature <= 9:
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if 5 <= num <= 7]
            tilfaeldige_keys = random.choice(sorter_varme_keys) 
            bukser_info = bukser_data['bukser'][tilfaeldige_keys]
            if bukser_info.get('baelte', False):  
                 return bukser_info, baelter()
            else:
                 return bukser_info, None

def overtraeksbukser():
    with open('./Json/bukser.json') as f:
        bukser_data = json.load(f)
        find_vandtaette_keys = list(findkeys(bukser_data['overtraeksbukser'], 'vandtaet'))
        if next_hour_precipitation >= 1:                         
              sorter_vandtaette_keys = [i for i, x in enumerate(find_vandtaette_keys) if x]
              tilfaeldige_keys = random.choice(sorter_vandtaette_keys)   
              return bukser_data['overtraeksbukser'][tilfaeldige_keys]

def hovedbeklaedning(): 
     with open('./Json/hovedbeklaedning.json') as f:
        hovedbeklaedning_data = json.load(f)
        find_varme_keys = list(findkeys(hovedbeklaedning_data['huer'], 'varme'))
        if current_temperature -20 <= current_temperature <= 4:
            min_varme = 6  
            sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if num >= min_varme]
            tilfaeldige_keys = random.choice(sorter_varme_keys) 
            hovedbeklaedning_data_varme = hovedbeklaedning_data['huer'][tilfaeldige_keys]
            return hovedbeklaedning_data_varme
        else:
            hovedbeklaedning_data = random.choice(hovedbeklaedning_data['kasketter'])
            return hovedbeklaedning_data
   
def sko():
    with open('./Json/sko.json') as f:
        sko_data = json.load(f)
        find_varme_keys = list(findkeys(sko_data, 'varme'))
        find_vandtaette_keys = list(findkeys(sko_data, 'vandtaet'))
    if next_hour_precipitation >= 1:
        sorter_vandtaette_keys = [i for i, x in enumerate(find_vandtaette_keys) if x]
        tilfaeldige_keys = random.choice(sorter_vandtaette_keys)   
        sko_data_vandtaette = sko_data['sko'][tilfaeldige_keys]
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
     with open('./Json/troejer.json') as f:
        troejer_data = json.load(f)
        if 5 <= current_temperature  <= 14:
            troejer_data_rnd = random.choice(troejer_data['troejer'])
            return troejer_data_rnd
        elif -20 <= current_temperature <= 4:    
             troejer_data_sweater = random.choice(troejer_data['sweater'])
             return troejer_data_sweater
        elif current_temperature > 13:
            return None
                    

def jakker():
    with open('./Json/jakker.json') as f:
        jakker_data = json.load(f)
        troejer_data = troejer()
        find_varme_keys = list(findkeys(jakker_data, 'varme'))
        find_lang_jakke = list(findkeys(jakker_data, 'lang'))
        find_vandtaette_keys = list(findkeys(jakker_data, 'vandtaet'))
    if next_hour_precipitation >= 1:                   
        sorter_vandtaette_keys = [i for i, x in enumerate(find_vandtaette_keys) if x]
        tilfaeldige_keys = random.choice(sorter_vandtaette_keys)   
        return jakker_data['jakker'][tilfaeldige_keys]
    elif current_temperature <= 4:
        sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if num >= 8]
        tilfaeldige_keys = random.choice(sorter_varme_keys) 
        return jakker_data['jakker'][tilfaeldige_keys]
    elif 5 <= current_temperature <= 6:
        sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if 6 <= num <= 7]
        tilfaeldige_keys = random.choice(sorter_varme_keys) 
        return jakker_data['jakker'][tilfaeldige_keys]
    elif 7 <= current_temperature <= 12:
        sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if 4 <= num <= 5]
        tilfaeldige_keys = random.choice(sorter_varme_keys) 
        return jakker_data['jakker'][tilfaeldige_keys]
    elif 12 <= current_temperature <= 17:
        sorter_varme_keys = [i for i, num in enumerate(find_varme_keys) if  0 <= num <= 3]
        tilfaeldige_keys = random.choice(sorter_varme_keys) 
        return jakker_data['jakker'][tilfaeldige_keys]
    elif current_temperature > 18:
            return None


def tshirt():
    with open('./Json/t-shirts.json') as f:
        t_shirt_og_skjorte_data = json.load(f)
        if current_temperature > 18:
            t_shirt_data = random.choice(t_shirt_og_skjorte_data['t-shirts'])
            return t_shirt_data
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
    with open('./Json/jakker.json') as f:
        jakker_data = json.load(f)
        find_lang_jakke_keys = list(findkeys(jakker_data, 'lang'))
        lange_jakke = [jakker_data['jakker'][i] for i, is_long in enumerate(find_lang_jakke_keys) if is_long]
        return random.choice(lange_jakke)

def get_random_sweater():
    with open('./Json/troejer.json') as f:
        sweater_data = json.load(f)
        return random.choice(sweater_data['sweater'])

def get_random_troeje():
    with open('./Json/troejer.json') as f:
        troeje_data = json.load(f)
        find_alm_troeje = list(findkeys(troeje_data, 'blazer'))
        alm_troeje = [troeje_data['troejer'][i] for i, blazer in enumerate(find_alm_troeje) if not blazer]
        return random.choice(alm_troeje)

    
def outfit(timeseries):
    outfit = []
    kategorier = [hovedbeklaedning, accessories, tshirt, troejer, jakker, handsker, bukser, overtraeksbukser, sko]
    for category_function in kategorier:
        result = category_function()
        if result is None:
            continue  
        if isinstance(result, tuple):
            for item in result:
                if item and 'navn' in item:
                    outfit.append(item['navn'])
        elif 'navn' in result:
            outfit.append(result['navn'])

    if next_hour_precipitation >= 1:
        if 5 <= current_temperature <= 14:
            for index, item in enumerate(outfit):
                if 'blazer' in item:
                    alm_troeje = get_random_troeje()
                    if alm_troeje and 'navn' in alm_troeje:
                        outfit[3] = alm_troeje['navn']
                        print(outfit[3])
                    break  
    else:
        for index, item in enumerate(outfit):
            if 'blazer' in item:
                long_jacket = get_random_lang_jakke()
                if long_jacket and 'navn' in long_jacket:
                    outfit[4] = long_jacket['navn']
                    print(outfit[4])
                break  
    
    FORMAT = '%Y%m%d%H%M%S'
    directory = "./Logs"
    filename = "vejr.txt"
    new_filename = '%s_%s' % (datetime.now().strftime(FORMAT), filename)
    new_path = os.path.join(directory, new_filename) 

    if not os.path.exists(directory):
        os.mkdir(directory)
    
    with open(new_path, "w") as f:
        json.dump(outfit, f, indent=4)
    
    
    print(json.dumps(outfit, indent=4))
   

  
def main():
    outfit1 = outfit(timeseries)
    symbol_code = get_next_hour_symbol_code(timeseries)
    print(f"temperatur er lige nu {current_temperature} og vejrsituationen er {symbol_code}")
 
if __name__ == "__main__":
    main()

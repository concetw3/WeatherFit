import requests
import json
import random
from datetime import datetime
import os
import http.client, urllib
  
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

def load_json_file(path):
    with open(path) as f:
        return json.load(f)


accessories_data = load_json_file('./Json/accessories.json')
hovedbeklaedning_data = load_json_file('./Json/hovedbeklaedning.json')
bukser_data = load_json_file('./Json/bukser.json')
solbriller_data = load_json_file('./Json/solbriller.json')
sko_data = load_json_file('./Json/sko.json')
troejer_data = load_json_file('./Json/troejer.json')
jakker_data = load_json_file('./Json/jakker.json')
t_shirts_data = load_json_file('./Json/t-shirts.json')


latitude = 55.67
longitude = 12.56
timeseries = get_weather_forecast(latitude, longitude)
current_temperature = get_current_temperature(timeseries)
timeseries = get_weather_forecast(latitude, longitude)
next_hour_precipitation = get_next_hour_precipitation(timeseries)
symbol_code = get_next_hour_symbol_code(timeseries) 

def baelter():
        return random.choice(accessories_data['baelter'])

def handsker():
        if -20 <= current_temperature <= 3:
            return random.choice([item for item in accessories_data['handsker'] if  item['varme'] >= 8])
        elif 3 <= current_temperature <= 5:
            return random.choice([item for item in accessories_data['handsker'] if 3 <= item['varme'] <= 6])
        else:
            return None

def slips():
        return random.choice(accessories_data['slips'])
                    
def solbriller(): 
    if symbol_code in ['fair_day', 'clearsky_day']:
        return random.choice(solbriller_data['solbriller'])
        
def bukser():
    if 18 <= current_temperature <= 40:
        return random.choice(bukser_data['shorts'])
    elif 9 <= current_temperature <= 18:
        return random.choice([item for item in bukser_data['bukser'] if 3 <= item['varme'] <= 6])
    elif -10 <= current_temperature <= 9:
        return random.choice([item for item in bukser_data['bukser'] if 5 <= item['varme'] <= 7])
 
def overtraeksbukser():
        find_vandtaette_keys = [item['vandtaet'] for item in bukser_data['overtraeksbukser']]
        if next_hour_precipitation >= 1:                           
              return random.choice(bukser_data['overtraeksbukser'])

def hovedbeklaedning():    
        if current_temperature -20 <= current_temperature <= 4:
            return random.choice(hovedbeklaedning_data['huer'])
        else:
            return random.choice(hovedbeklaedning_data['kasketter'])
   
def sko():                                                                
        if next_hour_precipitation >= 1:
            return random.choice([item for item in sko_data['sko'] if item['vandtaet']])
        else:
            if current_temperature -20 <= current_temperature <= 2:
                return random.choice([item for item in sko_data['sko'] if 7 <= item['varme'] <= 8])
            elif 2 <= current_temperature <= 15:
                return random.choice([item for item in sko_data['sko'] if 4 <= item['varme'] <= 7])
            elif 15 <= current_temperature <= 40:
                    return random.choice([item for item in sko_data['sko'] if 0 <= item['varme'] <= 2])

def troejer():
        if 3 <= current_temperature  <= 14:
            return random.choice(troejer_data['troejer'])
        elif -20 <= current_temperature <= 3:    
             return random.choice(troejer_data['sweater'])
        elif current_temperature > 13:
            return None
                    

def jakker():  
        if next_hour_precipitation >= 1:    
            return random.choice(item for item in jakker_data['jakker'] if item['vandtaet'])
        elif current_temperature < 3:
            return random.choice([item for item in jakker_data['jakker'] if 7 <= item['varme'] <= 8])
        elif 3 <= current_temperature <= 6: 
            return random.choice([item for item in jakker_data['jakker'] if 6 <= item['varme'] <= 7])
        elif 7 <= current_temperature <= 12:
            return random.choice([item for item in jakker_data['jakker'] if 4 <= item['varme'] <= 5])
        elif 12 <= current_temperature <= 17:
            return random.choice([item for item in jakker_data['jakker'] if 0 <= item['varme'] <= 3])
        elif current_temperature > 18:
                return None 

def tshirt():
        return random.choice(t_shirts_data['t-shirts'])

def skjorter():
        if current_temperature < 17:
            return random.choice(t_shirts_data['skjorter'])
        else: 
            return None
                

def get_random_lang_jakke():
        lange_jakke = [jacket for jacket, is_long in zip(jakker_data['jakker'], findkeys(jakker_data, 'lang')) if is_long]
        return random.choice(lange_jakke) if lange_jakke else None


def get_random_troeje():
        alm_troeje = [troejer for troejer, is_blazer in zip(troejer_data['troejer'], findkeys(troejer_data, 'blazer')) if not is_blazer]
        return random.choice(alm_troeje) if alm_troeje else None

    
def outfit(timeseries):
    outfit = []
    belts = []
    kategorier = [hovedbeklaedning, solbriller, tshirt, skjorter, troejer, jakker, handsker, bukser, overtraeksbukser, sko, baelter]
  
    for category_function in kategorier:
        result = category_function()
        if result is None:
            continue  
        if isinstance(result, tuple):
            for item in result:
                if item and 'navn' in item:
                    if category_function.__name__ == 'bukser' and not item.get('baelte', False):
                        belts.append(item)
                    else:
                        outfit.append({'name': item['navn'], 'category': category_function.__name__, 'image_path': item.get('billede', '')})
        elif 'navn' in result:
            if category_function.__name__ == 'bukser' and not result.get('baelte', False):
                belts.append(result)
            else:
                outfit.append({'name': result['navn'], 'category': category_function.__name__, 'image_path': result.get('billede', '')})
   
    for belt in belts:
        outfit.append({'name': belt['navn'], 'category': 'baelter', 'image_path': belt.get('billede', '')})
   
    if next_hour_precipitation >= 1 and 5 <= current_temperature <= 14:
        for index, item_dict in enumerate(outfit):
            if 'blazer' in item_dict['name'].lower():  
                alm_troeje = get_random_troeje()
                if alm_troeje and 'navn' in alm_troeje:
                    outfit[index]['name'] = alm_troeje['navn']
                break


    blazer_found = False   
    
    if blazer_found:
        for index, item in enumerate(outfit):
            
            jacket_details = next((jacket for jacket in jakker_data if jacket['navn'] == item), None)
            if jacket_details and not jacket_details['lang']: 
                new_jacket = get_random_lang_jakke()
                if new_jacket:
                    outfit[index] = new_jacket['navn']
                    break 
   
    '''            
    FORMAT = '%Y%m%d%H%M%S'
    directory = "/T-jprogram/Logs"
    filename = "vejr.txt"
    new_filename = '%s_%s' % (datetime.now().strftime(FORMAT), filename)
    new_path = os.path.join(directory, new_filename) 

    if not os.path.exists(directory):
    os.mkdir(directory)
    
    with open(new_path, "w") as f:
    json.dump(outfit, f, indent=4)
    '''    
    '''
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
    "token": "agv6vuha11wiv4a7gw55qwjmpp97az",
    "user": "uz7q8o8jtapyur766atyoyuwjxmp4h",
    "message": json.dumps(outfit, indent=4),
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    '''

    json_dump_data = json.dumps(outfit)
    json_load_data = json.loads(json_dump_data)

    print(json_load_data)
    return(json_load_data)


    


  
def main():
    outfit1 = outfit(timeseries)
    symbol_code = get_next_hour_symbol_code(timeseries)
    print(f"temperatur er lige nu {current_temperature} og vejrsituationen er {symbol_code} sandsynligheden for at det kommer til at regne er {next_hour_precipitation}")
 
if __name__ == "__main__":
    main()
   # billede_sekvens()

import requests
import json
from datetime import datetime
from io import StringIO
import random

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
    with open('Json\\sko.json') as f:
        sko_data = json.load(f)
        sko_data = random.choice(sko_data['sko'])
        return sko_data

def jakker():
    with open('Json\\jakker.json') as f:
        jakker_data = json.load(f)
        jakker_data = random.choice(jakker_data['jakker'])
        return jakker_data
    


def troejer():
     with open('Json\\troejer.json') as f:
        troejer_data = json.load(f)
        troejer_data = random.choice(troejer_data['troejer'])
        return troejer_data


def tshirt():
    with open('Json\\t-shirts.json') as f:
        t_shirt_data = json.load(f)
        t_shirt_data2 = random.choice(t_shirt_data['t-shirts'])
        t_shirt_data_3 = t_shirt_data['t-shirts']
        return t_shirt_data2


def regntoej():
    nextonehour()
    Rain_in_millimeter_next_hour = nextonehour()
    with open('Json\\bukser.json') as f:
        bukser_data = json.load(f)
    if Rain_in_millimeter_next_hour >= 1:
        regn_bukser = random.choice(bukser_data['overtraeksbukser'])
        return regn_bukser
       
      
#Hente data
my_headers = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
response = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/complete?lat=55.67&lon=12.56", headers = {'User-Agent':my_headers})

#Lave det til en dict
data = json.loads(response.text)

properties = data['properties']
timeseries = properties['timeseries']

#Funktion til at søge i dict
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

def nextonehour():
    Access_properties = data['properties']
    Access_timeseries = Access_properties['timeseries']
    Access_data = Access_timeseries[0]['data']
    Access_next1hours = Access_data['next_1_hours']
    Access_next1hours_summary = Access_next1hours['summary']
    Access_next1hours_details = Access_next1hours['details']
    Rain_in_millimeters = Access_next1hours_details['precipitation_amount']
    return Rain_in_millimeters



def temperatur_right_now():
    Access_properties = data['properties']
    Access_timeseries = Access_properties['timeseries']
    Access_data = Access_timeseries[0]['data']
    Access_instant = Access_data['instant']
    Access_temperatur = Access_instant['details']['air_temperature']

    Temperatur = Access_temperatur
    print("The date and time is " + str(datetime.now().replace(microsecond=0)))
    print("The temperature is at " + str(Temperatur) + " degrees celcius outside right now")

     
def next_couple_of_hours():
    Access_properties = data['properties']
    Access_timeseries = Access_properties['timeseries']
    Access_data = Access_timeseries[0]['data']
    Access_next12hours = Access_data['next_12_hours']
    Access_next12hours_summary = Access_next12hours['summary']
    print("During the next 12 hours there will be " + Access_next12hours_summary['symbol_code'])   

def kl12():
    iso_date_kl12 = datetime.now().replace(hour=12,minute=0,second=0,microsecond=0,).isoformat()
    iso_date_kl12z ='Z'
    iso_date_kl12_kombineret = ''.join([iso_date_kl12,iso_date_kl12z])

    time = list(findkeys(timeseries, 'time'))
    Klokken18 = time.index(iso_date_kl12_kombineret)

    Access_properties = data['properties']
    Access_timeseries = Access_properties['timeseries']
    Access_data = Access_timeseries[Klokken18]['data']
    Access_instant = Access_data['instant']
    Access_temperatur = Access_instant['details']['air_temperature']

    Temperatur = Access_temperatur
    print("The temperature at 18pm will be " + str(Temperatur) + " degrees celcius outside")
   

def kl18():
    global Klokken18
    iso_date_kl18 = datetime.now().replace(hour=18,minute=0,second=0,microsecond=0,).isoformat()
    iso_date_kl18z ='Z'
    iso_date_kl18_kombineret = ''.join([iso_date_kl18,iso_date_kl18z])

    time = list(findkeys(timeseries, 'time'))
    Klokken18 = time.index(iso_date_kl18_kombineret)

    Access_properties = data['properties']
    Access_timeseries = Access_properties['timeseries']
    Access_data = Access_timeseries[Klokken18]['data']
    Access_instant = Access_data['instant']
    Access_temperatur = Access_instant['details']['air_temperature']

    Temperatur = Access_temperatur
    print("The temperature at 18pm will be " + str(Temperatur) + " degrees celcius outside")
    return Klokken18
def kl23():
    #programmet finder ud af hvilken dato det er og hvad klokken er, 
    #og laver datoen og tiden om med .replace funktionen. så den passer til den givne dato. "2024-02-08T19:32:44.55" bliver til "2024-02-08T23:00:00"
    #Variablen er en string
    iso_date_kl23 = datetime.now().replace(hour=23,minute=0,second=0,microsecond=0,).isoformat()
    #Simple string variable der indeholder værdien 'Z'
    iso_date_kl23z ='Z'
    #Kombinere begge string variabler så det bliver til "2024-02-08T23:00:00Z" -- som skal bruges i 'time' funktionen der leder efter klokkeslættet
    iso_date_kl23_kombineret = ''.join([iso_date_kl23,iso_date_kl23z])
    #Funktion der leder i list efter alle tidspunkter og putter dem i en list
    time = list(findkeys(timeseries, 'time'))
    #Finder indextallet i listen 'time' og propper det ind i variablen 'Klokken23' som en integer -- som indeholder alle de andre data fra den time som nedbør, sol, temperatur
    Klokken23 = time.index(iso_date_kl23_kombineret)
    #Går ind i api'en og iterater først via keys indtil vi når den store nested list
    Access_properties = data['properties']
    Access_timeseries = Access_properties['timeseries']
    #Her anvender vi vores indextal vi har fundet i 'Klokken23' til at alle data fra kl 23
    Access_data = Access_timeseries[Klokken23]['data']
    Access_instant = Access_data['instant']
    Access_temperatur = Access_instant['details']['air_temperature']

    Temperatur2 = Access_temperatur
    print("The temperature at 23pm will be " + str(Temperatur2) + " degrees celcius outside")
    #print("The index of kl 23 is: " + str(Klokken23))



def outfit():
    outfit = []  
    outfit.append(sko())
    outfit.append(bukser())
    outfit.append(tshirt())
    outfit.append(troejer())
    outfit.append(jakker())
    outfit.append(hovedbeklaedning())
    #outfit.append(regntoej()) 
    outfit = json.dumps(outfit, indent=4,)
    print(outfit)


 

        
   


outfit()






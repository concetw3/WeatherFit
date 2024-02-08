import requests
import json
from datetime import datetime

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

#Søge i data med funktion
time = list(findkeys(timeseries, 'time'))

        #vejret = list(findkeys(data, 'symbol_code'))

#Tidspunkt lige nu uden rigtige minut eller sekunder
iso_date = datetime.now().replace(minute=0,second=0,microsecond=0,).isoformat()
def temperatur_right_now():
    Access_properties = data['properties']
    Access_timeseries = Access_properties['timeseries']
    Access_data = Access_timeseries[0]['data']
    Access_instant = Access_data['instant']
    Access_temperatur = Access_instant['details']['air_temperature']

    Temperatur = Access_temperatur
    print("The date and time is " + str(datetime.now().replace(microsecond=0)))
    print("The temperature is at " + str(Temperatur) + " degrees celcius outside right now")
    

 #Kommer det til at regne eller sne de næste 12 time?   
def next_couple_of_hours():
    Access_properties = data['properties']
    Access_timeseries = Access_properties['timeseries']
    Access_data = Access_timeseries[0]['data']
    Access_next12hours = Access_data['next_12_hours']
    Access_next12hours_summary = Access_next12hours['summary']

    print(Access_next12hours_summary['symbol_code'])

iso_date_kl18 = datetime.now().replace(hour=18,minute=0,second=0,microsecond=0,).isoformat()
iso_date_kl18z ='Z'
iso_date_kl18_kombineret = ''.join([iso_date_kl18,iso_date_kl18z])

def kl18():
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
    print(Klokken18)

def kl23():
    #programmet finder ud af hvilken dato det er og hvad klokken er, 
    #og laver datoen og tiden om med .replace funktionen. så den passer til den givne dato. "2024-02-08T19:32:44.55" bliver til "2024-02-08T23:00:00"
    #Variablen er en string
    iso_date_kl18 = datetime.now().replace(hour=23,minute=0,second=0,microsecond=0,).isoformat()
    #Simple string variable der indeholder værdien 'Z'
    iso_date_kl18z ='Z'
    #Kombinere begge string variabler så det bliver til "2024-02-08T23:00:00Z" -- som skal bruges i 'time' funktionen der leder efter klokkeslættet
    iso_date_kl18_kombineret = ''.join([iso_date_kl18,iso_date_kl18z])
    #Funktion der leder i list efter alle tidspunkter og putter dem i en list
    time = list(findkeys(timeseries, 'time'))
    #Finder indextallet i listen 'time' og propper det ind i variablen 'Klokken23' som en integer -- som indeholder alle de andre data fra den time som nedbør, sol, temperatur
    Klokken23 = time.index(iso_date_kl18_kombineret)
    #Går ind i api'en og iterater først via keys indtil vi når den store nested list
    Access_properties = data['properties']
    Access_timeseries = Access_properties['timeseries']
    #Her anvender vi vores indextal vi har fundet i 'Klokken23' til at alle data fra kl 23
    Access_data = Access_timeseries[Klokken23]['data']
    Access_instant = Access_data['instant']
    Access_temperatur = Access_instant['details']['air_temperature']

    Temperatur = Access_temperatur
    print("The temperature at 23pm will be " + str(Temperatur) + " degrees celcius outside")
    print("The index of kl 23 is: " + str(Klokken23))




#print("During the next 1 hour there will be " + Access_timeseries[2]['next_1_hours'])
#print("The temperature is at " + Access_timeseries[0]['air_temperature'] + " degrees celcius outside right now")
next_couple_of_hours()
kl18()
kl23()


#print(Access_instant['details']['air_temperature'])





import requests
import json
from datetime import datetime

#Hente data
my_headers = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
response = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/complete?lat=55.67&lon=12.56", headers = {'User-Agent':my_headers})


#Lave det til en dict
data = json.loads(response.text)

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
#temp = list(findkeys(data, 'air_temperature'))
#vejret = list(findkeys(data, 'symbol_code'))

#Tidspunkt lige nu uden rigtige minut eller sekunder
iso_date = datetime.now().replace(minute=0,second=0,microsecond=0,).isoformat()

voresliste = data['properties']
voresliste2 = voresliste['timeseries']
#testp
#listdata = list(data.keys())[2]['air_temperature']
#Printe diverse
""""print("The date and time is " + str(datetime.now()))
print("During the next 12 hours there will be " + vejret[0])
print("During the next 1 hour there will be " + vejret[1])
print("The temperature is at " + str(temp[1]) + " degrees celcius outside right now")"""
#print(list(data.values()))
print(voresliste2[0])
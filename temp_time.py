import requests

def gettat(lat,lon):
 url="https://api.darksky.net/forecast/499e95d4fe8a037e6f001b7e5ae8d7d5/"+str(float(lat))+","+str(float(lon))
 response=requests.get(url)
 data=response.json()
 actual=data['currently']['temperature']
 return actual

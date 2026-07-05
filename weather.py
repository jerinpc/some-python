import requests
from config import API 

city_name=input('Enter a city name : ').lower().strip()

def weather(city_name):
    weather_api = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&units=metric"
    response=requests.get(weather_api)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        print('',response.status_code)

data=weather(city_name)

#tempinc = data['main']['temp']- 273.15 
print(f"Humidity : {data['main']['humidity']}") 
#print(f"Temperature : {tempinc:.2f}°C") 
print(f"Temperature : {data['main']['temp']}°C") 
print(f"Feels like : {data['main']['feels_like']}") 
print(f"Wind : {data['wind']['speed']}") 
print(f"Place : {data['name']}") 
print(f"Country : {data['sys']['country']}")

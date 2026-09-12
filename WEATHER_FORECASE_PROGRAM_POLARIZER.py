import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name=input("Enter city name: ")
complete_url= base_url+"appid="+api_key+"&q="+city_name
response=requests.get(complete_url)
x=response.json()

if{x["cod"] != "404"}:
         
         y=x["main"]
         current_temperature=y["temp"]
         current_pressure=y["pressure"]
         current_humidity=y["humidity"]
         current_wind=x["wind"]["speed"]
         z=x["weather"]
         weather_description=z[0]["description"]

         print(f"Temperature(in Celcius):{current_temperature-273.15:.2f}")
         print(f"Pressure(in hPa):{current_pressure}")
         print(f"Humidity(in percentage):{current_humidity}"+"%")
         print(f"Weather description:{weather_description.capitalize()}")       
         print(f"Wind speed(in kph):{current_wind}")
else:
        print("City not found!") 













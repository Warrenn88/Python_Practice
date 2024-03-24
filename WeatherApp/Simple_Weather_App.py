import requests

def weather_api_call(zip_code):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "e8751357b838b575a20019990b1785f5"
    complete_url = base_url + "appid=" + api_key + "&zip=" + str(zip_code) + "&units=imperial"
    responsejson = requests.get(complete_url)
    return responsejson.json()

while True:
    zip_code = int(input("Please input your zip code for a weather report,\nor '0' to end program:"))
    if zip_code == 0:
        break
    else:
        weather_data = weather_api_call(zip_code)
        while True:
             if 'main' in weather_data:
                 print("Temperature:", weather_data['main']['temp'], "F")
                 print("Feels like:", weather_data['main']['feels_like'], "F")
                 print("Minimum Temperature:", weather_data['main']['temp_min'], "F")
                 print("Maximum Temperature:", weather_data['main']['temp_max'], "F")
             else:
                 print("Temperature data not found for the provided ZIP code.")

             if 'weather' in weather_data and len(weather_data['weather']) > 0:
                 main_weather = weather_data['weather'][0]['main']
                 print("Main Weather Condition:", main_weather)
                 break
             else:
                 print("Weather data not found for the provided ZIP code.")
                 break
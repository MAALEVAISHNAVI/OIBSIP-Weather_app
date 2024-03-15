import requests

def get_weather(api_key, location):
    base_url="https://api.openweathermap.org/data/2.5/weather"
    params = {'q':location, 'appid':api_key, 'units':'metric'}

    try:
        response=requests.get(base_url, params=params)
        data=response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None
        
    except Exception as e:
        print(f"Error in fetching weather data: {str(e)}")
        return None
    
def display_weather(weather_data):
    if weather_data:
        print("\n Current Weather: ")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}")
        print(f"Humidity: {weather_data['main']['humidity']}")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    
    else:
        print("Weather data not available")

if __name__ == "__main__":
    api_key="41cc441ee862f14fdf39aaf6695649f5"
    location=input("Enter city or ZIP code: ")
    weather_data=get_weather(api_key, location)

    if weather_data:
        display_weather(weather_data)


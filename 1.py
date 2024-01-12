import requests
def get_weather_forecast():
    """
    Gets the weather forecast for the current location.

    Returns:
        The weather forecast.
    """
    api_key = "055a81cfd91e9aea50b077b99ca00c66"
    location = "KOTA"
    url = f"https://api.weatherstack.com/current?access_key=${api_key}&query=${location}"
    response = requests.get(url)
    data = response.json()
    print(data)
   
get_weather_forecast()
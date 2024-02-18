import requests
import json
from pprint import *


def getWeather():
    url = "https://api.weatherapi.com/v1/current.json?key=d0feacb41e1345dcb66203126241502&q=Austin&aqi=no"
    data = requests.get(url).content
    data = json.loads(data)
    current = data["current"]
    pprint(data)
    message = f"Rain: {current['precip_in']} in.\
            \nTemp: {current['temp_f']}F, feels like {current['feelslike_f']}F\
            \nWind: {current['wind_dir']} at {current['wind_mph']} mph."
    print(message)
    return message


def getGCal():
    pass


def getTasks():
    pass


def getNews():
    pass


def getStocks():
    pass


def generateMessage():
    weather = getWeather()
    return weather


if __name__ == "__main__":
    generateMessage()

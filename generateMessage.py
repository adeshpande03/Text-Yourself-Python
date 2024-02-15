import requests
from datetime import date
import os


def getWeather():
    today = date.today()

    url = f"https://api.weatherapi.com/v1/history.json?key={os.environ.get('WEATHER_API')}&q=Austin&dt={today.strftime('%Y-%m-%d')}"
    # print(requests.get(url).content)
    # print(url)
    return requests.get(url.content)


def getGCal():
    pass


def getTasks():
    pass


def getNews():
    pass


def getStocks():
    pass


def generateMessage():
    return getWeather()


getWeather()

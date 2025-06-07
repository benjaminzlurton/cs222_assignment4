import json
import urllib.request

weatherData = json.loads(urllib.request.urlopen("https://api.weather.gov/points/40.1934,-85.3864").read())
weatherForecast = json.loads(urllib.request.urlopen(weatherData["properties"]["forecast"]).read())

for forecastPeriod in weatherForecast['properties']['periods']:
    print(f"{forecastPeriod['name']} - {forecastPeriod['temperature']}°F \n{forecastPeriod['detailedForecast']}\n")
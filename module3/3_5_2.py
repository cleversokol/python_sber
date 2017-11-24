import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"

params = {
    'q': 'Saint-Petersburg',
    'appid': ''
}

res = requests.get(api_url, params=params)
print(res.status)
print(res.headers["Content-Type"])
data = res.json()
print(data["main"]["temp"])
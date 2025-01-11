import requests 

api_url = "http://api.openweathermap.org/data/2.5/weather"

city = input('City? ')

# http://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=
# 7e0a673e0be7647a6760e1ef1d78e9e6&units=metric
# Вот что это значит и как это соединяется с юрл выше, если city – Moscow
params = {
    'q': city, # 'Saint-Petersburg' он не принял хех - 404
    'appid': "7e0a673e0be7647a6760e1ef1d78e9e6",
    'units': 'metric'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers['Content-Type'])
# print(res.json())

data = res.json()
template = 'Current temperature in {} is {}'
print(template.format(city, data['main']['temp']))
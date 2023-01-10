import requests

city = "Moscow,RU"
appid = "c5e1aec170571f9f30a66189140f8048"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city,
                     'units': 'metric',
                     'lang': 'ru',
                     'APPID': appid})
data = res.json()

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city,
                           'units': 'metric',
                           'lang': 'ru',
                           'APPID': appid})
data = res.json()

print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("____________________________")


# ---------------------------------
# Homework
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city,
                     'units': 'metric',
                     'lang': 'ru',
                     'APPID': appid})
data = res.json()
print('Weather for today:')
print("Visibility:", data['visibility'])
print("Wild:")
print("- speed:", data['wind']['speed'])
print("- deg:", data['wind']['deg'])
print("- gust:", data['wind']['gust'])


res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city,
                           'units': 'metric',
                           'lang': 'ru',
                           'APPID': appid})
data = res.json()
print('Weather for week:')
for i in data['list']:
    print("Visibility:", i['visibility'])
    print("Wild:")
    print("- speed:", i['wind']['speed'])
    print("- deg:", i['wind']['deg'])
    print("- gust:", i['wind']['gust'])
    print("____________________________")

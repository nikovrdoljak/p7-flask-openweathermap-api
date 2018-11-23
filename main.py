from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests
from datetime import datetime
from flask_caching import Cache
app = Flask(__name__)
bootstrap = Bootstrap(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
@cache.cached(timeout=1)
def index():
    # 2643743 London, 3186952 Zadar
    return city(3186952)

@app.route('/<id>')
@cache.cached(timeout=1)
def city(id):
    parameters = { 'appid': 'OVDJE_STAVITE_SVOJ_OPENWEATHEMAP_APPID',
    'id': id, 'units': 'metric', 'lang': 'hr' }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    url2 = 'https://api.openweathermap.org/data/2.5/forecast'
    response = requests.get(url, params=parameters)
    response2 = requests.get(url2, params=parameters)
    jsonWeather = response.json()
    jsonForecast = response2.json()
    dt = datetime.utcfromtimestamp( jsonWeather['dt'] )
    now = datetime.now()
    return render_template('index.html', jsonForecast=jsonForecast,
        jsonWeather=jsonWeather, 
        dt=dt, now=now)



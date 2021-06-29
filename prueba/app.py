from flask import Flask, render_template, request

import requests
app = Flask(__name__)

@app.route('/city')
def search_city():
    API_KEY = '15a69e441bf1a3d224eb0dae7d1505e7'  
    city = request.args.get('q') 

    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()

  
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error temperatura {city.title()}. Mensaje de error = {message}'

    viento = response.get('wind', {}).get('speed')
    if  viento:
        x  = f'En {city.title()} hace una velocidad del viento de {viento} '
    else:
        x  = f'Error temperatura {city.title()}'

    temp_actual= response.get('main', {}).get('temp')
    if temp_actual:
        temp_actual_celsius = round(temp_actual - 273.15, 2)
        y  = f'y una temperatura de de {temp_actual_celsius} &#8451;'
    else:
        y  = f'Error temperatura en {city.title()}'
    return x + y
from flask import Flask, request
from pprint import pprint
import requests

app = Flask(__name__)
#configure_routes(app)

@app.route('/city')

def read_data(url):   
    url = 'http://api.openweathermap.org/data/2.5/weather?q=madrid&APPID=15a69e441bf1a3d224eb0dae7d1505e7'
    return requests.get(url)


def test_get_status_code_200():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=madrid&APPID=15a69e441bf1a3d224eb0dae7d1505e7'    
    response = read_data(url)
    assert (response.status_code == 200) 

'''def test_get_status_code_404():
    url = 'http://api.openweathe/data/2.5/weather?q=madrid&APPID=15a69e441bf1a3d224eb0dae7d1505e7'    
    response = read_data(url)
    assert (response.status_code == 404)'''

def test_get_status_code_401():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=madrid&APPID=15a6'    
    response = read_data(url)
    pprint(response)
    assert (response.status_code == 401)

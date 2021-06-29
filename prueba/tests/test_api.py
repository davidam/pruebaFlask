import pytest
import requests
from flaskr.db import get_db



def test_get_status_code_200():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=madrid&APPID=15a69e441bf1a3d224eb0dae7d1505e7'    
    response = requests.get(url)
    assert (response.status_code == 200) 

def test_get_status_code_401():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=madrid&APPID=15a6'
    response = requests.get(url)
    assert(response.status_code == 401)

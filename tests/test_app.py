import requests

base_url = 'http://0.0.0.0:8080/api/dogs/'


def test_get_all_dogs():
    """Tests a call to get all dogs"""
    res = requests.get(base_url).json()
    assert isinstance(res, list), "The response should be a list."
  

def test_get_dog():
    """Tests a call to get a specific dog"""
    res = requests.get('{0}norma'.format(base_url)).json()
    assert isinstance(res, dict), "The response should be a dictionary."
    
    
def test_add_dog():
    """Tests a call to add a new dog"""
    

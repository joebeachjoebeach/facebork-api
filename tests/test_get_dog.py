import json
from fixtures import temp_app, temp_db

def test_get_dog(temp_app, temp_db):
    """Tests to make sure getting a specific dog works."""
    res = temp_app.get('/api/dogs/normie')
    res_data = json.loads(res.data)
    assert res.status_code == 200, 'The response should have a status code of 200 - OK.'
    assert isinstance(res_data, dict), 'The data should be a json dict.'
    assert '_id' not in res_data


def test_get_nonexistent_dog(temp_app, temp_db):
    """Tests to see if lookup of nonexistent dog fails properly."""
    res = temp_app.get('api/dogs/bob')
    res_data = json.loads(res.data)
    assert res.status_code == 404, 'The response should be 404 -- NOT FOUND'
    assert isinstance(res_data, dict), 'The data should be a json dict.'
    assert 'error' in res_data

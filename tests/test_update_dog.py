import json
from dummy_data import (normie_update, 
                        normie_update_color,
                        normie_update_breed,
                        normie_update_name,
                        normie_update_id)
from fixtures import temp_app, temp_db

def test_update_dog(temp_app, temp_db):
    """Tests updating a dog with valid data"""
    res = temp_app.put('/api/dogs/normie',
                        data=json.dumps(normie_update),
                        content_type='application/json')
    res_data = json.loads(res.data)
    assert res.status_code == 200, 'The response code should be 200 -- OK.'
    assert isinstance(res_data, dict), 'The response data should be a json dictionary.'
    assert 'owners' in res_data, 'The response should have an owners key now.'
    assert res_data['weight'] == 95

    dogs = temp_db
    normie_in_db = dogs.find_one({'_id': 'normie'})
    assert 'owners' in normie_in_db, 'The document should have a new owners key.'
    assert normie_in_db['weight'] == 95, 'The weight should now be 95.'
    assert 'brownie' in normie_in_db['friends'], 'Brownie should now be in the friends list.'


def test_update_bad_color(temp_app, temp_db):
    """Tests that you can't change a dog's colors"""
    res = temp_app.put('/api/dogs/normie',
                        data=json.dumps(normie_update_color),
                        content_type='application/json')
    res_data = json.loads(res.data)
    assert res.status_code == 400, 'The response code should be 400 -- BAD REQUEST.'
    assert isinstance(res_data, dict), 'The response should be a json dictionary.'
    assert 'error' in res_data, 'The respsonse should contain the key "error".'


def test_update_bad_breed(temp_app, temp_db):
    """Tests that you can't change a dog's breed"""
    res = temp_app.put('/api/dogs/normie',
                        data=json.dumps(normie_update_breed),
                        content_type='application/json')
    res_data = json.loads(res.data)
    assert res.status_code == 400, 'The response code should be 400 -- BAD REQUEST.'
    assert isinstance(res_data, dict), 'The response should be a json dictionary.'
    assert 'error' in res_data, 'The respsonse should contain the key "error".'


def test_update_bad_name(temp_app, temp_db):
    """Tests that you can't change a dog's name"""
    res = temp_app.put('/api/dogs/normie',
                        data=json.dumps(normie_update_name),
                        content_type='application/json')
    res_data = json.loads(res.data)
    assert res.status_code == 400, 'The response code should be 400 -- BAD REQUEST.'
    assert isinstance(res_data, dict), 'The response should be a json dictionary.'
    assert 'error' in res_data, 'The respsonse should contain the key "error".'


def test_update_bad_id(temp_app, temp_db):
    """Tests that you can't change a dog's _id"""
    res = temp_app.put('/api/dogs/normie',
                        data=json.dumps(normie_update_id),
                        content_type='application/json')
    res_data = json.loads(res.data)
    assert res.status_code == 400, 'The response code should be 400 -- BAD REQUEST.'
    assert isinstance(res_data, dict), 'The response should be a json dictionary.'
    assert 'error' in res_data, 'The respsonse should contain the key "error".'

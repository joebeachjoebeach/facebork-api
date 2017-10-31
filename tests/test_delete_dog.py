import json
from fixtures import temp_app, temp_db

def test_delete_dog(temp_app, temp_db):
    """Tests deleting a dog."""
    res = temp_app.delete('/api/dogs/normie')
    res_data = json.loads(res.data)
    assert res.status_code == 200, 'The response should be 200 -- OK.'
    assert isinstance(res_data, dict), 'The response should be a json dict.'
    assert 'result' in res_data, 'The response should contain the key "result".'

    dogs = temp_db
    dog_in_db = dogs.find_one({'_id': 'normie'})
    assert dog_in_db is None


def test_delete_nonexistent_dog(temp_app, temp_db):
    """Tests that you can't delete a nonexistent dog"""
    res = temp_app.delete('/api/dogs/blorma')
    res_data = json.loads(res.data)
    assert res.status_code == 404, 'The response should be 404 -- NOT FOUND.'
    assert isinstance(res_data, dict), 'The data should be a json dict.'
    assert 'error' in res_data, 'The response should contain the key "error".'

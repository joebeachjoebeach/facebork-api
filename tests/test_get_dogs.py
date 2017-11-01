import json
from fixtures import temp_app, temp_db

def test_get_dogs(temp_app, temp_db):
    """Tests to make sure getting all dogs works."""
    res = temp_app.get('/api/dogs')
    res_data = json.loads(res.data)
    assert res.status_code == 200, 'The response should have a status code of 200 - OK.'
    assert isinstance(res_data, list), 'The data should be a json list.'
    assert '_id' not in res_data[0]

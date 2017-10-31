import json
from fixtures import temp_app, temp_db

def test_get_dogs(temp_app, temp_db):
    """Tests to make sure getting all dogs works."""
    res = temp_app.get('/api/dogs')
    assert res.status_code == 200, 'The response should have a status code of 200 - OK.'
    assert isinstance(json.loads(res.data), list), 'The data should be a json list.'

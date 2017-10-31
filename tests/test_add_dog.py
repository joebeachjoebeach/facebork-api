import json
from fixtures import temp_app, temp_db
from dummy_data import (normie,
                        leelou,
                        leelou_unformatted,
                        leelou_incomplete,)

def test_add_dog(temp_app, temp_db):
    """Tests to make sure adding a new dog works."""
    res = temp_app.post('/api/dogs', data=json.dumps(leelou), content_type='application/json')
    res_data = json.loads(res.data)
    assert res.status_code == 201, 'The response should have a status code of 201 - CREATED.'
    assert isinstance(res_data, dict), 'The data should be a json dict.'
    assert '_id' in res_data, 'The response should have a new _id key.'

    dogs = temp_db
    dog_in_db = dogs.find_one({'_id': 'leelou'})
    assert dog_in_db is not None
    assert dog_in_db['weight'] == 45


def test_add_unformatted_dog(temp_app, temp_db):
    """Tests to make sure an unformatted dog gets properly formatted."""
    res = temp_app.post('/api/dogs',
                        data=json.dumps(leelou_unformatted),
                        content_type='application/json')
    res_data = json.loads(res.data)
    assert res.status_code == 201, 'The response should have a status code of 201 - CREATED.'
    assert isinstance(res_data, dict), 'The data should be a json dict.'
    assert '_id' in res_data, 'The response should have a new _id key.'

    dogs = temp_db
    dog_in_db = dogs.find_one({'_id': 'leelou'})
    assert dog_in_db is not None
    assert dog_in_db['weight'] == 45
    assert all (key in res_data for key in ('friends', 'owners', 'colors')), \
        'The response should have friends, owners, and colors keys.'
    assert isinstance(dog_in_db['friends'], list)
    assert isinstance(dog_in_db['owners'], list)
    assert isinstance(dog_in_db['colors'], list)
    assert isinstance(dog_in_db['breed'], list)


def test_add_dupe_dog(temp_app, temp_db):
    """Tests to see if duplicate dog entry fails."""
    res = temp_app.post('/api/dogs',
                        data=json.dumps({'name': 'normie'}),
                        content_type='application/json')
    assert res.status_code == 400, 'The response should have a status code of 400 -- BAD REQUEST.'
    assert isinstance(json.loads(res.data), dict), 'The data should be a json dict.'


def test_add_incomplete_dog(temp_app, temp_db):
    """Tests to see if dog with no 'name' fails."""
    res = temp_app.post('/api/dogs',
                        data=json.dumps(leelou_incomplete),
                        content_type='application/json')
    assert res.status_code == 400, 'The response should have a status code of 400 -- BAD REQUEST.'
    assert isinstance(json.loads(res.data), dict), 'The data should be a json dict.'

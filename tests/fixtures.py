import pymongo
from pytest import fixture
from app import create_app, bp
from dummy_data import normie, fido

def create_test_app():
    return create_app(TESTING=True, DEBUG=False, MONGO_DBNAME='faceborktest')


@fixture
def temp_db():
    """Sets up and populates our test database collection."""
    client = pymongo.MongoClient()
    db = client.faceborktest
    col = db.dogs
    col.insert_one(normie)
    col.insert_one(fido)
    yield col
    col.delete_many({})


@fixture
def temp_app():
    """Sets up and returns a flask test client app."""
    test_app = create_test_app()
    # test_app.register_blueprint(bp)
    return test_app.test_client()

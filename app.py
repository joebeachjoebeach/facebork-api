from flask import Flask, jsonify, make_response, request, Blueprint, url_for
from flask_pymongo import PyMongo
import json
from utils import format_dog, create_public_dog

mongo = PyMongo()

def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_object('config')
    app.config.update(config_overrides)
    mongo.init_app(app)
    app.register_blueprint(bp)
    return app


bp = Blueprint('bp', __name__)

@bp.route('/api/dogs/', methods=['GET'])
@bp.route('/api/dogs', methods=['GET'])
def get_all_dogs():
    """Returns a list of all the dogs in the collection."""
    return jsonify([create_public_dog(dog) for dog in mongo.db.dogs.find()])


@bp.route('/api/dogs/', methods=['POST'])
@bp.route('/api/dogs', methods=['POST'])
def add_dog():
    """Adds a new dog to the collection."""
    if not request.json:
        return make_response(jsonify({'error': 'Request body must be json.'}), 400)

    if not 'name' in request.json:
        return make_response(jsonify({'error': 'Request must have at least a "name" key.'}), 400)

    dog = format_dog(request.json)

    dog_in_db = mongo.db.dogs.find_one({'_id': dog['name']})
    if (dog_in_db is not None):
        return make_response(jsonify({'error': 'Resource already exists'}), 400)
    
    dog['_id'] = dog['name']
    mongo.db.dogs.insert_one(dog)
    return jsonify(dog), 201
    
    
@bp.route('/api/dogs/<string:dog>/', methods=['GET'])
@bp.route('/api/dogs/<string:dog>', methods=['GET'])
def get_dog(dog):
    """Returns the requested dog."""
    dog_in_db = mongo.db.dogs.find_one({'_id': dog})
    if (dog_in_db is not None):
        return jsonify(create_public_dog(dog_in_db))
    return make_response(jsonify({'error': 'Resource not found on server.'}), 404)


@bp.route('/api/dogs/<string:dog>/', methods=['DELETE'])
@bp.route('/api/dogs/<string:dog>', methods=['DELETE'])
def delete_dog(dog):
    """Deletes the specified dog."""
    dog_in_db = mongo.db.dogs.find_one({'_id': dog})
    if (dog_in_db is not None):
        mongo.db.dogs.delete_one({'_id': dog})
        return jsonify({'result': True})
    return make_response(jsonify({'error': 'Resource not found on server.'}), 404)


@bp.route('/api/dogs/<string:dog>/', methods=['PUT'])
@bp.route('/api/dogs/<string:dog>', methods=['PUT'])
def update_dog(dog):
    """Updates the specified dog with the provided data."""
    dog_in_db = mongo.db.dogs.find_one({'_id': dog})

    if (dog_in_db is not None):
        dog_updates = format_dog(request.json)
        # can't change the _id:
        if '_id' in dog_updates and dog_updates['_id'] != dog_in_db['_id']:
            return make_response(jsonify({'error': 'Cannot change id of dog.'}), 400) 
        # can't change the name
        if 'name' in dog_updates and dog_updates['name'] != dog_in_db['name']:
            return make_response(jsonify({'error': 'Cannot change name of dog.'}), 400) 
        # can't change the colors if they're already set
        if ('color' in dog_updates or 'colors' in dog_updates) and 'colors' in dog_in_db:
            return make_response(jsonify({'error': 'Cannot change colors of dog.'}), 400)
        # can't change the breed if it's already set
        if 'breed' in dog_updates and 'breed' in dog_in_db:
            return make_response(jsonify({'error': 'Cannot change breed of dog.'}), 400)

        if 'friends' in dog_updates:
            new_friends = list(set(dog_updates['friends'] + dog_in_db['friends']))
            dog_updates['friends'] = new_friends

        mongo.db.dogs.update_one({'_id': dog}, {'$set': dog_updates})
        return jsonify(mongo.db.dogs.find_one({'_id': dog}))

    return make_response(jsonify({'error': 'Resource not found on server.'}), 404)
    

if __name__ == '__main__':
    app = create_app()
    # app.register_blueprint(bp)
    app.run(port=8000)

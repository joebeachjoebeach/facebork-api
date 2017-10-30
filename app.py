from flask import Flask, jsonify, abort, make_response, request
from pymongo import MongoClient

client = MongoClient()
db = client.dogdb
dogs = db.dogs

app = Flask(__name__)

@app.route('/api/dogs/')
@app.route('/api/dogs')
def get_all_dogs():
    return jsonify([dog for dog in dogs.find()])
    
    
@app.route('/api/dogs/<string:dog>/')
@app.route('/api/dogs/<string:dog>')
def get_dog(dog):
    return jsonify(dogs.find_one({'_id': dog}))
    
    
if __name__ == '__main__':
    app.run(debug=True)

from pymongo import MongoClient

client = MongoClient()
db = client.faceborktest
col = db.dogs

norma = {
    '_id': 'normie',
    'name': 'normie',
    'breed': ['great pyrenees', 'poodle'],
    'colors': ['black', 'white'],
    'weight': 85,
    'friends': ['joel', 'ellie', 'zelda', 'ida', 'jelly roll', 'leeloo', 'woody']
}

col.insert_one(norma)


## Facebork API

Finally, just what you've been looking for: a dog-social-network API.


### Usage

**Get all dogs in the network**:

GET: `/api/dogs/`

**Get a specific dog**:

GET: `/api/dogs/:name/`

**Add a dog**

POST: `/api/dogs/` with `Content-Type: application/json` with at minimum a 'name' key

Sample POST request data:
```json
{
  "name": "fido",
  "colors": ["black", "white", "brown"],
  "breed": "bernese mountain dog",
  "weight": 100,
  "friends": ["rover", "spot", "lassie"],
  "owners": ["janine", "frederic"]
}
```

**Update a dog**

PUT: `api/dogs/:name/` with `Content-Type: application/json`

If they have already been set, you cannot update `owners`, `colors`, or `breed`

Any items in `friends` will be added to the dog's friends; they will not be overwritten.

Sampe PUT request `/api/dogs/fido/`:
```json
{
  "weight": 120,
  "friends": ["sparky"]
}
```

**Delete a dog**

DELETE: `api/dogs/:name/`

---
### Contributing
PR's welcome

1. Clone or download the repo
2. `pipenv install` to install the dependencies
3. `pipenv shell` to activate the virtual environment
4. `PYTHONPATH=. py.test` to run the tests
5. `python3 app.py` to run the server

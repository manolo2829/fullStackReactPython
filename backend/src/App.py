import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo, ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'
# --------------------------- MONGO ES LA CONEXION --------------------------- #
mongo = PyMongo(app)

# ------------ Apllicamos el CORS para poder interactuar con React ----------- #
CORS(app)

db = mongo.db.users


@app.route('/users', methods=['POST'])
def createUser():
    id = db.insert_one({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    })
    return jsonify(str(id.inserted_id))

@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in db.find():
       users.append({
           '_id': str(doc['_id']),
           'name': doc['name'],
           'email' : doc['email'],
           'password': doc['password']
       })
    return jsonify(users)


@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    user = db.find_one({'_id': ObjectId(id)})
    print(user)
    return jsonify({
        '_id': str(user['_id']),
        'name': user['name'],
        'email' : user['email'],
        'password': user['password']
    })


@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'User deleted'})


@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    db.update_one({'_id': ObjectId(id)}, {'$set': {
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password'],

    }})
    
    return jsonify({'msg': 'User Updated'})

if __name__ == "__main__":
    app.run(debug=True)
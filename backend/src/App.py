from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo, ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'
# --------------------------- MONGO ES LA CONEXION --------------------------- #
mongo = PyMongo(app)

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
    return 'received'


@app.route('/user/<id>', methods=['GET'])
def getUser():
    return 'received'


@app.route('/users/<id>', methods=['GET'])
def deleteUser():
    return 'received'


@app.route('/user/<id>', methods=['PUT'])
def updateUser():
    return 'received'

if __name__ == "__main__":
    app.run(debug=True)
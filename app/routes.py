from app import app , mongo
from app.models import User
from flask import  request, jsonify
from bson.objectid import ObjectId


db = mongo.db.users

@app.route('/user', methods=['POST'])
def createUser():
    try :
        data = request.get_json()
        user = User(**data)

        db.insert_one(user.to_dict())
        return jsonify({
            'message': 'User created'
        })
    except Exception as e:
        return jsonify({
            'message': 'User not created',
            'error': str(e)
        })
    
@app.route("/users", methods=['GET'])
def getAllUsers():
    try :
        users = []
        for user in db.find():
            users.append({
                '_id': str(user['_id']),
                'name': user['name'],
                'email': user['email'],
            })
        return jsonify({
            'message': 'Users fetched',
            'users': users
        })
    except Exception as e:
        return jsonify({
            'message': 'Users not fetched',
            'error': str(e)
        })
    
@app.route("/users/<id>", methods=['GET'])
def getUserById(id):
    try : 
        user = db.find_one({"_id":ObjectId(id)})
        if user:
            return jsonify({
                "name": user['name'],
                "email": user['email'],
                "id": str(user['_id'])
            })
        else:
            return jsonify({
                'message': 'User not found'
            })
    except Exception as e:
        return jsonify({
            'message': 'User not found',
            'error': str(e)
        })

@app.route("/users/<id>", methods=['PUT'])
def updateUser(id):
    try : 
        user = db.find_one({"_id":ObjectId(id)})
        if user:
            db.update_one({"_id":ObjectId(id)},{"$set":{"name":request.json['name'],"email":request.json['email']}})
            return jsonify({
                'message': 'User updated'
            })
        else:
            return jsonify({
                'message': 'User not found'
            })
    except Exception as e:
        return jsonify({
            'message': 'User not updated',
            'error': str(e)
        })

@app.route("/users/<id>", methods=['DELETE'])
def deleteUser(id):
    try :
        user = db.find_one({"_id":ObjectId(id)})
        if user:
            db.delete_one({"_id":ObjectId(id)})
            return jsonify({
                'message': 'User deleted'
            })
        else:
            return jsonify({
                'message': 'User not found'
            })
    except Exception as e:
        return jsonify({
            'message': 'User not deleted',
            'error': str(e)
        })
        


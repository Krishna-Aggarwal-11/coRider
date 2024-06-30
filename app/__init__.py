from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/CoRider'
mongo = PyMongo(app)

from app import routes , models

if __name__ == '__main__':
    app.run(debug=True)
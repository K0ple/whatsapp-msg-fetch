from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "put-your-connection-string"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('cfg')
user_collection = pymongo.collection.Collection(db, 'users')
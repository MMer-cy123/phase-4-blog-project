from flask import request,jsonify,make_response

from flask_restful import Resource

from config import app, api, db
from models import User, Comment, Post, Vote

class Index(Resource):
    def get(self):
        return {"message": "welcome to moringa blog api"}, 200
    
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(port=5500, debug = True)  
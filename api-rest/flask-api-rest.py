#!/usr/bin/env python
# coding: utf-8

# pip install flask-restful



from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)


tvs = [
    {
        "id" : "id1",
        "name" : "tv1",
        "price": 1000
    },
    {
        "id" : "id2",
        "name" : "tv2",
        "price": 2000
    },
    {
        "id" : "id3",
        "name" : "tv3",
        "price": 3000
    }
]





RESPONSE_OK = 200
RESPONSE_NOT_FOUND = 404
RESPONSE_CREATED = 201
RESPONSE_BAD_REQUEST = 400





class Tv(Resource):
    def get(self, id):
        for tv in tvs:
            if (tv["id"] == id):
                return tv, RESPONSE_OK
            
        return "Object not found", RESPONSE_NOT_FOUND
    
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("price")
        args = parser.parse_args()
        
        for tv in tvs:
            if (tv["id"] == id):
                return "Object with id " + id + " already exists", RESPONSE_BAD_REQUEST
            
        tv = \
        {
            "id" : id,
            "name" : args["name"],
            "price": args["price"]
        }
        
        tvs.append(tv)           
        return tv, RESPONSE_CREATED
        
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("price")
        args = parser.parse_args()
        
        tv = \
        {
            "id" : id,
            "name" : args["name"],
            "price": args["price"]
        }

        print(tv)
        
        for i in range(len(tvs)):
            if (tvs[i]["id"] == id):
                tvs[i] = tv
                return tv, RESPONSE_OK
            
        tvs.append(tv)           
        return tv, RESPONSE_CREATED
    
    def delete(self, id):
        print(id)
        for i in range(len(tvs)):
            if(tvs[i]["id"] == id):
                tv = tvs[i]
                del tvs[i]
                return tv, RESPONSE_OK
            
        return "Object with id " + id + "is not found", RESPONSE_NOT_FOUND




api.add_resource(Tv, "/tv/<string:id>")





app.run(debug = True, port = 5500)







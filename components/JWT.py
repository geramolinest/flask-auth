from flask import Flask, jsonify
from flask_jwt_extended import create_access_token, JWTManager,jwt_required,verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity


class JWTAuth:

    def __init__(self,app: Flask):
        self.app = app
        JWTManager(app)

    def generate_token(self,payload: dict):
        try:
            print(payload)
            token = create_access_token({'user': payload['user']})
            return jsonify({'access-token':token})
        except Exception as e:
            return jsonify(msg = e.args)

    @jwt_required()
    def hi(self):
        try:
            if verify_jwt_in_request():
                
                return jsonify('Hi')
        except Exception as e:
            return jsonify(msg = e.args)
    
from flask import Flask, jsonify,request
from components.JWT import JWTAuth


class Server:

    def __init__(self):

        self.app = Flask(__name__)
        self.OAuth = JWTAuth(self.app)
        self.config_app()
        self.router()

    def config_app(self):
        self.app.config['SECRET_KEY'] = 'secreto'

    def router(self):
        app = self.app

        @app.route('/hi')
        def protected_route():
            return self.OAuth.hi()
        
        @app.route('/')
        def greet():
            return jsonify({'msg':'Hello from flask running at geramolina.com'})
        
        @app.route('/login',methods = ['POST'])
        def login():
            payload = request.get_json()
            token = self.OAuth.generate_token(payload)
            return token
    
    def run(self):
        self.app.run(host='geramolina.com', port =8000,debug=True)
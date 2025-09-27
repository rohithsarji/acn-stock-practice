from flask import Flask
from flask_restx import Api
from app.controller import api as hello_nss


app = Flask(__name__)
api = Api(app, version='1.0', title='Hello NSS API', description='A simple Hello NSS API')
api.add_namespace(hello_nss, path='/api/hello')

if __name__ == '__main__':
    app.run(debug=True)
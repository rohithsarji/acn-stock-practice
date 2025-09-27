from flask_restx import Namespace, Resource
from flask import request
from app.service import greet_user

api = Namespace('hello', description='Hello NSS operations')
parser = api.parser()
parser.add_argument('name', type=str, required=True, help='Name to greet')

@api.response(200, 'Success')
@api.response(400, 'Validation Error')
@api.route('/')
class Hello(Resource):
    @api.expect(parser)
    def post(self):
        name = request.args.get('name')
        if not name:
            return {'message': 'Name is required'}, 400
        message = greet_user(name)
        return {'message': message}


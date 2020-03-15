from flask import request
from flask_restplus import Resource, Namespace, fields

from pets_api.daos.users import UserDAO

""" init the namespace for these routes """
api = Namespace('users', description='User(s) routes')

user = api.model('User', {
    'id': fields.String(required=True, description='user identifier'),
    'username': fields.String(required=True, description='username'),
})


@api.route('/')
class Users(Resource):
    """
    Users Resource
    """

    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        return UserDAO.get_all()


@api.route('/<id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class User(Resource):
    """
    User Resource
    """

    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self):
        # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                current_user = UserDAO.get({'id': resp})

                requested_user = UserDAO.get(request.json['username'])
                if UserDAO.role_can_access(current_user, requested_user):
                    response_object = {
                        'status': 'success',
                        'data': {
                            'user_id': requested_user.id,
                            'email': requested_user.email,
                            'admin': requested_user.admin,
                            'registered_on': requested_user.registered_on
                        }
                    }
                    return response_object, 200

            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401


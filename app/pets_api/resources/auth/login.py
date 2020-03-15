from flask import request
from flask_restplus import Resource, Namespace

from pets_api.daos.users import UserDAO

""" init the namespace for these routes """
api = Namespace('/login', description='Login user.')


@api.route('/login')
@api.response(403, 'Email or password incorrect.')
@api.response(500, 'Try again.')
class Login(Resource):
    """
    User Login Resource
    """

    @api.doc('POST - user login')
    def post(self):
        data = request.json
        try:
            # fetch the user data
            user = UserDAO.get({'email': data['email']})
            if user and user.verify_password(data['password']):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    return response_object, 200
            else:
                return 403
        except Exception as e:
            print(e)
            return 500


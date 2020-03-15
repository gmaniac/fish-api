from flask import request
from flask_restplus import Resource, Namespace

from pets_api.papi.daos.users import UserDAO

""" init the namespace for these routes """
api = Namespace('/register', description='Register user.')


@api.route('/register')
class Register(Resource):
    """
    Register User Resource
    """

    @api.doc('POST - user register')
    def post(self):
        return UserDAO.create(request.json)


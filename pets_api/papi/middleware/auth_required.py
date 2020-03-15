from flask import request
from functools import wraps

from pets_api.papi.daos.tokens import TokenDAO
from pets_api.papi.daos.users import UserDAO


def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        authorized = TokenDAO.get({'token': request.headers.get('Authorization')})
        if authorized and not UserDAO.check_blacklist(authorized.token):
            kwargs['user'] = UserDAO.get({'id': authorized.user})
            return f(*args, **kwargs)
        else:
            return "Login required", 401
    return decorator


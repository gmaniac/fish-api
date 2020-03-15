import udatetime

from pets_api.papi.documents.users import User
from pets_api.papi.documents.blacklist_tokens import BlacklistToken


class UserDAO:
    @staticmethod
    def create(data):
        user = User.objects(email=data['email']).first()
        if not user:
            new_user = User(
                email=data['email'],
                username=data['username'],
                date_created=udatetime.utcnow()
            )
            new_user.hashed_password = new_user.hash_password(data['password'])
            new_user.save()

            # generate the auth token
            auth_token = user.encode_auth_token(user.id)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': auth_token.decode()
            }

            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return response_object, 409

    @staticmethod
    def get_all():
        return User.objects().all()

    @staticmethod
    def get(kword):
        return User.objects(**kword).first()

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.objects(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False

    @staticmethod
    def role_can_access(current_user, requested_user):
        return current_user == requested_user or [role in [User.const_developer_role, User.const_admin_role] for role in current_user.roles]


import hashlib, binascii, os
import udatetime
import jwt
from datetime import timedelta

from mongoengine_goodjson import Document, EmbeddedDocument
from mongoengine import BooleanField, DateTimeField, EmbeddedDocumentListField, ListField, ReferenceField, StringField

# from pet_models.locations import Location
# from pet_models.blacklist_tokens import BlacklistToken


class Website(EmbeddedDocument):
    name = StringField()
    url = StringField()


class Avatar(EmbeddedDocument):
    image = BooleanField(default=False, required=True)
    background = StringField()
    url = StringField()


class User(Document):
    """User class."""
    const_user_role = 'user'
    const_buyer_role = 'buyer'
    const_author_role = 'author'
    const_seller_role = 'seller'
    const_developer_role = 'developer'
    const_admin_role = 'admin'
    const_roles = [const_user_role, const_buyer_role, const_author_role, const_seller_role, const_developer_role, const_admin_role]

    username = StringField(required=True, unique=True)
    first_name = StringField()
    last_name = StringField()
    profile_image = StringField()
    password_hash = StringField()
    # locations = ListField(ReferenceField(Location))
    roles = ListField(choices=const_roles, default=const_user_role, required=True)
    bio = StringField()
    curated_url = StringField()
    websites = EmbeddedDocumentListField(Website)
    avatar = EmbeddedDocumentListField(Avatar)
    date_created = DateTimeField(default=udatetime.utcnow)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    @staticmethod
    def hash_password(password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, provided_password):
        """Verify a stored password against one provided by user"""
        stored_password = self.password_hash
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def encode_auth_token(self, expiration, secret_key):
        """
        Generates the Auth Token
        ;param secret_key
        ;param expiration
        :return: string
        """
        try:
            payload = {
                'exp': udatetime.utcnow() + timedelta(**expiration),
                'iat': udatetime.utcnow(),
                'sub': self.id
            }
            return jwt.encode(
                payload,
                secret_key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token, secret_key):
        """
        Validates the auth token
        :param secret_key:
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, secret_key)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


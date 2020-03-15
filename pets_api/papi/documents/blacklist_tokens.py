import udatetime

from mongoengine_goodjson import Document
from mongoengine import DateTimeField, StringField


class BlacklistToken(Document):
    """
    Token Model for storing JWT tokens
    """
    token = StringField(max_length=500, unique=True)
    blacklisted_on = DateTimeField(default=udatetime.utcnow)

    def __repr__(self):
        return '<id: token: {}'.format(self.token)


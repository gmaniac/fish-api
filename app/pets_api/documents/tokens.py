import udatetime

from mongoengine_goodjson import Document
from mongoengine import DateTimeField, ReferenceField, StringField

# from pet_models.users import User


class Token(Document):
    """Token class."""
    # user = ReferenceField(User)
    type = StringField()
    name = StringField()
    token = StringField(max_length=500, unique=True)
    date_created = DateTimeField(default=udatetime.utcnow)


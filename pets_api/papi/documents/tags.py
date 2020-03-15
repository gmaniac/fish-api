import udatetime

from mongoengine_goodjson import Document
from mongoengine import DateTimeField, ListField, ReferenceField, StringField


class Tag(Document):
    """Tag class."""
    type = ListField(choices=['page', 'post', 'message', 'user', 'shop', 'product', 'location'], default=['user'], required=True)
    tag = StringField()
    parent = ReferenceField('self')
    taxonomy_id = StringField()
    date_created = DateTimeField(default=udatetime.utcnow)


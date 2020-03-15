import udatetime

from mongoengine_goodjson import Document, EmbeddedDocument
from mongoengine import BooleanField, DateTimeField, EmbeddedDocumentListField, ListField, StringField


class Meta(EmbeddedDocument):
    """Attachment Meta class."""
    type = ListField(choices=['file', 'doc', 'image', 'video'], default=['image'], required=True)
    extension = StringField()
    external = BooleanField(default=False)


class Attachment(Document):
    """Attachment class."""
    name = StringField()
    url = StringField()
    primary = BooleanField(default=False)
    meta = EmbeddedDocumentListField(Meta)
    description = StringField()
    date_created = DateTimeField(default=udatetime.utcnow)


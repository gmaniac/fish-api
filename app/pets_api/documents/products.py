import udatetime

from mongoengine_goodjson import Document
from mongoengine import BooleanField, DateTimeField, FloatField, IntField, ListField, StringField


class Product(Document):
    """Product class."""
    name = StringField()
    description = BooleanField()
    featured = BooleanField(default=False)
    price = FloatField(min_value=0)
    dimensions = ListField(FloatField(min_value=0))
    per_order = IntField(min_value=1)
    inventory = IntField(min_value=0)
    available = IntField(min_value=0)
    backorder = IntField(min_value=0)
    date_created = DateTimeField(default=udatetime.utcnow)


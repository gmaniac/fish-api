import udatetime

from mongoengine_goodjson import Document
from mongoengine import BooleanField, DateTimeField, FloatField, ListField, ReferenceField, StringField

# from pet_models.products import Product


class Sale(Document):
    """Sale class."""
    name = StringField()
    description = BooleanField()
    # products = ListField(ReferenceField(Product))
    discount = FloatField(min_value=0)
    active = BooleanField(default=False)
    start_date = DateTimeField()
    end_date = DateTimeField()
    date_created = DateTimeField(default=udatetime.utcnow)


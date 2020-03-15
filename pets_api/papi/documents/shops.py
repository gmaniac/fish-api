import udatetime

from mongoengine_goodjson import Document
from mongoengine import BooleanField, DateTimeField, ListField, ReferenceField, StringField

from pet_models.locations import Location
from pet_models.products import Product
from pet_models.sales import Sale
from pet_models.users import User


class Shop(Document):
    """Shop class."""
    ein = StringField()
    name = StringField()
    owners = ListField(ReferenceField(User))
    approved = BooleanField(default=False)
    products = ListField(ReferenceField(Product))
    locations = ListField(ReferenceField(Location))
    sales = ListField(ReferenceField(Sale))
    date_created = DateTimeField(default=udatetime.utcnow)


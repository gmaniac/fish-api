import udatetime

from mongoengine_goodjson import Document
from mongoengine import BooleanField, DateTimeField, ListField, StringField, PointField


class Location(Document):
    """Location class."""
    name = ListField(choices=['home', 'shop', 'shipping', 'billing'], default=['home'], required=True)
    primary = BooleanField()
    street1 = StringField()
    street2 = StringField()
    city = StringField()
    state = StringField()
    statecode = StringField()
    postcode = StringField()
    country = StringField()
    countrycode = StringField()
    timezone = StringField()
    geo = PointField()
    date_created = DateTimeField(default=udatetime.utcnow)

    def get_coordinates(self):
        return {'longitude': self.geo.coordinates[0], 'latitude': self.geo.coordinates[1]}


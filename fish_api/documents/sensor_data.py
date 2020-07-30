import udatetime

from fish_api.db import db

from fish_api.documents.sensor import Sensor


class SensorData(db.Document):
    """Sensor Data class."""
    sensor = db.ReferenceField(Sensor)
    value = db.StringField()
    unit = db.StringField()
    date_created = db.DateTimeField(default=udatetime.utcnow)


import udatetime

from fish_api.db import db

from fish_api.documents.system import System


class Sensor(db.Document):
    """Sensor class."""
    const_moisture_sensor = 'moisture'
    const_ph_sensor = 'ph'
    const_sonar_sensor = 'sonar'
    const_temperature_sensor = 'temperature'
    const_total_dissolved_solids_sensor = 'tds'
    const_turbidity_sensor = 'turbidity'
    const_types = [const_moisture_sensor, const_ph_sensor, const_sonar_sensor, const_temperature_sensor,
                   const_total_dissolved_solids_sensor, const_turbidity_sensor]

    name = db.StringField()
    type = db.ListField(db.StringField(), choices=const_types)
    system = db.ReferenceField(System)
    description = db.StringField()
    date_created = db.DateTimeField(default=udatetime.utcnow)


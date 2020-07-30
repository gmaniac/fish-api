import udatetime

from fish_api.db import db


class System(db.Document):
    """System class."""
    name = db.StringField()
    description = db.StringField()
    date_created = db.DateTimeField(default=udatetime.utcnow)


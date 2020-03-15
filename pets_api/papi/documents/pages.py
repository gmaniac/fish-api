import udatetime

from mongoengine_goodjson import Document
from mongoengine import DateTimeField, ListField, ReferenceField, StringField, LongField

from pet_models.seos import SEO
from pet_models.tags import Tag
from pet_models.users import User


class Page(Document):
    """Page class."""
    title = StringField()
    author = ListField(ReferenceField(User))
    seo = ReferenceField(SEO)
    date_created = DateTimeField(default=udatetime.utcnow)
    stage = ListField(choices=['draft', 'published'], default=['draft'], required=True)
    body = StringField()
    excerpt = StringField(max_length=140)
    tags = ListField(ReferenceField(Tag))
    template = StringField(default='page')
    curated_url = StringField()
    order = LongField(default=0)


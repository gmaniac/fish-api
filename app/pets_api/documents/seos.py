import udatetime

from mongoengine_goodjson import Document, EmbeddedDocument
from mongoengine import BooleanField, DateTimeField, EmbeddedDocumentListField, ListField, ReferenceField, StringField

# from pet_models.users import User


class Article(EmbeddedDocument):
    """SEO Article class."""
    published_time = StringField()
    # author = ListField(ReferenceField(User))
    tag = StringField()


class Media(EmbeddedDocument):
    """SEO Media class."""
    url = StringField()
    type = StringField()
    width = StringField()
    height = StringField()


class OG(EmbeddedDocument):
    """SEO OG class."""
    url = StringField()
    title = StringField()
    description = StringField()
    site_name = StringField(default="Pets Shop")
    image = EmbeddedDocumentListField(Media)
    video = EmbeddedDocumentListField(Media)
    article = EmbeddedDocumentListField(Article)


class SEO(Document):
    """SEO class."""
    title = StringField()
    description = StringField(max_length=280)
    keywords = ListField(StringField())
    noindex = BooleanField(default=False)
    nofollow = BooleanField(default=False)
    noodp = BooleanField(default=False)
    noydir = BooleanField(default=False)
    og = EmbeddedDocumentListField(OG)
    tracker = StringField()
    date_created = DateTimeField(default=udatetime.utcnow)


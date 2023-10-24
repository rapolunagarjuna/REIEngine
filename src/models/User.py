from mongoengine import Document, StringField, IntField

class User(Document):
    username = StringField(required=True, unique=True)
    age = IntField()
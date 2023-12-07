from mongoengine import Document, StringField, IntField, EmailField

class User(Document):
    username = StringField(required=True, unique=True)
    age = IntField()
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
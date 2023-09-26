from flask import Flask
from src.handlers.DefaultHandler import default
from src.handlers.PropertyHandler import property

app = Flask(__name__)
app.register_blueprint(default)
app.register_blueprint(property)

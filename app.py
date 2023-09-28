from flask import Flask
from src.handlers.DefaultHandler import default
from src.handlers.PropertyHandler import property
from src.handlers.MFToolHandler import mftool

app = Flask(__name__)
app.register_blueprint(default)
app.register_blueprint(property)
app.register_blueprint(mftool)

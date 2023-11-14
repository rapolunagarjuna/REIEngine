from flask import Flask
from src.handlers.DefaultHandler import default
from src.handlers.PropertyHandler import property
from src.handlers.MFToolHandler import mftool
from src.handlers.SchoolsHandler import schools
from src.handlers.UserHandler import user
from src.handlers.CalculatorHandler import calculator
from mongoengine import connect

from constants.uri import MONGODB_URI

application = Flask(__name__)
connect(db='realEstate', host=MONGODB_URI);

application.register_blueprint(default)
application.register_blueprint(property)
application.register_blueprint(mftool)
application.register_blueprint(schools)
application.register_blueprint(user)
application.register_blueprint(calculator)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
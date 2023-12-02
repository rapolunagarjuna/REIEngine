from flask import Flask
from src.handlers.DefaultHandler import default
from src.handlers.PropertyHandler import property
from src.handlers.MFToolHandler import mftool
from src.handlers.SchoolsHandler import schools
from src.handlers.UserHandler import user
from src.handlers.CalculatorHandler import calculator
from mongoengine import connect
from flask_cors import CORS


from constants.uri import MONGODB_URI

app = Flask(__name__)
CORS(app)
connect(db='realEstate', host=MONGODB_URI);

app.register_blueprint(default)
app.register_blueprint(property)
app.register_blueprint(mftool)
app.register_blueprint(schools)
app.register_blueprint(user)
app.register_blueprint(calculator)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.host = "0.0.0.0"
    app.port = 5000
    app.debug = True
    app.run()
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/login")
@app.route("/signup")
def home():
    return render_template("login.html")

if __name__ == '__main__':
      app.run(host="localhost", port=80, debug=True)
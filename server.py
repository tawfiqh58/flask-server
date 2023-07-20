from flask import Flask
from routes.scrap import scrap_route

app = Flask(__name__)

app.register_blueprint(scrap_route)

@app.route("/")
def method_name():
    return "<p>Restricted!</p>"
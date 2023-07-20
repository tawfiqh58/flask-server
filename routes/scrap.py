from flask import Blueprint

scrap_route = Blueprint('scrap-route-bp', __name__) # This is router extender instance

@scrap_route.route('/scrap') # This is the /end-point
def scrap_handler(): # You can give any name unique in this file, flask will call it
    return "<p>Scrap!</p>"
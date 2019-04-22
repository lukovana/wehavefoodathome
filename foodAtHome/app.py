import foodAtHome
from flask import Flask
# ??? creating an instance of the Flask class using the special __name__ variable
website = Flask(__name__)

@website.route("/")
def index():
    recipe = foodAtHome.getRecipe()
    return "<html><body><p>" + recipe + "</p></body></html>"
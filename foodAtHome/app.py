import foodAtHome
from flask import *
from flask_cors import CORS
# ??? creating an instance of the Flask class using the special __name__ variable
website = Flask(__name__)
CORS(website)

# this is where we get the list of ingredients from the user  ??? myaeb
@website.route("/input", methods = ['GET', 'POST'])
def inputList():
    ingredient = request.form['ingredient']
    return ingredient

@website.route("/test")
def index():
    recipe = str(foodAtHome.getRecipe())
    return recipe

if __name__ == '__main__':
    app.run(debug=True, port=5000)
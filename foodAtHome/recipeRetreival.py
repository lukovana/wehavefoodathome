import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

#  Necessary variables for MongoDB
client = MongoClient("127.0.0.1", 27017)
database = client.recipe
collection = database.ingredients

# WIP # WIP # WIP # WIP # WIP # WIP #
#
#  findRecipe(ingredient, ingredients)
#  Searches through the Mongo database to retrieve a list
#  of recipes depending on the user's input
#
#  RETURNS: list of recipes
#
def findRecipe(ingredient, ingredients):

   # Initialize counter
   count = 0

   #  we also gotta figure out what to do if the user enters an ingredient
   #  that's not in the database. must validate user input. figure out how 
   #  these dictionaries work. this isnt that big of a problem
   item = collection.find( {"ingredients": ingredient}, 
                           {"_id": 0, "url": 1, "tag": 1, "attribute": 1, 
                           "recipeContent": 1})

   # Initialize list that will store query of recipes. Must be two dimensional
   # ERROR ! count() is a deprecated method. they have an alterative, but 
   # i gotta work on that. for now tho, this code runs fine
   recipeQuery = [[x for x in range(4)] for y in range(item.count())]

   for recipe in item:

      url = recipe.get("url")
      tag = recipe.get("tag")
      attribute = recipe.get("attribute")
      content = recipe.get("recipeContent")

      recipeQuery[count][0] = url
      recipeQuery[count][1] = tag
      recipeQuery[count][2] = attribute
      recipeQuery[count][3] = content

      count += 1
   return recipeQuery

#  processRecipe(url, tag, attribute, content)
#  Parses the html from a web page into text.
#
#  RETURNS: recipe that has been scraped
#
def processRecipe(url, tag, attribute, content):

   response = requests.get(url)
   page = response.text
   soop = BeautifulSoup(page, 'html.parser')

   recipe_elmt = soop.find(tag, attrs={attribute: content})
   recipe = recipe_elmt.text.strip()

   return recipe
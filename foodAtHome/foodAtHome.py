#  APRIL 20th 2019
#     (line 82) ERROR ! count() is a deprecated method.
#     (line 75) input validation
from recipeRetreival import *
from random import *
import app

def getRecipe():

   # Initialize iterator
   i = 0

   # Initialize lists
   recipeList = []
   ###ingredientList = []

   ingredients = app.inputList()
   ingredientList = ingredients.split(", ")
   
   ###for item in ingredientList:
   ###   ingredientList[item] = ingredients[item]

   ###userList = ['celery', 'potato', 'apple', 'onion']

   # Retrieve the recipes needed for the ingredients the user entered.
   for item in ingredientList:

      # Collects all possible recipes for the user's query into a list
      recipes = findRecipe(item, ingredientList)

      for i in range(len(recipes)):
         # Parses the HTML from the recipe websites into text
         recipeText = processRecipe(recipes[i][0], recipes[i][1], recipes[i][2], recipes[i][3])
         recipeList.append(recipeText)

   # Have the program pick a random recipe from the list you made above
   randIdx = randomRecipe(0, len(recipeList) - 1)

   # Display the recipe
   print("\n", recipeList[randIdx], "\n")
   print(randIdx, "the length: ", len(recipeList))

   return recipeList[randIdx]

#  def randomRecipe(recipeFirst, recipeLast)
#  Generates a single random recipe from a list
#  of recipes
#
#  RETURNS: int index for the recipeList
#
def randomRecipe(recipeFirst, recipeLast):
   index = randint(recipeFirst, recipeLast)
   return index

getRecipe()
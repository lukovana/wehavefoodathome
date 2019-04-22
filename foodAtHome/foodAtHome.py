#  APRIL 20th 2019
#     (line 82) ERROR ! count() is a deprecated method.
#     (line 75) input validation
from recipeRetreival import *
from random import *

def getRecipe():

   # Initialize iterator
   i = 0

   # Initialize recipe list
   recipeList = []

   # WIP # WIP # WIP # WIP # WIP # WIP #
   # Have the user enter ingredients into a list
   #
   #  this is probably gonna change if we are getting
   #  the input from react
   #
   userList = userIngredient()

   # Retrieve the recipes needed for the ingredients the user entered.
   for ingredient in userList:

      # Collects all possible recipes for the user's query into a list
      recipes = findRecipe(ingredient, userList)

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

#  userIngredient()
#  Prompts user to enter ingredients
#
#  RETURNS: list of ingredients
#
def userIngredient():
   
   # Initialize variables and lists
   choice = "no"
   ulist = []
   counter = 0
   
   # Prompts user to enter an ingredient until they are satisfied.
   # It's possible that the way the loop is driven will change
   while (choice[0] != "n" or choice[0] != "N"):
      ingredient = input("Enter ingredient: ")
      ulist.append(ingredient)
      choice = input("Do you have any more to enter? (Y/N): ")
      
      if choice[0] == "n" or choice[0] == "N":
         break

   return ulist

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
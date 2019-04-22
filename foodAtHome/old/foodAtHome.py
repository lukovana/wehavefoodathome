import requests
from bs4 import BeautifulSoup
from ingredients import *

def main():
   userList = userIngredient()
   print(userList)   #  just verifying its existence
   recipes, ingredients = loopingList(userList)

   for recipe in recipes:
      print(recipe, "\n")

   for ingredient in ingredients:
      print(ingredient, "\n")
      
def userIngredient():
   
   choice = "no"
   ulist = []
   counter = 0
   
   # Prompts user to enter an ingredient until they are satisfied
   while (choice[0] != "n" or choice[0] != "N"):
      ingredient = input("Enter ingredient: ")
      ulist.append(ingredient)
      choice = input("Do you have any more to enter? (Y/N): ")
      
      if choice[0] == "n" or choice[0] == "N":
         break

   return ulist

def processRecipe(url, tag, attribute, content):

   response = requests.get(url)
   page = response.text
   soop = BeautifulSoup(page, 'html.parser')

   # The contents inside of the find() method should also be a parameter
   recipe_elmt = soop.find(tag, attrs={attribute: content})
   recipe = recipe_elmt.text.strip()

   return recipe

def loopingList(ulist):
   # Initialize loop accumulator
   count = 0
   userCount = 0

   # Initialize lists
   siteRecipeList = []
   siteIngredList = []

   for element in ingredientList:
      print(count, element)               # testing to see how loop is working

      for ingredient in ulist:
         print("\n", ingredient, "\n")    # testing to see how loop is working
         if ingredient == element:
            recipeText = processRecipe(
               assets[count][0], assets[count][1], 
               assets[count][2], assets[count][3]) # "3" is the preparation class name
            ingredientText = processRecipe(
               assets[count][0], assets[count][1], 
               assets[count][2], assets[count][4]) # "4" is the ingredient class name
            siteRecipeList.append(recipeText)
            siteIngredList.append(ingredientText)

      count += 1
   
   return siteRecipeList, siteIngredList


main()
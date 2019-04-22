import requests
from bs4 import BeautifulSoup

def main():

   # This url is bound to change. This should be a parameter
   url = 'https://iheartumami.com/thai-peanut-sauce-cucumber-noodles/?fbclid=IwAR1dxzTltQ6LeWHa5ycuh3w5E6HNAhTHmR5KMcM6UV8n-CDB_XJ6M1IXE2k'
   response = requests.get(url)
   page = response.text
   soop = BeautifulSoup(page, 'html.parser')

   # The contents inside of the find() method should also be a parameter
   tag = 'div'
   attribute = 'class'
   contentAttr = 'wprm-recipe-instruction-group'
   recipe_elmt = soop.find(tag, attrs={attribute: contentAttr})
   recipe = recipe_elmt.text.strip()

   print(recipe)

main()

# def processRecipe(url, tag, attribute, content):
#
#    response = requests.get(url)
#    page = response.text
#    soop = BeautifulSoup(page, 'html.parser')
#
#    # The contents inside of the find() method should also be a parameter
#    recipe_elmt = soop.find(tag, attrs={attribute: content})
#    recipe = recipe_elmt.text.strip()
#
#    return recipe

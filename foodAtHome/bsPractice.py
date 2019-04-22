import requests
from bs4 import BeautifulSoup

def main():

   # This url is bound to change. This should be a parameter
   url = 'https://www.cooks.com/recipe/as5n36k2/depression-era-potato-pancakes.html?fbclid=IwAR0NSvAYTlPyK4TzHF9W9-5ld3gn3wQLhlEqSaxyFpqUBcKr_91IapzRGwk'
   response = requests.get(url)
   page = response.text
   soop = BeautifulSoup(page, 'html.parser')

   # The contents inside of the find() method should also be a parameter
   tag = 'div'
   attribute = 'class'
   contentAttr = 'instructions'
   recipe_elmt = soop.find(tag, attrs={attribute: contentAttr})
   recipe = recipe_elmt.text.strip()

   print(recipe)

main()

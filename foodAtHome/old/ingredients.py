#
#   so this is one VERY tedious implementation that does not use a database
#   instead me, the programmer, practically creates a database using python
#   lists/tuples which is pretty ridiculous and redundant when i could be
#   using mongoDb. im a dummy
#
#   aanyways im keeping this IN CASE i decide to revert back to it
#   in the mean time i am gonna try to use mongo my dudes
#



# url | tag | attribute | content | INGREDIENT CONTENT (assets[]4)
cucumberAssets = [
    'https://iheartumami.com/thai-peanut-sauce-cucumber-noodles/?fbclid=IwAR1dxzTltQ6LeWHa5ycuh3w5E6HNAhTHmR5KMcM6UV8n-CDB_XJ6M1IXE2k', #url
    'div','class','wprm-recipe-instruction-group','wprm-recipe-ingredients-container wprm-block-text-normal'
]
celeryAssets = [
    'https://www.epicurious.com/recipes/food/views/celery-soup-51246210/amp?fbclid=IwAR2LphkPQCXbsmsFEjimyZSPHXAOSKRqC_9ma8-nBkoOdf2m4TUf1AltOrU',
    'div','class','preparation-group', 'ingredient-group']
potatoAssets = [
    'https://www.gimmesomeoven.com/5-ingredient-potato-soup/?fbclid=IwAR351FovvPx0JYyaLHj1JAgTYNHOkKPHV7LQr9ILp0H5sS0X41PkziFme9Y',
    'div','class','instructions','ingredients'
]
appleAssets = [
    'https://divascancook.com/best-southern-fried-apples-recipe/'
    'div','class','instructions-container','ingredients-container'
]

# these are the parents of the above assets
ingredientList  = ["celery", "cucumber", "potato", "apple"]
assets          = [celeryAssets, cucumberAssets, potatoAssets, appleAssets]
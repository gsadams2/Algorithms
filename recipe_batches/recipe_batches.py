#!/usr/bin/python

import math

pancake_recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
pancake_ing = { 'milk': 198, 'butter': 52, 'cheese': 10 }


def recipe_batches(recipe, ingredients):
  total = []
 
  for i in recipe:
    if i in ingredients:
      for j in ingredients:
        if j == i:
          total.append(ingredients[j] // recipe[i] )
    else:
      return 0

  max_output = min(total)
  return max_output

print(recipe_batches(pancake_recipe, pancake_ing))



# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
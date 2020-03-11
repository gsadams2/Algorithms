#!/usr/bin/python



import sys

denominations = [1, 5, 10, 25, 50]

# Write a function `making_change` that receives as input an amount of money 
# in cents as well as an array of coin denominations and calculates the total 
# number of ways in which change can be made for the input amount using the given coin denominations.

def making_change(amount, denominations):
  ways = [0] * (amount + 1)
  ways[0] = 1

  for coin in denominations:
    for higher_amount in range(coin, amount + 1):
      remainder = higher_amount - coin
      ways[higher_amount] += ways[remainder]

  return ways[amount]
  
making_change(300, denominations)


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
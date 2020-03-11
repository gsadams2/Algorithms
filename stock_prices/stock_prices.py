#!/usr/bin/python

import argparse

a = [1050, 270, 1540, 3800, 2]

def find_max_profit(prices):
  max_profit = None

  for i in range(0, len(prices)-1):
    for j in range(i + 1, len(prices)):
      profit_yo = prices[j] - prices[i]

      if max_profit is None:
        max_profit = profit_yo

      elif profit_yo > max_profit:
        max_profit = profit_yo
  
  return max_profit  
          

print(find_max_profit(a))


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
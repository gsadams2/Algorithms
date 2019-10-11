#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

#ways to eat 4 cookies... there are 7 ways (not sure if this is right)

#1111
#112
#121
#221
#22
#13
#31


#ways to eat 5 cookies... there are 13 ways 

#11111
#1112
#1121
#1211
#2111
#32
#23
#221
#122
#212
#311
#131
#113

def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      cache = {i: 0 for i in range(n+1)}
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

  












if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
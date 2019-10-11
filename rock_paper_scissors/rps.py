#!/usr/bin/python

import sys

# [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

def rock_paper_scissors(n):
  results = []
  base_options = [['rock'], ['paper'], ['scissors']]
  if n == 0:
    return [[]]
  if n == 1:
    return base_options
  else:
    for i in rock_paper_scissors(n-1):
      for j in base_options:
        results.append(i + j)
  return results



print(rock_paper_scissors(2))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
import sys
import random

def degeneration(a, b):
  for i in xrange(len(a)):
    if (a[i]==b[i]):
      return False
  return True

args = sys.argv[1:]
shuffled = args[:]
while not degeneration(args, shuffled):
  random.shuffle(shuffled)

print zip(args, shuffled)

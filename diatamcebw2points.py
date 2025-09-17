import sys

import math

if len(sys.argv) != 5:

  print("Usage: python program.py x1 y1 x2 y2")

  sys.exit(1)

x1 = float(sys.argv[1])

y1 = float(sys.argv[2])

x2 = float(sys.argv[3])

y2 = float(sys.argv[4])


manhattan = abs(x1 - x2) + abs(y1 - y2)


euclidean = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("Manhattan Distance:", manhattan)

print("Euclidean Distance:", euclidean)
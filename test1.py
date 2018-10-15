from math import floor, ceil

x = float(input())
if x % 1 > 0.5:
    print(ceil(x))
else:
    print(floor(x))

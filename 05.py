from math import floor

n = float(input())
n1 = floor(n)
n2 = (n % 1) * 100
print(n1, round(n2), sep=' ')

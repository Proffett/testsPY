a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if (d * a - b * c) != 0 and a != 0:
    y = ((f * a - e * c) / (d * a - b * c))
    x = ((e - b * y) / a)
    print(x, y)
else:
    x = f
    y = e
    print(x, y)

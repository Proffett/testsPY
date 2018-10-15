n = int(input())
b = 0
a = 1
s = 0
while a <= n:
    b = a * a
    s += b
    a += 1
else:
    print(s)

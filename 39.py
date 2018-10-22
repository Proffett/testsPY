m = -1
s = 0
b = 0
n = int(input())
while n != 0:
    if m == n:
        s += 1
    else:
        m = n
        b = max(b, s)
        s = 1
    n = int(input())
b = max(b, s)
print(b)

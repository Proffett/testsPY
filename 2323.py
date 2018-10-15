a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= b <= c:
    (a, b, c) = (a, b, c)
elif b <= a <= c:
    (a, b, c) = (b, a, c)
elif b <= c <= a:
    (a, b, c) = (b, c, a)
elif a <= c <= b:
    (a, b, c) = (a, c, b)
elif c <= a <= b:
    (a, b, c) = (c, a, b)
else:
    (a, b, c) = (c, b, a)

if a <= d and b <= e:
    print('YES')
else:
    print('NO')

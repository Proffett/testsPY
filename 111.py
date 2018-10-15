a, b, c = int(input()), int(input()), int(input())
if a == c and c < b:
    (a, b, c) = (a, c, b)
    print(a, b, c)
elif b == c and b < a:
    (a, b, c) = (b, c, a)
    print(a, b, c)
elif a == b and b < c:
    print(a, b, c)
elif a > b < c:
    if a > c:
        print(b, c, a)
    else:
        print(b, a, c)
elif b > a < c:
    if b > c:
        print(a, c, b)
    else:
        print(a, b, c)
elif a > c < b:
    if a > b:
        print(c, b, a)
    else:
        print(c, a, b)
elif c > b:
    print(b, a, c)
elif b > a:
    print(a, b, c)
elif b > c:
    print(c, b, a)

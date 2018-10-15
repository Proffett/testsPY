a, b, c = int(input()), int(input()), int(input())
if a == c and a == b and a == c:
    print(3)
elif a != b and a != c and b != c:
    print(0)
else:
    print(2)

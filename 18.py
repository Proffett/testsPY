a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if a1 <= b1 <= c1:
    (a1, b1, c1) = (a1, b1, c1)
elif b1 <= a1 <= c1:
    (a1, b1, c1) = (b1, a1, c1)
elif b1 <= c1 <= a1:
    (a1, b1, c1) = (b1, c1, a1)
elif a <= c <= b:
    (a1, b1, c1) = (a1, c1, b1)
elif c1 <= a1 <= b1:
    (a1, b1, c1) = (c1, a1, b1)
else:
    (a1, b1, c1) = (c1, b1, a1)
if a2 <= b2 <= c2:
    (a2, b2, c2) = (a2, b2, c2)
elif b2 <= a2 <= c2:
    (a2, b2, c2) = (b2, a2, c2)
elif b2 <= c2 <= a2:
    (a2, b2, c2) = (b2, c2, a2)
elif a2 <= c2 <= b2:
    (a2, b2, c2) = (a2, c2, b2)
elif c2 <= a2 <= b2:
    (a2, b2, c2) = (c2, a2, b2)
else:
    (a2, b2, c2) = (c2, b2, a2)
if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print('The first box is larger than the second one')
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')

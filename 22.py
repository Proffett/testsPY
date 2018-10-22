x = float(input())
y = float(input())
a = 1
if x == y:
    print(a)
while x < y:
    a = a + 1
    x = x + ((x / 100) * 10)
    if x > y:
        print(a)

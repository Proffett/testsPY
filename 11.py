n = int(input())
a = 0
b = a * a
while b < n:
    a = a + 1
    b = a * a
    if b > n:
        break
    print(b, end=' ')

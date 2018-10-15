n = int(input())
a = 1
while a <= n:
    a = a + 1
    if n % a == 0:
        print(a)
        break

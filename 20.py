n = int(input())
a = 2
if n == 2:
    print(a)
while n % a != 1:
    a = a + 1
    if n % a == 0:
        print(a)
else:
    print(a)

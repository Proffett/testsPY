a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a, end='')
elif b >= a and b >= c:
    print(b, end='')
else:
    print(c, end='')
if a <= b and a <= c:
    print(a, end='')
elif b <= a and b <= c:
    print(b, end='')
else:
    print(c, end='')
k = [a, b, c]
f = (a + b + c)
print(f - (min(k) + max(k)), sep='')

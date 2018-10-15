n = int(input())
Max = n
m = 0
while n != 0:
    if n >= Max:
        if n == Max:
            m += 1
        Max = n
    n = int(input())
print(m)

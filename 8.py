n = int(input())
if n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9:
    print(n, 'korov')
elif n % 10 == 0:
    print(n, 'korov')
elif n == 11 or n == 12 or n == 13 or n == 14:
    print(n, 'korov')
elif n == 1 or n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')

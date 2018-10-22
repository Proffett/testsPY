a = int(input())
b = int(input())
print('YES' * int(a % b == 0) or 'NO' * int(a % b != 0))

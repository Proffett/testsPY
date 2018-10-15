P = int(input())
X = int(input())
Y = int(input())
X1 = 100 * X + Y
Y1 = int(X1 * (100 + P) / 100)
print(Y1 // 100, Y1 % 100)

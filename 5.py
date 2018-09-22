A = int(input())
B = int(input())
N = int(input())
S = ((A * 100 + B) * N) % 100
F = ((A * 100 + B) * N) // 100
print(F, S)

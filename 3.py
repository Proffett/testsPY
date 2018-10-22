N = int(input())
B = (N % 1440) // 60
A = (N % 1440) % 60
print(B, str(' ') + str(A))

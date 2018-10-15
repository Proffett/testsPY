first = int(input())
i = first
second = 0
while (i != 0):
    if i > first:
        second, first = first, i
    elif second < i < first:
        second = i
    i = int(input())
print(second)

first = int(input())
i = 1
second = 0
while i != 0:
    if i > first:
        second, first = first, i
    elif second < i < first:
        second = i
    elif i == first:
        second = first
    i = int(input())
print(second)

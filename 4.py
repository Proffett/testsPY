pervstolb = int(input())
pervstr = int(input())
vtorstolb = int(input())
vtorstr = int(input())
if vtorstolb == pervstolb - 1 and vtorstr == pervstr - 1:
    print('YES')
elif vtorstolb == pervstolb - 1 and vtorstr == pervstr + 1:
    print('YES')
elif vtorstolb == pervstolb + 1 and vtorstr == pervstr + 1:
    print('YES')
elif vtorstolb == pervstolb + 1 and vtorstr == pervstr - 1:
    print('YES')
else:
    print('NO')

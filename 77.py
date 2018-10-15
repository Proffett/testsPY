pst = int(input())
pstr = int(input())
vst = int(input())
vstr = int(input())
if vst == pst - 1 and vstr == pstr - 1:
    print('YES')
elif vst == pst - 1 and vstr == pstr + 1:
    print('YES')
elif vst == pst + 1 and vstr == pstr + 1:
    print('YES')
elif vst == pst + 1 and vstr == pstr - 1:
    print('YES')
elif vst == pst and (vstr == pstr - 1 or vstr == pstr + 1):
    print('YES')
elif (vst == pst + 1 or vst == pst - 1) and vstr == pstr:
    print('YES')
else:
    print('NO')

str = input()
ind = str.find('f')
ind += 1
if str.find('f') >= 0 and str.find('f', ind) == -1:
    print(-1)
elif str.find('f') == -1:
    print(-2)
else:
    ind = str.find('f')
    ind += 1
    print(str.find('f', ind))

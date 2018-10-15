str = input()
ind = str.find('f')
ind += 1
if str.find('f') >= 0 and str.find('f', ind) == -1:
    print(str.find('f'))
elif str.find('f') >= 0:
    ind = str.find('f')
    s = len(str)
    ind += 1
    print(str.find('f'), str.rfind('f'), end=" ")

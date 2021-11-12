str1 = input().replace("+","")
ll = [int(el) for el in str1]
ll.sort()
zz=""
for i in range(len(ll)):
    zz+=f"+{str(ll[i])}"
print(zz[1:])
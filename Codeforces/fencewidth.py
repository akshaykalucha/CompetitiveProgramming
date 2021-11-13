n, h = map(int, input().split())
ll = list(map(int, input().split()))
zz = 0

for i in range(len(ll)):
    if ll[i] > h:
        zz += 2
    else:
        zz += 1
print(zz)
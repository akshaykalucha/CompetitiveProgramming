# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n,m = map(int, input().split())
segs = set()
cc= []
for _ in range(n):
    l,r = map(int, input().split())
    z = [i for i in range(l,r+1)]
    for el in z:
        segs.add(el)
for i in range(1,m+1):
    if i in segs:
        pass
    else:
        cc.append(i)
print(len(cc))
print(*cc)

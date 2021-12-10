# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    p,a,b,c = map(int, input().split())
    zz = [a,b,c]
    for i in range(len(zz)):
        if p%zz[i]==0:
            zz[i]=0
        else:
            zz[i] = zz[i]-(p%zz[i])
    print(min(zz))
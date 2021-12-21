# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(map(int, input().split()))
q = int(input())
for i in range(q):
    x,y = map(int, input().split())
    wire = x-1
    bcurr = ll[wire]
    belft = y-1
    bright = ll[wire]-y
    if wire-1>=0:
        ll[wire-1]+=belft
    if wire+1<n:
        ll[wire+1]+=bright
    ll[wire]=0
for el in ll:
    print(el)
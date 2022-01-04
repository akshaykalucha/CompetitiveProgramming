# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n, m  = map(int, input().split())
nl = list(map(int, input().split()))
ml = list(map(int, input().split()))
count = 0
nodd = 0
neven =  0
modd = 0
meven = 0
for i in range(len(nl)):
    if nl[i]%2==0:
        neven+=1
    else:
        nodd+=1
for i in range(len(ml)):
    if ml[i]%2==0:
        meven+=1
    else:
        modd+=1
print(min(nodd,meven)+min(neven,modd))
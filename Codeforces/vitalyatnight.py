# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n, m = map(int, input().split())
cc=0
for _ in range(n):
    ll = list(map(int, input().split()))
    i=1
    while i<(2*m):
        if ll[i]==1 or ll[i-1]==1:
            cc+=1
        i+=2
print(cc)
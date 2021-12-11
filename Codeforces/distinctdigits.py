# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

def solve(n):
    zz = str(n)
    kk = set(zz)
    if len(zz)==len(kk):
        return True
    return False

l,r=map(int, input().split())
f = False
for i in range(l,r+1):
    if solve(i):
        print(i)
        f = True
        break
if f == False:
    print(-1)
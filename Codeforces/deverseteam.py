# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n,k=map(int, input().split())
ll = list(map(int, input().split()))
zz = set(ll)
if len(zz)>=k:
    zz = list(zz)
    i=0
    print("YES")
    while k>0:
        print(ll.index(zz[i])+1, end=" ")
        i+=1
        k-=1
else:
    print("NO")
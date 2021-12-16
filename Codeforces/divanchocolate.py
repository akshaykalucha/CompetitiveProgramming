# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n,l,r,k = map(int, input().split())
    ll = list(map(int, input().split()))
    count = 0
    ll.sort()
    for i in range(len(ll)):
        if k-ll[i]<0:
            break
        if l<=ll[i]<=r:
            if k-ll[i]>=0:
                k-=ll[i]
                count+=1
        
    print(count)

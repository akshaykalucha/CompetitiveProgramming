# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n, d = map(int, input().split())
    ll = list(map(int, input().split()))
    if len(ll) == 1:
        print(ll[0])
    else:
        dist = 0
        for i in range(1,len(ll)):
            dist = i
            if ll[i]!=0:
                while d-dist>=0 and ll[i]>0:
                    ll[i]-=1
                    ll[0]+=1
                    d-=dist
        print(ll[0])
    
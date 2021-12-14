# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n,k = map(int, input().split())
    ll = [i for i in range(1,n+1)]
    flag = True
    if n%2!=0:
        if k>(n-1)//2:
            print(-1)
            flag=False
        else:
            currin = 1
            for i in range(k):
                ll[currin],ll[currin+1]=ll[currin+1],ll[currin]
                currin+=2
    else:
        if k > (n//2)-1:
            print(-1)
            flag = False
        else:
            currin = 1
            for i in range(k):
                ll[currin],ll[currin+1]=ll[currin+1],ll[currin]
                currin+=2
    if flag:
        print(*ll)
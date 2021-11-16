# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    o = 0
    e = 0
    if len(ll) == 1:
        if ll[0]%2==0:
            print(0)
        else:
            print(-1)
    else:
        for i in range(len(ll)):
            if i%2==0:
                if ll[i]%2!=0:
                    o+=1
            elif i%2!=0:
                if ll[i]%2==0:
                    e+=1
        if o!=e:
            print(-1)
        elif o==e:
            if (o+e)%2==0:
                print((o+e)//2)
    
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    q=sorted([a,b,c])
    if q[-1]==q[-2]:
        print('YES')
        if a==b:
            print(a,1,c)
        elif a==c:
            print(1,b,c)
        else:
            print(a,1,c)
    else:
        print('NO')
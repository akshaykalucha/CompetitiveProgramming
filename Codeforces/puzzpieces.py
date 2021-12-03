T=int(input())
for t in range(T):
    n,m=map(int,input().split())
    ans='NO'
    if n==1 or m==1:
        ans='YES'
    elif n==2 and m==2:
        ans='YES'
    print(ans)
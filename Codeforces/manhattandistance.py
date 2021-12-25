def solve():
    for _ in range(int(input())):
        x,y=map(int,input().split())
        xn=-1
        yn=-1
        for i in range(51):
            for j in range(51):
                if ((i+j)*2)==(x+y) and (2*(abs(x-i)+abs(y-j)))==(x+y):
                    xn=i
                    yn=j
        print(xn,yn)
 
solve()
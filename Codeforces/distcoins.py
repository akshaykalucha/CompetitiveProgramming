# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    a,b,c,n = map(int, input().split())
    mnum = max(a,b,c)
    suba = abs(mnum-a)
    subb = abs(mnum-b)
    subc = abs(mnum-c)
    n-= suba
    a+=suba
    n-=subb
    b+=subb
    n-=subc
    c+=subc
    if n < 0:
        print("NO")
    else:
        if n == 0:
            print("YES")
        else:
            if n == 1 or n == 2:
                print("NO")
            else:
                if n%3==0:
                    print("YES")
                else:
                    print("NO")

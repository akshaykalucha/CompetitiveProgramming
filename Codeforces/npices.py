# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')


for _ in range(int(input())):
    w,h,n = map(int, input().split())
    c = 1
    while True:
        if w%2==0:
            w /=2
            c*=2
        if h%2==0:
            h /=2
            c*=2
        if h%2!=0 and w%2!=0:
            break
    if c>=n:
        print("YES")
    else:
        print("NO")
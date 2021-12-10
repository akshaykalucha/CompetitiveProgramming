# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    b,p,f = map(int, input().split())
    h,c = map(int, input().split())
    price = 0
    if h >= c:
        while p>0 and b>1:
            price+=h
            b-=2
            p-=1
        while f>0 and b>1:
            price+=c
            b-=2
            f-=1
    else:
        while f>0 and b>1:
            price+=c
            b-=2
            f-=1
        while p>0 and b>1:
            price+=h
            b-=2
            p-=1
    print(price)
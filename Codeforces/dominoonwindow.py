# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n, k1, k2 = map(int, input().split())
    w,b = map(int, input().split())
    if k1+k2>=w*2 and 2*n-(k1+k2)>=b*2:
        print("YES")
    else:
        print("NO")
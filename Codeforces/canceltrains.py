# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n, m = map(int, input().split())
    bot = list(map(int, input().split()))
    left = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if bot[i] in left:
            c+=1
    print(c)
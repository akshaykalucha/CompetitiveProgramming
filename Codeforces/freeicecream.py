# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n, x = map(int, input().split())
dist = 0
for i in range(n):
    a, b = map(str, input().split())
    b = int(b)
    if a == '+':
        x += b
    else:
        if x >= b:
            x-=b
        else:
            dist += 1
print(x, dist)
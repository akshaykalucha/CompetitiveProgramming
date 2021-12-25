# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n, m = map(int, input().split())
cost = 9999999.0
for i in range(n):
    a, b = map(int, input().split())
    cc = m*(a/b)
    cost = min(cost,cc)
print(cost)
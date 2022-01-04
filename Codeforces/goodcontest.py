# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
f = False
for _ in range(n):
    name, before, after = map(str, input().split())
    if int(after)>=2400 and int(before)>=2400 and int(after)>int(before):
        f=True
if f:
    print("YES")
else:
    print("NO")
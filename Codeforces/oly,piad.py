# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n = int(input())
ll = list(map(int, input().split()))
z = set()
for i in range(len(ll)):
    if ll[i]!=0:
        z.add(ll[i])
print(len(z))
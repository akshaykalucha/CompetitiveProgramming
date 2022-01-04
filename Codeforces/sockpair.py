# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(map(int, input().split()))
cs = 0
table = set()
for i in range(len(ll)):
    if ll[i] not in table:
        table.add(ll[i])
        cs=max(cs,len(table))
    else:
        table.remove(ll[i])
print(cs)
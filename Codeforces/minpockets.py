# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n = int(input())
ll = list(map(int, input().split()))
d = {x: ll.count(x) for x in ll}
z = max(list(d.values()))
if z == 1 :
    print(1)
else:
    print(z)

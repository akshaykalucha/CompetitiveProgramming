# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(set(list(map(int, input().split()))))
ll.sort()
if len(ll)==1:
    print("NO")
else:
    print(ll[1])
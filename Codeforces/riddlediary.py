# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll={}
for i in range(n):
    name=input()
    if name in ll:
        print("YES")
    else:
        print("NO")
        ll[name]=1
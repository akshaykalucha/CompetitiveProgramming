# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ss = list(input())
c = 0
for i in range(len(ss)):
    if int(ss[i])%2==0:
        c+=i+1
print(c)
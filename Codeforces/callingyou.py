# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n, m, z = map(int, input().split())
kill = 0
for i in range(1,z+1):
    if i%m==0 and i%n==0:
        kill+=1
print(kill)
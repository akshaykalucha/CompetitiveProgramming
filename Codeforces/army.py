# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ds = list(map(int, input().split()))
a, b = map(int, input().split())
yrs = 0
i = a-1
while a!=b:
    yrs+=ds[i]
    i+=1
    a+=1
print(yrs)
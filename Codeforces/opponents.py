# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n, d = map(int, input().split())
totmax = 0
currmax = 0
for _ in range(d):
    st = [int(i) for i in input()]
    if sum(st)!=n:
        currmax+=1
    else:
        currmax=0
    totmax = max(totmax, currmax)
print(totmax)
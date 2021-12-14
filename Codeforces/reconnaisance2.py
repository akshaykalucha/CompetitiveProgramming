# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(map(int, input().split()))
currmin = [0,1]

for i in range(len(ll)):
    a = 0
    b = 0
    if i == n-1:
        solmin = abs(ll[i]-ll[0])
        a = i
        b = 0
    else:
        solmin = abs(ll[i]-ll[i+1])
        a = i
        b = i+1
    if solmin < abs(ll[currmin[0]] - ll[currmin[1]]):
        currmin = [a,b]
        
print(currmin[0]+1, currmin[1]+1)
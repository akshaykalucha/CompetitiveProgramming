# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(map(int, input().split()))
aa = []
for i in range(len(ll)):
    curr = ll[i]
    count = 0
    for j in range(len(ll)):
        if ll[j]>curr:
            count+=1
    aa.append(count+1)
print(*aa)
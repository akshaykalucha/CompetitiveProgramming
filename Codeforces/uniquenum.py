# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

t = int(input())
for times in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    schet = [0 for i in range(n + 1)]
    ind = [int(i) for i in range(n + 1)]
    for i in range(n):
        schet[a[i]] += 1
        ind[a[i]] = i + 1
    min_ind = -1
    for i in range(n + 1):
        if schet[i] == 1:
            min_ind = ind[i]
            break
    print(min_ind)
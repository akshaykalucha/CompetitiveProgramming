# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    ll.sort()
    flag = True
    for i in range(len(ll)-1):
        if abs(ll[i]-ll[i+1])==1:
            flag = False
            break
    if flag:
        print(1)
    else:
        print(2)
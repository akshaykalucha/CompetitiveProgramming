# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = list(map(int, input().split()))
ll.sort()
if ll[0]>=0:
    print(sum(ll))
else:
    aa = []
    for i in range(len(ll)):
        if ll[i]<0:
            aa.append(ll[i])
    if len(aa)==len(ll):
        print(abs(sum(aa)))
    else:
        print(sum(ll)-sum(aa)-sum(aa))

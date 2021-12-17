# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, k = map(int, input().split())
    ll = list(map(int, input().split()))
    count = 0
    ll.sort()
    i = 1
    while True:
        n = len(ll)
        if n==1:
            break
        if i==n:
            i=1
            continue
        if ll[-1]>=k or ll[-1]+ll[0]>k:
            ll.pop()
            continue
        ll[i]+=ll[0]
        i+=1
        count+=1
    print(count)
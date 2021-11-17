# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    ll.sort(reverse=True)
    curmin = 0
    for i in range(len(ll) - 1):
        if i == 0:
            curmin = ll[i]-ll[i+1]
        else:
            if ll[i]-ll[i+1] < curmin:
                curmin = ll[i]-ll[i+1]
    print(curmin)
# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    ll = []
    if n % 2 == 0:
        for i in range(n//2):
            ll.append(seq[i])
            ll.append(seq[-(i+1)])
    else:
        for i in range((n-1)//2):
            ll.append(seq[i])
            ll.append(seq[-(i+1)])
        ll.append(seq[(n-1)//2])
    print(*ll)
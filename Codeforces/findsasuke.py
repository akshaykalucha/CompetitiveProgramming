# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    i = 0
    b = []
    while i<n:
        b.append(ll[i+1])
        b.append(-ll[i])
        i+=2
    print(*b)
    
    mult = [a * b for a, b in zip(ll, b)]
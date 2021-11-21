# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(map(int, input().split()))
    odd = 0
    even  = 0
    for el in ll:
        if el%2==0:
            even+=1
        elif el%2!=0:
            odd+=1
    if odd==even:
        print("YES")
    else:
        print("NO")
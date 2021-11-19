# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    p1, p2, p3, p4 = map(int, input().split())
    if max(p1,p2)<min(p3,p4) or min(p1,p2)>max(p3,p4):
        print("NO")
    else:
        print("YES")
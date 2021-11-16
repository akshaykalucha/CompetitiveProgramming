# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

t=int(input())
for k in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = min(a)
    y = min(b)
    cc = 0
    for i in range(n):
        st1 = a[i]-x
        st2 = b[i]-y
        addup = abs(st1-st2)
        cc+=addup+(max(st1, st2)-addup)
    print(cc)
                    
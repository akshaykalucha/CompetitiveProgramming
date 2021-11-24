# import sys
# sys.stdin = open("Codeforces/input.txt", 'r')
# sys.stdout = open("Codeforces/output.txt", 'w')

for _ in range(int(input())):
    n = int(input())
    s = sorted(list(map(int, input().split())),reverse = True)
    if sum(s)%n:
        print(-1)
    else:
        need = sum(s)/n
        ans = 0
        for i in s:
            if need<i:
                ans += 1
        print(ans)
            
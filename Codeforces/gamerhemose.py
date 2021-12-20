# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n, H = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    x = a[-1]; y = a[-2]
    ans = H // (x + y) * 2
    H %= x + y
    if H > x: ans += 2
    elif H > 0: ans += 1
    print(ans)
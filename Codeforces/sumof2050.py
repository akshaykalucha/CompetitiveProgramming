# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    if n%2050!=0:
        print(-1)
    else:
        n//=2050
        ans = 0
        while n!=0:
            ans+=(n%10)
            n//=10
        print(ans)
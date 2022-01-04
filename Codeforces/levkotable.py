# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n, k = map(int, input().split())
for i in range(n):
    ll = [0]*n
    ll[i]=k
    print(*ll)
# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


n,m = map(int, input().split())
s=list(map(str, input().split()))
t=list(map(str, input().split()))
q = int(input())
for i in range(q):
    y = int(input())
    print(s[(y%n)-1]+t[(y%m)-1])
    